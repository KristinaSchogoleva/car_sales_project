import csv
import re
from datetime import datetime

# =========================
# Configuration
# =========================
INPUT_FILE = "car_sales_data.txt"
OUTPUT_FILE = "car_sales_raw.csv"
MARKUP = 0.4  # 40% profit markup for car dealership


# =========================
# Regex pattern for parsing
# =========================
pattern = re.compile(
    r"""
    ^\w+\s+                 # Customer name (removed / ignored)
    Car:\s(.+?)\s{2,}       # Car model
    £([\d,]+)\s{2,}         # Price
    (\w+)\s{2,}             # Branch
    (Cash|Card)\s{2,}       # Payment type
    \d+\s{2,}               # Card number (removed / ignored)
    (\d{2}/\d{2}/\d{4})     # Date
    """,
    re.VERBOSE
)


# =========================
# Data processing
# =========================
def process_sales_data(input_file: str, output_file: str) -> None:
    """
    Parses raw car sales data from TXT file,
    removes PII, calculates profit,
    and exports cleaned data to CSV.
    """

    with open(input_file, "r", encoding="utf-8") as txt_file, \
         open(output_file, "w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        # CSV header
        writer.writerow([
            "product",
            "price",
            "branch",
            "payment_type",
            "date",
            "profit"
        ])

        for line in txt_file:
            match = pattern.search(line)
            if match:
                product = match.group(1)
                price = float(match.group(2).replace(",", ""))
                branch = match.group(3)
                payment_type = match.group(4)
                date = datetime.strptime(
                    match.group(5), "%d/%m/%Y"
                ).date()

                profit = round(price * MARKUP, 2)

                writer.writerow([
                    product,
                    price,
                    branch,
                    payment_type,
                    date,
                    profit
                ])


# =========================
# Script entry point
# =========================
if __name__ == "__main__":
    process_sales_data(INPUT_FILE, OUTPUT_FILE)
    print("✅ Car sales data successfully processed and exported to CSV")

