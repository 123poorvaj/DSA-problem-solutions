import calendar
year=int(input("Enter which  year calendar you want: "))
month=int(input("Enter a month  number: "))
calendar=calendar.month(year,month)
print(calendar)
