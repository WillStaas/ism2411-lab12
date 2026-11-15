import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

#SA Questions
#1 Python is better for automating repetitive tasks, handling large datasets, and performing complex data transformations. Excel is easier for organizing data, creating charts, and making quick edits. Python saves time when the same process needs to be repeated, while Excel is more user friendly for basic data analysis.
#2An online store could use append mode to keep track of customer orders. Every new order would be added to an existing CSV file without deleting previous records. This makes append mode useful because the business can maintain a continuous record of all its sales.





#Exercise 1

with open(SALES_FILE, "r") as f:
    print(f"Opened{SALES_FILE}.")

#Exercise 2
with open(SALES_FILE, "r") as f:
    reader =csv.reader(f)
    for row in reader:
        print(row)

#Exercise 3

with open(SALES_FILE, "r") as f:
    reader= csv.reader(f)
    header= next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

#exercise 4
total_revenue = 0
with open(SALES_FILE,"r") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str=row
        price= float(price_str)
        quantity= int(qty_str)
        total= price*quantity
        total_revenue += total
        print(f"{product}:{quantity}")

#exercise 5
with open(SALES_FILE,"r") as f:
    reader= csv.reader(f)
    next(reader)
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price= float(price_str)
        quantity= int(qty_str)
        total=price*quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open( CLEANED_FILE, "w", newline="") as f:
    writer= csv.writer(f)
    write.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

#exercise 6

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader= csv.DictReader(f)
    for row in reader:
        price=float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f}= ${total:.2f} ")

#exercise 7
summary={}

with open(SALES_FILE,"r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        product= row["product"]
        total= float(row["price"])* int(row["quantity"])
        summary[product]= summary.get(product,0)+total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

#exercise 8

timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"Log entries so far: {entries}")