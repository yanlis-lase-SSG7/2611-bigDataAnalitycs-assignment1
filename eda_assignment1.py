"""Audited Assignment I EDA over the nine validated Olist Parquet tables.

Run notebook 01 first. The CSV schema/FAILFAST gate and Snappy round trip live
there; this script independently re-reads orders with a typed FAILFAST schema.
Only small aggregate reports are collected to the Python driver.
"""

import csv
import json
import os
from pathlib import Path
import sys

from pyspark.sql import SparkSession, Window, functions as F
from pyspark.sql.types import StringType, StructField, StructType, TimestampType

ROOT = Path(os.environ.get("BDA_PROJECT_DIR", Path(__file__).resolve().parent)).resolve()
RAW = ROOT / "datasets_raw"
LAKE = ROOT / "datasets_parquet"
OUT = ROOT / "outputs_ml_graph"
RUNTIME = ROOT / ".runtime"


def configure_local_runtime():
    if os.name != "nt":
        raise RuntimeError("The verified local setup currently supports Windows only")
    javas = sorted(p for p in RUNTIME.glob("jdk-*") if (p / "bin/java.exe").is_file())
    if not javas:
        raise FileNotFoundError("Run setup_runtime.py before EDA")
    for name, value in {
        "JAVA_HOME": str(javas[-1]), "HADOOP_HOME": str(RUNTIME / "hadoop"),
        "SPARK_HOME": str(RUNTIME / "spark-home"),
        "PYSPARK_PYTHON": sys.executable, "PYSPARK_DRIVER_PYTHON": sys.executable,
    }.items():
        os.environ[name] = value
    os.environ["PATH"] = (str(javas[-1] / "bin") + os.pathsep +
                          str(RUNTIME / "hadoop/bin") + os.pathsep + os.environ["PATH"])
    temporary = RUNTIME / "tmp"
    temporary.mkdir(parents=True, exist_ok=True)
    for name in ("TMP", "TEMP", "TMPDIR"):
        os.environ[name] = str(temporary)


