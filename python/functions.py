""" Function is a block of code that performs a specific task. this fuction will always execute that block of code whenever it is called. the aim of functions is to keep the code DRY"""
def key():
    print('open door')
key()

x = 5
if x == 5:
    key()
    
if 6 > x and x < 7:
    key()
# the above simple function does not return anything. instead of printing multiple 'open door' the function allows you to open doors whenever key is called
def lock():
    return 'close door'
    lock() 
print(lock()) 
""" line 15 because this function has a return value, calling the function alone does not do anythin. on 17 however, calling the function with the print function produces the output of the lock function"""
# both functions do not take any arguements/inputs

def make_tea(water, beverage):

    if water and beverage:
        return "tea is ready"
    else:
        return "improper tea"
print(make_tea(1, 3))
#this function takes two arguements

def em_data(*args, **kwargs):
    print(args)
    print(kwargs)
em_data('sales', 'target', 'bonus', name='kofi', age=30, sex='male')
#the above function creates a tuple and a dictionary seperately when executed

em_1 = ['sales', 'target', 'bonus']
em_2 = {'name': 'kofi', 'age': 30, 'sex': 'male'}
em_data(em_1, em_2)
#the above code does the same thing as the other however it creates the tuple and dictionary together
em_data(*em_1, **em_2)
#order to have the tuple and dictionaries created differently like the first code, the function call should have the arguements preceeded by a pointer and double pointerlike 

def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(leap(2024))
#the above function checks whether a given year is a leap year or not
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and leap(year):
        return 29
    return month_days[month-1]
print(days_in_month(2021, 11))
#the above function also checks for the number of days in a month and whether that year is a leap year or not.
