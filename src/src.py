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
    if not check_date(year, month, day):  # Checks if the date is correct.
        print("An incorrect date. sets a default date.")
        year, month, day = 2000, 1, 1
        
    def dispatch(msg):
        """ This function returns the requested function based on the received text. """
        if msg == 'year':
            return year
        elif msg == 'month':
            return month
        elif msg == 'day':
            return day
    return dispatch

def get_date(dt, val):
    """ getter date. """
    return dt(val)

def check_date(year, month, day):
    """ This boolean function checks if the date is correct. """
    if year < 2000:
        return False
    if month > 12:
        return False
    if day > 31:
        return False
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # Checks if it leap year.
            if not day <= 29:
                return False
        elif not day <= 28:
            return False
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if not day <= 31:
            return False
    if month == 4 or month == 6 or month == 9 or month == 11:
        if not day <= 30:
            return False
            
    return True
#------------------------------------------------------------------------------ 

def day(dt):
    """ getter for the day of specific date. """
    return get_date(dt, 'day')

def month(dt):
    """ Returns the name of the month of specific date. """
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
    """ getter for the year of specific date. """
    return get_date(dt, 'year')
#------------------------------------------------------------------------------ 

def str_date(dt):
    """ This function prints the date. """
    if day(dt) == 1:
        print('{0}st of {1}, {2}'.format(day(dt), month(dt), year(dt)))
    elif day(dt) == 2:
        print('{0}nd of {1}, {2}'.format(day(dt), month(dt), year(dt)))
    elif day(dt) == 3:
        print('{0}rd of {1}, {2}'.format(day(dt), month(dt), year(dt)))
    else:
        print('{0}th of {1}, {2}'.format(day(dt), month(dt), year(dt)))
#------------------------------------------------------------------------------

# Question -2-                                      
