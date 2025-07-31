from datetime import datetime

# Start date
start_date = datetime(2022, 7, 19)
today = datetime.now()

# Calculate the difference
years = today.year - start_date.year
months = today.month - start_date.month

if today.day < start_date.day:
    months -= 1

if months < 0:
    years -= 1
    months += 12

experience_str = f"Experience: {years} yrs {months} months"

# Update the README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

import re
updated_content = re.sub(r"Experience:.*", experience_str, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)