def write_csv(path, columns, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def main():
    configure_local_runtime()
    OUT.mkdir(exist_ok=True)
    spark = (SparkSession.builder.master("local[4]").appName("Olist_Assignment_I_EDA")
             .config("spark.driver.memory", "4g")
             .config("spark.sql.shuffle.partitions", "4")
             .config("spark.driver.bindAddress", "127.0.0.1")
             .config("spark.driver.host", "127.0.0.1")
             .config("spark.local.dir", str(RUNTIME / "spark-local"))
             .config("spark.sql.warehouse.dir", (RUNTIME / "spark-warehouse").as_uri())
             .config("spark.sql.session.timeZone", "America/Sao_Paulo")
             .getOrCreate())
    try:
        names = [
            "olist_customers_dataset", "olist_geolocation_dataset",
            "olist_order_items_dataset", "olist_order_payments_dataset",
            "olist_order_reviews_dataset", "olist_orders_dataset",
            "olist_products_dataset", "olist_sellers_dataset",
            "product_category_name_translation",
        ]
        frames = {}
        profile = {}
        for name in names:
            path = LAKE / f"{name}.parquet"
            if not path.is_dir():
                raise FileNotFoundError(f"Run notebook 01 first: {path}")
            df = spark.read.parquet(str(path))
            frames[name] = df
            fields = df.schema.fields
            nulls = df.agg(*[
                F.sum(F.when(F.col(field.name).isNull(), 1).otherwise(0)).alias(field.name)
                for field in fields
            ]).first().asDict()
            rows = df.count()
            profile[name] = {"rows": rows, "columns": len(fields), "fields": {
                field.name: {"type": field.dataType.simpleString(),
                             "null_count": int(nulls[field.name] or 0),
                             "null_pct": round(100 * int(nulls[field.name] or 0) / rows, 4)}
                for field in fields
            }}
            print(f"PROFILE {name}: {rows:,} rows", flush=True)

        critical_fields = {
            "olist_orders_dataset": ["order_id", "customer_id", "order_status",
                                      "order_purchase_timestamp", "order_estimated_delivery_date"],
            "olist_customers_dataset": ["customer_id", "customer_state"],
            "olist_order_items_dataset": ["order_id", "order_item_id", "seller_id", "product_id"],
            "olist_sellers_dataset": ["seller_id", "seller_state"],
            "olist_products_dataset": ["product_id"],
        }
        for table, columns in critical_fields.items():
            for column in columns:
                if profile[table]["fields"][column]["null_count"]:
                    raise ValueError(f"Critical null assertion failed: {table}.{column}")

        orders = frames["olist_orders_dataset"]
        customers = frames["olist_customers_dataset"]
        items = frames["olist_order_items_dataset"]
        sellers = frames["olist_sellers_dataset"]
        products = frames["olist_products_dataset"]
        if orders.schema["order_delivered_customer_date"].dataType != TimestampType():
            raise ValueError("Orders Parquet timestamp schema changed")
        # A second strict typed read demonstrates that malformed source values fail
        # before derived EDA is published. Notebook 01 additionally checks every CSV.
        order_schema = StructType([
            StructField("order_id", StringType(), False),
            StructField("customer_id", StringType(), False),
            StructField("order_status", StringType(), True),
            StructField("order_purchase_timestamp", TimestampType(), True),
            StructField("order_approved_at", TimestampType(), True),
            StructField("order_delivered_carrier_date", TimestampType(), True),
            StructField("order_delivered_customer_date", TimestampType(), True),
            StructField("order_estimated_delivery_date", TimestampType(), True),
        ])
        source_orders = (spark.read.schema(order_schema).option("header", True)
                         .option("enforceSchema", False).option("multiLine", True)
                         .option("mode", "FAILFAST")
                         .csv(str(RAW / "olist_orders_dataset.csv")))
        if source_orders.count() != profile["olist_orders_dataset"]["rows"]:
            raise ValueError("Typed FAILFAST order count differs from validated Parquet")

        orphan_rules = {
            "orders_to_customers": (orders, customers, "customer_id"),
            "items_to_orders": (items, orders, "order_id"),
            "items_to_sellers": (items, sellers, "seller_id"),
            "items_to_products": (items, products, "product_id"),
        }
        orphan_counts = {}
        for label, (child, parent, key) in orphan_rules.items():
            count = child.join(parent.select(key).dropDuplicates(), key, "left_anti").count()
            orphan_counts[label] = count
            if count:
                raise ValueError(f"Orphan assertion failed: {label}={count}")

        status_rows = [r.asDict() for r in orders.groupBy("order_status")
                       .agg(F.count("*").alias("orders"))
                       .orderBy(F.desc("orders")).collect()]
        if sum(r["orders"] for r in status_rows) != profile["olist_orders_dataset"]["rows"]:
            raise ValueError("Status counts do not reconcile")
        write_csv(OUT / "eda_order_status.csv", ["order_status", "orders"], status_rows)

        labeled = (orders.filter((F.col("order_status") == "delivered") &
                                 F.col("order_delivered_customer_date").isNotNull() &
                                 F.col("order_estimated_delivery_date").isNotNull())
                   .select("order_id", "customer_id", (F.col("order_delivered_customer_date") >
                           F.col("order_estimated_delivery_date")).cast("int").alias("is_delayed")))
        national = labeled.agg(F.count("*").alias("orders"),
                               F.sum("is_delayed").alias("delayed")).first()
        if national.orders != 96470 or national.delayed != 7826:
            raise ValueError("EDA delay population differs from validated report baseline")
        state = (labeled.join(customers.select("customer_id", "customer_state"), "customer_id")
                 .groupBy("customer_state")
                 .agg(F.count("*").alias("orders"), F.sum("is_delayed").alias("delayed")))
        state_rows = [{"customer_state": r.customer_state, "orders": r.orders,
                       "delayed": r.delayed,
                       "delay_rate_pct": round(100 * r.delayed / r.orders, 2)}
                      for r in state.orderBy(F.desc("delayed")).collect()]
        if sum(r["orders"] for r in state_rows) != national.orders or sum(
                r["delayed"] for r in state_rows) != national.delayed:
            raise ValueError("State breakdown does not reconcile to national orders")
        write_csv(OUT / "eda_state_delay.csv",
                  ["customer_state", "orders", "delayed", "delay_rate_pct"], state_rows)

        # Match notebooks 02/03: the smallest order_item_id defines primary seller.
        representative = (items.withColumn("position", F.row_number().over(
            Window.partitionBy("order_id").orderBy("order_item_id")))
            .filter(F.col("position") == 1).select("order_id", "seller_id"))
        # Ephemeral per-run salt avoids publishing stable source IDs. Only
        # state aggregates leave Spark; this is pseudonymization, not anonymity.
        salt = os.urandom(32).hex()
        seller_orders = (labeled.join(representative, "order_id", "inner")
                         .join(sellers.select("seller_id", "seller_state"), "seller_id")
                         .withColumn("seller_token", F.sha2(F.concat(
                             F.lit(salt), F.lit(":"), F.col("seller_id")), 256))
                         .drop("seller_id"))
        seller_total = seller_orders.agg(F.count("*").alias("orders"),
                                         F.sum("is_delayed").alias("delayed")).first()
        if seller_total.orders != national.orders or seller_total.delayed != national.delayed:
            raise ValueError("Primary-seller coverage does not reconcile")
        seller_rows = [
            {"seller_state": r.seller_state, "seller_count": r.seller_count,
             "orders": r.orders, "delayed": r.delayed,
             "delay_rate_pct": round(100 * r.delayed / r.orders, 2)}
            for r in seller_orders.groupBy("seller_state").agg(
                F.countDistinct("seller_token").alias("seller_count"),
                F.count("*").alias("orders"), F.sum("is_delayed").alias("delayed")
            ).orderBy(F.desc("orders")).collect()
        ]
        write_csv(OUT / "eda_seller_delivery.csv",
                  ["seller_state", "seller_count", "orders", "delayed", "delay_rate_pct"],
                  seller_rows)
        quality = {
            "definition": "delivered with non-null actual and estimated timestamps; actual > estimated",
            "national": {"orders": national.orders, "delayed": national.delayed,
                         "delay_rate_pct": round(100 * national.delayed / national.orders, 2)},
            "orphan_counts": orphan_counts, "tables": profile,
            "critical_null_assertions": {name: columns for name, columns in critical_fields.items()},
            "seller_attribution": "smallest order_item_id per order; state aggregates, not seller-level SLA",
            "privacy": "ephemeral salted SHA-256 seller tokens in Spark; no identifiers, tokens, or salt exported; state aggregates only; not anonymous",
        }
        (OUT / "eda_quality_profile.json").write_text(
            json.dumps(quality, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("PASS: 9 table profiles, 4 orphan checks, 96,470 labels, 7,826 delays")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
