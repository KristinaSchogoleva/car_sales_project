# Architecture Diagram & Project Requirements
![Architecture Diagram](../img/diagram.png)
## Requirement

You have been approached by some local businesses (Cafe, Vets, Record Store, Car Dealership) to help them visualize their sales performance in terms of **sales and profit by store**.  

> For profit, assume a markup of:  
> - Cafe: 50%  
> - Vets: 70%  
> - Record Store: 20%  
> - Car Dealership: 40%  

You need to pick **one of the businesses above** for your pilot study, or create your own raw data in a text file for a business you are interested in.  

They also wish to include **customer buying habits**, such as:  
- What was purchased  
- How often items are purchased  
- How the products were paid for  

> All data must be **anonymized**, removing client names and card details at the earliest point of data ingestion.

The client is unsure which type of visualization is best, so they would like your **advice on visualization type** and the **best visualization tool** to use.  

They requested a **local pilot system** on **Windows or Mac**.  

The **raw data** will be provided as a text file, which is a subset of the data they want to process.  
> The data format may vary depending on the company type you choose.

If the pilot is successful, the solution must be **scalable** and easily migrated to **cloud or local server**.  

They would like you to explore at least **one data storage option** initially:  
- Using a Local Database  
- Using locally stored CSV files  

---

## Approach

You have a choice on how to build the solution:

### Choice 1
- Build a simple **ETL pipeline**: Extract → Transform → Load  
- Extract data from a source, **clean incorrect records** and remove **PII** (card number, name)  
- Upload data to a **local MySQL database** for storage  
- Use **Python, Docker, MySQL**, or other tools (Docker is optional)  
- Import data into a **visualization tool** for user-friendly display  

### Choice 2
- Import raw data, **clean and format** it  
- Produce **visualizations directly** from the visualization tool  
- Display in a **user-friendly format**  

---

## User Interface (UI)

The client leaves the choice up to you:  
1. Run an application from command prompt or icon with instructions  
2. Build a **CLI** or **GUI**  
3. Customize existing visualization tools with a **UI**  

---

## Data Source & Structure

**Record structure and data types**:  

Products - Customer Name, Product, Price, Branch, Payment Type, Card Number, Date/Time



Examples:  

- **Cafe Data:**  

Dave “Latte 2 £3.50” Epsom Card 0123456 12/08/2024

- **Car Data:**  
Carol Car: Tesla Model S £24,500 Guildford Cash 9528512 05/12/2024

- **Vets Data:**  
Carol Vaccination £45.00 Guildford Cash 9528512 05/12/2024

- **Record Shop Data:**  
Bob Album: “Hotel California” £3.50 Woking Cash 1713895 12/08/2024


---

## Delivery Deadline

- Approx **3 weeks** from project initiation

---

## Final Deliverables to the Client

- **Product demo** of the application functions (~5 mins)  
- **Client-facing presentation** (~5 mins) covering:  
- **HOW** - Tools/applications used  
- **WHAT** - Visualizations produced  
- **WHY** - Benefits to the client  

- **Document development process** explaining tools and components used  

---

## Source Control

- Use **GIT/GitHub** if coding the project  
- No branches required unless desired  
- If not coding, Git/GitHub optional for documentation  

---

## Tools for Coding Task

- **GIT/GitHub** – Version control  
- **VS Code** – IDE  
- **Python** – Run the code  

---

## Development Phases

### Phase 1 – Set up Development Infrastructure
1. Install Python  
2. Install VS Code  
3. Setup project directory structure  
4. Setup local GIT repository and connect to private GitHub repository  

### Phase 2 – Build and Test the Product
1. Create a simple **ETL and Data Visualization Program (app.py)**  

### Phase 3 – Final Deliverables
- Demo application  
- Presentation slides  

---

## Useful Links

### Data and Visualization
- [CSV to Grafana](https://grafana.com/blog/2025/02/05/how-to-visualize-csv-data-with-grafana/)  
- [TXT to CSV to Excel](https://www.exceldemy.com/convert-text-file-to-excel-automatically/)  
- [Python CSV and TXT files](https://softhandtech.com/transforming-txt-to-csv-a-guide-to-python-conversion)  
- [Matplotlib Cheatsheet](https://matplotlib.org/stable/users/cheatsheets.html)  
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)  
- [Power BI - Get data from CSV](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-csv-files)  
- [Power BI - Power Query Text/CSV connector](https://learn.microsoft.com/en-us/power-query/connectors/textcsv)  

### Development Environment
- [Python Downloads](https://www.python.org/downloads/) (tick "Add Python.exe to PATH")  
- [VS Code Download](https://code.visualstudio.com/download)  
- [GIT Bash](https://gitforwindows.org/)  
- [GitHub Signup](https://github.com)  
- [Microsoft Python Tutorials](https://www.youtube.com/watch?v=jFCNu1-Xdsw&t=1s)  
- [VS Code Tutorial](https://www.youtube.com/watch?v=jFCNu1-Xdsw&t=1s)
