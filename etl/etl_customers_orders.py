import csv

input_file = "data/processed/orders_enriched.csv"
output_file = "data/processed/fact_orders.csv"

with open(input_file, mode="r") as infile, open(output_file, mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)

    fieldnames = [
        "order_id",
        "customer_id",
        "order_date",
        "total_amount"
    ]

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    kept = 0
    dropped = 0

    for row in reader:
        if not row["first_name"]:
            dropped += 1
            continue

        writer.writerow({
            "order_id": row["order_id"],
            "customer_id": row["customer_id"],
            "order_date": row["order_date"],
            "total_amount": row["total_amount"]
        })

        kept += 1

print("Orders kept:", kept)
print("Orders dropped:", dropped)
