import csv

file_path = "data/processed/customers_enriched.csv"

missing_count = 0
total_rows = 0

with open(file_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        total_rows += 1

        if "" in row.values():
            missing_count += 1

print("Total customer records:", total_rows)
print("Records with missing values:", missing_count)

customer_ids = set()
duplicate_count = 0

with open(file_path, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        customer_id = row["customer_id"]

        if customer_id in customer_ids:
            duplicate_count += 1
        else:
            customer_ids.add(customer_id)

print("Duplicate customer_id records:", duplicate_count)

customer_ids = set()

with open("data/processed/customers_enriched.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        customer_ids.add(row["customer_id"])

invalid_orders = 0
total_orders = 0

with open("data/processed/orders_enriched.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_orders += 1
        if row["customer_id"] not in customer_ids:
            invalid_orders += 1

print("Total orders:", total_orders)
print("Orders with invalid customer_id:", invalid_orders)

sample_invalid = set()

with open("data/processed/orders_enriched.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["customer_id"] not in customer_ids:
            sample_invalid.add(row["customer_id"])
        if len(sample_invalid) >= 5:
            break

print("Sample invalid customer_ids:", sample_invalid)

valid_customer_ids = set()

with open("data/processed/customers_enriched.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        valid_customer_ids.add(row["customer_id"])

clean_orders = []

with open("data/processed/orders_enriched.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    for row in reader:
        if row["customer_id"] in valid_customer_ids:
            clean_orders.append(row)

output_path = "data/processed/orders_enriched_clean.csv"

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(clean_orders)

print("Clean orders written to:", output_path)
print("Clean order count:", len(clean_orders))

invalid_clean_orders = 0
total_clean_orders = 0

with open("data/processed/orders_enriched_clean.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_clean_orders += 1
        if row["customer_id"] not in valid_customer_ids:
            invalid_clean_orders += 1

print("Clean orders total:", total_clean_orders)
print("Invalid clean orders (should be 0):", invalid_clean_orders)

invalid_amount = 0
total_fact_rows = 0

with open("data/processed/fact_orders.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_fact_rows += 1

        total_amount = float(row["total_amount"])

        if total_amount <= 0:
            invalid_amount += 1

print("Total fact_orders rows:", total_fact_rows)
print("Rows with invalid total_amount (<=0):", invalid_amount)
