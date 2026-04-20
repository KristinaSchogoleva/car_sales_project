# Car Dealership Sales Project

## 1. Project Overview
This project is designed for a **local car dealership** to visualize sales and profit performance, as well as customer buying habits.  

This analysis was designed to answer:

- Which branches generate the highest revenue and profit?
- Which car models perform best in terms of sales?
- How do customer payment preferences differ?
- What sales patterns and seasonality can be observed?
  
**Important:** Customer-sensitive information such as names and card numbers has been removed to ensure data privacy.

A sample Power BI dashboard is shown below:

![Car Sales Dashboard](images/dashboard.png)

---
## Key Insights from the Data

### Product Performance
- Tesla Model S and Ford Mustang are the best-performing models in terms of sales and profitability.
- BMW 3 Series shows strong performance in premium segments.

### Branch Performance
- Guildford and Woking generate the highest number of transactions and revenue.
- Redhill shows lower transaction volume compared to other branches.

### Profitability
- Higher-priced vehicles contribute significantly to overall profit.
- Premium sales generate the highest margins.

### Payment Behaviour
- Cash payments slightly dominate over card payments.
- Card payments are more common for higher-value transactions.

### Sales Trends
- Peaks in sales are observed in August and December, indicating seasonal demand patterns.

## Outcome

This project demonstrates the ability to:

- Build a full ETL pipeline from raw text data
- Clean and anonymize sensitive information (PII compliance)
- Engineer business-relevant metrics (profit calculation)
- Design a Power BI dashboard
- Extract actionable business insights
- 
# 2. Project Architecture

```text
Raw Data (.txt) ---> Python ETL Script ---> Processed Data (.csv) ---> Power BI Dashboard
```

Explanation:
1. Extract: Read car_sales_raw.txt with Python
2. Transform: Remove personal information, parse data, calculate profit (40% markup)
3. Load: Save cleaned data as car_sales_clean.csv
4. Visualize: Import CSV into Power BI to create interactive KPIs, charts, and trends




## 3. Tools and Technologies

Python 3.9+ – data cleaning and ETL
pandas, csv, re, datetime – parsing and transforming data
Power BI – dashboard creation with KPIs and interactive charts
Git & GitHub – version control
VS Code – development environment

## 4. Data Processing Steps

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
  
  ## 5. Power BI Dashboard Design

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

## 6. How to Run

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
