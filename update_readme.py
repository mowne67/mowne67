from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

# Start date
start_date = datetime(2022, 7, 19)
today = datetime.now()

# Calculate difference using relativedelta
diff = relativedelta(today, start_date)
years, months, days = diff.years, diff.months, diff.days

# Format experience string
experience_str = f"Experience: {years} yrs {months} months {days} days"

# Update the README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

updated_content = re.sub(r"Experience:.*", experience_str, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)
