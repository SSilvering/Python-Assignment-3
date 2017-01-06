#===============================================================================#
#---------------------------Python Assignment 3---------------------------------# 
#                                                                               #
# Student 1:             Shai Hod     - 304800402                               #
# Student 2:             Dudu Abutbul - 200913671                               #
#===============================================================================#
from test._test_multiprocessing import get_value
from test.test_tools.test_unparse import nonlocal_ex
from setuptools.dist import sequence
from _elementtree import Element

# Question -1-
def make_date(year = 2000, month = 1, day = 1):   
    """
    This function returns a functional implementation of a mutable date form.
    @type year: Integers.
    @type month: Integers.
    @type day: Integers.
    """
    if not check_date(year, month, day):  # Checks if the date is correct.
        print("    An incorrect date. \nDefault date has been set.")
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

# TODO: need to be done.

#------------------------------------------------------------------------------ 
# Question -3-

def make_currency(amount = 0.0, symbol = ''):
    """
    This function stores a currency and its value.
    @param amount: Currency value.
    @type amount: Float.
    @param symbol: Currency sign.
    @type symbol: Unicode character.
    """
    def dispatch(message):
        """ This function returns the requested function based on the received text. """        
        if message == 'get_value':
            return get_value
        elif message == 'set_value':
            return set_value
        elif message == 'str':  # Prints a textual representation of this currency.
            print('{0}{1}'.format(symbol, amount))
        elif message == 'convert':
            return convert

    def get_value(msg):
        """ This function returns a specific element of the currency. """
        if msg == 'amount':
            return amount
        elif msg == 'symbol':
            return symbol
    
    def set_value(msg, value):
        """ This function sets a new value of a particular element of the currency. """
        nonlocal amount, symbol
        if msg == 'amount':
            amount = value
        elif msg == 'symbol':
            symbol = value

    def convert(func, new_sign):
        """ This function converts this specific currency to another currency. """
        nonlocal amount, symbol
        amount = func(amount)
        symbol = new_sign
    
    return dispatch

#------------------------------------------------------------------------------ 
# Question -4-
# TODO: write comments!!
def get_reverse_map_iterator(seq, func = None):
    
    reverse_map_iterator = []
    
    index = len(seq)
    
    if func:
        for _ in seq:
            index -= 1
            reverse_map_iterator.append(func(seq[index]))
    else:
        for _ in seq:
            index -= 1
            reverse_map_iterator.append(seq[index])
    
    def next():
        if has_more():
            nonlocal index
            index += 1
            return reverse_map_iterator[index - 1]
        else:
            return 'No more items.'
        pass
    def has_more():
        return index < len(seq)
    
    return {'next':next,'has_more':has_more}

#------------------------------------------------------------------------------ 
# Question -5-

# TODO: need to be done.
