# Car Dealership Sales Dashboard Project

## 1. Project Overview
This project is designed for a **local car dealership** to visualize sales and profit performance, as well as customer buying habits.  

The dashboard provides insights into:

- Total sales and total profit by branch  
- Customer purchase trends and frequency  
- Payment type distribution (Cash vs Card)  
- Top-selling car models  
- Sales trends over time  

**Important:** Customer-sensitive information such as names and card numbers has been removed to ensure data privacy.

---


# 2. Project Architecture

```text
Raw Data (.txt) ---> Python ETL Script ---> Processed Data (.csv) ---> Power BI Dashboard
```

Explanation:
1. Extract: Read car_sales_raw.txt with Python
2. Transform: Remove personal information, parse data, calculate profit (40% markup)
3. Load: Save cleaned data as car_sales_clean.csv
4. Visualize: Import CSV into Power BI to create interactive KPIs, charts, and trends

## 3. Project Structure


## 4. Tools and Technologies

Python 3.9+ – data cleaning and ETL

pandas, csv, re, datetime – parsing and transforming data

Power BI – dashboard creation with KPIs and interactive charts

Git & GitHub – version control

VS Code – development environment
