# Read the file
with open("emails.txt", "r") as file:
    content = file.read()

# Replace multiple spaces, commas, and newlines with a single comma
import re
cleaned_content = re.sub(r"[\s,]+", ",", content.strip())

# Save the cleaned content to a new file
with open("emails_cleaned.csv", "w") as file:
    file.write(cleaned_content)
