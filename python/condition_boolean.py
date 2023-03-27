game = 'baseball' #single = is an assignment 
if game == 'football': # double = tests for condition, this will be either true or false

    print("condition is true") #executes the condition if the statement is true
elif game == 'baseball':
    print('this is a new a game')
else:
    print('check and try again') #prints the alternative when the if statement is false

#boolean (and, or, not)
rent = 'expensive'
salary = 'small'
if rent == 'expensive' and salary == 'small': #the and boolean checks that two statements are true in order to execute to a true statement
    print('Accra stay by plan')
if rent == 'expensive' or salary == 'big': #in this case one true condition is enough to pass the test
    print('Accra still stay by plan')
if rent is not 'expensive' and salary is not 'small': #evaluates to the opposite of the condition, ie a true statement evaluate to false and vice-versa
    print('true')
else:
    print('false')
