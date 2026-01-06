import os
import logging
import subprocess


LOG_DIR = "etl"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "etl_pipeline.log")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

import subprocess

def main():
    logging.info("ETL pipeline started")

    # ---------- EXTRACTION ----------
    subprocess.run(["python", "etl/read_customers.py"], check=True)
    logging.info("Customer extraction completed")

    # ---------- TRANSFORMATION ----------
    subprocess.run(["python", "etl/etl_customers_orders.py"], check=True)
    logging.info("Customer and order transformation completed")

    # ---------- DATA QUALITY ----------
    subprocess.run(["python", "etl/data_quality.py"], check=True)
    logging.info("Data quality checks completed")

    logging.info("ETL pipeline completed successfully")


if __name__ == "__main__":
    main()



