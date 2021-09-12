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

   ''' mon1 = [4,6,9,11]
    for mnth in month_list:
        if month > 12:
            return None
        elif lp and month == 2:
            return 29
        elif month == 2:
            return 28
        elif month in mon1:
            return month_list[month-1]
        else:
            return month_list[month-1]'''

#START OF CUSTOMIZED INTERACTIVE CODE 
ip =''
while ip != 'exit':
    year = int(input('Enter Year: '))
    month = int(input('Enter Month: '))
    res = days_in_month(int(year),month)
    if res != None:
        print('Success\nNumber of days in',year,month,'is',res)
    else:
        print('Invalid')
    ip = input('Enter ok to continue or exit ')
    
#END OF CUSTOMIZED INTERACTIVE CODE 
                
'''
#DEFAULT or MANUAL CHECKED
test_years = [1900, 2000, 2016, 1987,2020]
test_months = [2, 2, 1, 11,17]
test_results = [28, 29, 31, 30,31]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")'''
'''
0-Jan 31
1-Feb 28
2-Mar 31
3-Apr 30*
4-May 31
5-Jun 30*
6-Jul 31
7-Aug 31
8-Sep 30*
9-Oct 31
10-Nov 30*
11-Dec 31
'''
