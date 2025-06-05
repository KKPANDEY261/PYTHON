from datetime import date
today=date.today()
birthday = date(2016, 11, 18)
days_remaining =  today - birthday
print("Days remaining until next birthday:", days_remaining.days) 