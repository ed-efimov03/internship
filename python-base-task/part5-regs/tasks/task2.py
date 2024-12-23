import re
file_name = 'text2.txt'
f = open(file_name, 'r')
content = f.read()

DATE_PATTERNS = [
        r'\b(\w+)\s(\d{1,2}),\s(\d{4})\b',  # month dd year
        r'\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b',  # dd.mm.yyyy
    ]

MONTHS = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

dates = []

for pattern in DATE_PATTERNS:
        matches = re.findall(pattern, content)
        for match in matches:
            if pattern == DATE_PATTERNS[0]:
                month, day, year = match
                month = MONTHS[month]
            else:
                day, month, year = match
            
            # Форматируем дату в dd.mm.yyyy
            formatted_date = f"{day.zfill(2)}.{month.zfill(2)}.{year}"
            dates.append(formatted_date)

print(dates)
    

