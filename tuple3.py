from datetime import date

def days_between_dates(date1, date2):
     d1 = date(date1[2], date1[1], date1[0])
     d2 = date(date2[2], date2[1], date2[0])
     return abs((d2 - d1).days)

 
date1 = (12, 5, 2022)
date2 = (25, 6, 2022)
print(days_between_dates(date1, date2))
