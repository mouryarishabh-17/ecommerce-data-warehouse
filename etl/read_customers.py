import csv

input_file = "data/processed/customers_filtered.csv"
output_file = "data/processed/customers_enriched.csv"

with open(input_file, mode="r") as infile, open(output_file, mode="w", newline="") as outfile:
    reader = csv.DictReader(infile)

    fieldnames = reader.fieldnames + ["customer_region"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        country = row["country"]

        if country == "INDIA":
            region = "APAC"
        elif country == "USA":
            region = "NORTH_AMERICA"
        else:
            region = "UNKNOWN"

        row["customer_region"] = region
        writer.writerow(row)
