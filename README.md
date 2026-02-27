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

## 5. Data Processing Steps

1. **Load raw data**  
   - Read data from `car_sales_raw.txt`

2. **Anonymize PII**  
   - Remove customer names  
   - Remove card numbers  

3. **Parse fields using regex**
   - `product` — car model  
   - `price` — sale price  
   - `branch` — dealership location  
   - `payment_type` — Cash or Card  
   - `date` — sale date (converted to `datetime`)  
   - `profit` — calculated using a 40% markup  

4. **Export processed data**
   - Save cleaned data to `car_sales_raw.csv`

5. **Data validation**
   - Verify data types  
   - Check for missing values  
   - Validate data consistency
   - Save data to `car_sales_final.csv`
  
  ## 6. Power BI Dashboard Design

### KPIs
- **Total Sales**
- **Total Profit**
- **Total Transactions**
- **Average Sale**

### Visualizations
- **Line chart** — sales trends over time  
- **Bar chart** — sales by branch  
- **Bar chart** — top-selling car models  
- **Pie chart** — payment type distribution  

### Interactivity
- Filters for **Branch**, **product** and **Date**  
- All KPIs and charts update dynamically based on selected filters


View the interactive Power BI dashboard here:  
[Car Sales Dashboard]()

## 7. How to Run

### Clone the repository
```bash
git clone https://github.com/YourUsername/car_sales_project.git
```
### Install dependencies
```bash
pip install pandas
```
### Run the ETL script
```bash
python scripts/clean_txt_to_csv.py
```

### Open the data in Power BI

Open the file below in Power BI and build the dashboard:
```bash
data/processed/car_sales_final.csv
```
