def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res
"""print(daysInMonth(2019,10 ))"""


def dayOfYear(year, month, day):
    if year < 0 or month < 1 or month > 12 or day < 1 or day >31:
        return None
    else:
        if isYearLeap == True:
            return 366
        else:
            return 365
    
print(dayOfYear(2014,9,6))
    
    


"""
testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"-> ",end="")
	result = daysInMonth(yr, mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")
"""