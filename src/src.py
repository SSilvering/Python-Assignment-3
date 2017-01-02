#===============================================================================#
#---------------------------Python Assignment 3---------------------------------# 
#                                                                               #
# Student 1:             Shai Hod     - 304800402                               #
# Student 2:             Dudu Abutbul - 200913671                               #
#===============================================================================#

# Question -1-

def make_date(y=2000, m=1, d=1):

    dt = {'year':y, 'month':m, 'day':d}
    
    def dispatch(msg):
        if msg == 'year':
            return dt['year']
        elif msg == 'month':
            return dt['month']
        elif msg == 'day':
            return dt['day']
        elif msg == 'str_date':
            return str_date(dt)
        
    return dispatch

def year(date_func):
    return date_func('year')

def month(date_func):
    if date_func('month') == 1:
        return 'January'
    elif date_func('month') == 2:
        return 'February'
    elif date_func('month') == 3:
        return 'March'
    elif date_func('month') == 4:
        return 'April'
    elif date_func('month') == 5:
        return 'May'
    elif date_func('month') == 6:
        return 'June'
    elif date_func('month') == 7:
        return 'July'
    elif date_func('month') == 8:
        return 'August'
    elif date_func('month') == 9:
        return 'September'
    elif date_func('month') == 10:
        return 'October'
    elif date_func('month') == 11:
        return 'November'
    elif date_func('month') == 12:
        return 'December' 

def day(date_func):
    return date_func('day')

def str_date(date_func):
    if day(date_func) == 1:
        print('{0}st of {1}, {2}'.format(day(date_func), month(date_func), year(date_func)))
    elif day(date_func) == 2:
        print('{0}nd of {1}, {2}'.format(day(date_func), month(date_func), year(date_func)))
    else:
        print('{0}th of {1}, {2}'.format(day(date_func), month(date_func), year(date_func)))

d = make_date(2016, 12, 26)
print(d)
# <function make_date.<locals>.dispatch at 0x02A880C0>
print(year(d))
# 2016
print(month(d))
# December
print(day(d))
# 26
str_date(d)
# 26th of December, 2016