def is_year_leap(year):
    if year%4 == 0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

def days_in_month(year, month):
    lp = is_year_leap(year)
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if lp and month == 2:
        return 29
    else:
        return month_list[month-1]

def day_of_year(year, month, days):
#Write your new code here.
    day_res = days_in_month(year,month)
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = 0
    if days>31 and month > 12:
        return None
    elif month == 2 and days>29:
        return None
    else:
        for i in range(month):
            day += month_list[i]
        return day
    
print(day_of_year(1900, 12, 31))
