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
