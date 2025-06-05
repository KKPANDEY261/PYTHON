from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print("Current date and time:", now) #Current date and time: 2025-06-03 09:46:04.925352

# Only current date
today = date.today()
print("Today's date:", today)    #Today's date: 2025-06-03
print("Year:", today.year)       #Year: 2025
print("Month:", today.month)     #Month: 6
print("Day:", today.day)         #Day: 3

# Date formatting
print("Formatted date:", now.strftime("%d-%m-%Y %H:%M:%S"))            #Formatted date: 03-06-2025 09:46:04
print("Formatted date (Hindi style):", now.strftime("%A, %d %B %Y"))   #Formatted date (Hindi style): Tuesday, 03 June 2025

"""    "%d": "Day of the month (01 to 31)",
    "%m": "Month as number (01 to 12)",
    "%Y": "Year with century ( 2025)",
    "%H": "Hour (00 to 23)",
    "%M": "Minute (00 to 59)",
    "%S": "Second (00 to 59)",
    "%A": "Full weekday name (Tuesday)",
    "%B": "Full month name (June)"""

# Adding/subtracting dates
one_week_later = today + timedelta(days=7)    
print("One week from today:", one_week_later)        #One week from today: 2025-06-10

# Difference between two dates
birthday = date(2023, 12, 25)
days_remaining = birthday - today
print("Days remaining until next birthday:", days_remaining.days)       #Days remaining until next birthday: -526


birth=date(2022,11,13)
days= today-birth
print(days.days)