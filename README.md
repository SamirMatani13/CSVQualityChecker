# 📊 CSV Data Quality Checker

A lightweight Python tool to quickly analyze CSV files for data quality issues.
Generates a report showing missing values, duplicate rows, numeric and categorical statistics, and outliers.

---

## 🛠 Features

* ✅ Detects **missing values** and shows the rows containing them
* ✅ Finds **duplicate rows**
* ✅ Provides **basic numeric statistics** (mean, std, min, max, quartiles)
* ✅ Provides **categorical statistics** and full value counts
* ✅ Detects **outliers** using z-score and lists the rows with outliers
* ✅ Generates a **clean, easy-to-read text report**

---

## 🚀 Usage

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/csv-data-quality-checker.git
cd csv-data-quality-checker
```

2. **Install dependencies**:

```bash
pip install pandas numpy
```

3. **Run the tool**:

```bash
python checker.py sample.csv
```

* By default, the report is saved as `report.txt`.
* You can specify a custom output file:

```bash
python checker.py sample.csv --output my_report.txt
```

4. **Open the report** to review missing values, duplicates, stats, and outliers.

---

## 📂 Example Output

```text
📊 CSV Data Quality Report
========================================
Total Rows: 52
Total Columns: 5

🔎 Missing Values:
salary        1
department    1

Rows with missing values:
    id  age  salary department  years_experience
5    6   34     NaN        HR                 7
10  11   29  52000.0       NaN                 3

🔎 Duplicates:
 - 2 duplicate rows found:
   ...

📈 Numeric Column Statistics:
           id    age     salary  years_experience
count   52.00  52.00      51.00             52.00
mean    24.73  41.65   96551.61             17.17
std     14.82  17.07  132100.23              9.55
min      1.00  19.00   31016.00              0.00
25%     11.75  31.75   53365.00              9.75
50%     24.50  39.50   78984.00             19.00
75%     37.25  53.25  103237.00             26.25
max     50.00 120.00 1000000.00             29.00

📊 Categorical Column Statistics:
       department
count          51
unique          4
top     Marketing
freq           20

📊 Category Value Counts:
HR          12
Engineering 10
Marketing   20
Sales        9

⚠️ Outliers Detected:
 - 2 rows contain outliers:
    id   age    salary department  years_experience
20  21   40  1000000  Marketing                17
25  26  120    65000       Sales                12
```

---

## 📂 Sample CSV

You can create a `sample.csv` to test the tool immediately:

```csv
id,age,salary,department,years_experience
1,25,50000,HR,2
2,30,60000,Engineering,5
3,29,45120,HR,3
4,40,75000,Sales,10
5,34,,HR,7
6,28,55000,Marketing,4
7,33,58000,Sales,6
8,44,78345,Marketing,14
9,50,120000,Engineering,20
10,29,52000,,3
```

Save this as `sample.csv` in your repository folder to run the checker and see the report.

---

## 📌 Notes

* Works with **any CSV file**.
* Uses **z-score method** for numeric outlier detection.
* Designed to be **lightweight and easy to use** for quick data sanity checks.

