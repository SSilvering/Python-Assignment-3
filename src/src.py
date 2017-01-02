#===============================================================================#
#---------------------------Python Assignment 3---------------------------------# 
#                                                                               #
# Student 1:             Shai Hod     - 304800402                               #
# Student 2:             Dudu Abutbul - 200913671                               #
#===============================================================================#

# Question -1-

def make_date(year = 2000, month = 1, day = 1):   
    """
    This function returns a functional implementation of a mutable date form.
    @type year: Integers.
    @type month: Integers.
    @type day: Integers.
    """
    def dispatch(msg):
        """
        
        @param msg:
        @type msg:
        """
        if msg == 'year':
            return year
        elif msg == 'month':
            return month
        elif msg == 'day':
            return day
    return dispatch

def get_date(dt, val):
    """
    
    @param dt:
    @type dt:
    @param val:
    @type val:
    """
    return dt(val)
#------------------------------------------------------------------------------ 
def day(dt):
    """
    
    @param dt:
    @type dt:
    """
    return get_date(dt, 'day')

def month(dt):
    """
    
    @param dt:
    @type dt:
    """
    if get_date(dt, 'month') == 1:
        return 'January'
    elif get_date(dt, 'month') == 2:
        return 'February'
    elif get_date(dt, 'month') == 3:
        return 'March'
    elif get_date(dt, 'month') == 4:
        return 'April'
    elif get_date(dt, 'month') == 5:
        return 'May'
    elif get_date(dt, 'month') == 6:
        return 'June'
    elif get_date(dt, 'month') == 7:
        return 'July'
    elif get_date(dt, 'month') == 8:
        return 'August'
    elif get_date(dt, 'month') == 9:
        return 'September'
    elif get_date(dt, 'month') == 10:
        return 'October'
    elif get_date(dt, 'month') == 11:
        return 'November'
    elif get_date(dt, 'month') == 12:
        return 'December' 

def year(dt):
    """
    
    @param dt:
    @type dt:
    """
    return get_date(dt, 'year')
#------------------------------------------------------------------------------ 
def str_date(dt):
    """
    
    @param dt:
    @type dt:
    """
    if day(dt) == 1:
        print('{0}st of {1}, {2}'.format(day(dt), month(dt), year(dt)))
    elif day(dt) == 2:
        print('{0}nd of {1}, {2}'.format(day(dt), month(dt), year(dt)))
    else:
        print('{0}th of {1}, {2}'.format(day(dt), month(dt), year(dt)))
    

d = make_date(2016, 12, 26)
d
# <function make_date.<locals>.dispatch at 0x02A880C0>
year(d)
# 2016
month(d)
# December
day(d)
# 26
str_date(d)
# 26th of December, 2016
