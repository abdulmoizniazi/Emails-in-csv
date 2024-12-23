# Email Formatting and CSV Transposing Tools

This repository contains Python scripts for cleaning email lists and preparing them for use in Excel or other spreadsheet tools. 

## Features
1. **Email Format Cleaner**: Removes unnecessary spaces, multiple commas, and newlines from an email list, ensuring a properly formatted CSV.
2. **CSV Transposer**: Converts a row of emails in a CSV file into a single column for better organization in Excel.

---

## How to Use the Python Scripts

### **Email Format Cleaner**
1. Place your raw email list in a text file named `emails.txt`.
2. Run the following script to clean the email list:
   ```python
   python email_cleaner.py

To transpose your CSV file data so that all email addresses are placed in a single column in Excel, follow these steps:

---

### **Method 1: Using Excel's Transpose Feature**
1. **Open the CSV File**:
   - Open the `emails_cleaned.csv` file in Excel.
   - By default, all email addresses will appear in a single row.

2. **Copy the Row Data**:
   - Select the entire row of email addresses.
   - Right-click and choose **Copy**.

3. **Transpose Data into a Column**:
   - Click on a cell where you want the column to begin (e.g., `A1`).
   - Right-click and choose **Paste Special** → **Transpose**.
     - Alternatively, press **Alt + E + S + E** for the Paste Special > Transpose shortcut.

4. **Save the File**:
   - Save the file as an `.xlsx` or `.csv` file.

---

### **Method 2: Using Excel Power Query (Automated and Scalable)**

1. **Load the CSV File**:
   - Open a blank Excel workbook.
   - Go to **Data** → **Get Data** → **From File** → **From Text/CSV**.
   - Select the `emails_cleaned.csv` file and click **Load**.

2. **Transform the Data**:
   - In the Power Query Editor, select the column containing all the email addresses.
   - Click on the **Transform** tab and choose **Split Column** → **By Delimiter** → Select **Comma**.
   - This will split all email addresses into separate columns.

3. **Transpose Data**:
   - Select all the email columns.
   - Go to **Transform** → **Transpose**.
   - This will rearrange the data into a single column.

4. **Load Data Back**:
   - Click **Close & Load** to load the transformed data back into Excel.

---

### **Method 3: Use Python for Automation**

If you'd like to automate the process, use Python to transform your CSV file:

```python
import csv

# Read the cleaned CSV file
with open("emails_cleaned.csv", "r") as file:
    reader = csv.reader(file)
    emails = next(reader)  # Read the single row of emails

# Write emails to a new CSV file in a single column
with open("emails_transposed.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for email in emails:
        writer.writerow([email])
```

- This script reads your cleaned CSV file and creates a new file, `emails_transposed.csv`, where each email is written into a new row.

---

Choose the method that best fits your needs!


### Notes:
- Replace `email_cleaner.py` and `csv_transposer.py` with the actual filenames of your scripts.
- Include the `LICENSE` file in your repository for completeness if you mention it.
