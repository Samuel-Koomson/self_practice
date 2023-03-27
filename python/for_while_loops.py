numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for num in numbers: #prints out all the integers in the list
    for letter in 'abc': #loop within a loop
        print(num, letter)
        if num == 11: #conditions in loops
            print('I got this figured')
        
    if num in (3, 6, 9): #unlike the single number above, this line of code will not run if we use the double = sign like line 3
        #break or continue #determined whether the loop should end or go ahead to iterate after a condition has been met
        print('numbers found')
    print(num)
for i in range(5): #this loops through items for a specified number of times 
    print(i)
    
"""While loop"""
#the while loop executes a condition until the condition becomes false.
x = 0
while x < 10: 
    print(x)
    x += 1
#without the last line x += 1, the loop will go into infinite loop because 0 will always be less than 10
x = 1
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
#just like the for loop, the break also works in this situation
    
