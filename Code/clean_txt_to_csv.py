import csv
import re
from datetime import datetime

file_txt = "car_sales_data.txt"
file_csv = "car_sales_raw.csv"

MARKUP = 0.4  # 40% for Car Dealership

pattern = re.compile(
    r"""
    ^\w+\s+                 # Customer name (to be removed)
    Car:\s(.+?)\s{2,}       # Car model
    £([\d,]+)\s{2,}         # Price
    (\w+)\s{2,}             # Branch
    (Cash|Card)\s{2,}       # Payment type
    \d+\s{2,}               # Card number (to be removed)
    (\d{2}/\d{2}/\d{4})     # Date
    """,
    re.VERBOSE
)

with open(file_txt, "r") as txt_file, open(file_csv, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

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
                match.group(5),
                "%d/%m/%Y"
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
