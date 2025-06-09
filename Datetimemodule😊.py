from datetime import datetime,date,timedelta


#Current date and time
now =datetime.now()
print("Current Date and Time:", now)
#----------------------------------------------#output (Current Date and Time: 2025-06-03 15:04:25.964407)


#Only current date
from datetime import datetime,date,timedelta

today =datetime.today()
print("Today's date",today)
#---------------------------------------#output  (Today's date 2025-06-03 15:12:17.198556)
print("year:", today.year)
#---------------------------------------#output  (year: 2025) 
print("Month:", today.month)
#----------------------------------------#output (Month: 6)
print("Day:", today.day)
#----------------------------------------#output (Day: 3)




#Date formatting
from datetime import datetime,date,timedelta
print("Formatted date:", now.strftime("%d-%m-%Y %H:%m:%S"))
#--------------------------------------------------------------#output (Formatted date: 03-06-2025 15:06:42)
print("Formatted date (Hindi style):",now.strftime("%A,%d %B %Y"))
#-------------------------------------------------------------------#output (Formatted date (Hindi style): Tuesday,03 June 2025)

"""    
"%d" :"Day of the month (01 to 30)",
"%d" :"Day of the month (01 to 31)",
"%m" :"Month as number (01 to 12)",
"%Y" :"Year with century (2025)",
"%H" :"Hour (00 to 22)",
"%S" :"Minute (00 to 58)",
"%A" :"Full weekday name (Tuesday)",
"%B" :"Full month name (June)" """



# Adding/subtracting dates
from datetime import datetime,date,timedelta
one_week_later = today + timedelta(days=7)
print("One week from today:", one_week_later)
#----------------------------------------------#output (One week from today: 2025-06-10 15:58:37.847952) 



#Difference between two dates
from datetime import date
today=date.today()
birthday = date(2016, 11, 18)
days_remaining =  today - birthday
print("Days remaining until next birthday:", days_remaining.days)                    #error



      


