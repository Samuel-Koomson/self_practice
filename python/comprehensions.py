new_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_list = []
for i in new_list:
    my_list.append(i)
print(my_list)
#this is a regular for loop that creates a new list using the append.
my_list1 = [n for n in new_list]
print(my_list1)

#using list comprehension allows for the execution of the same code in a much simpler way. the above code works perfectly just like the first code.

my_list = []
for i in new_list:
    my_list.append(i*i)
print(my_list)

my_list1 = [n*n for n in new_list]
print(my_list1)

#the above code uses both for loop and list comprehension to print the square root of the list

my_list = []
for i in new_list:
    if i% 2 == 0:
        my_list.append(i)
print(my_list)

my_list1 = [n%2 == 0 for n in new_list]
print(my_list1)

my_list1 = [n for n in new_list if n%2 == 0]
print(my_list1)

#these codes prints even numbers from the list. the first list comprehension code in this particular one prints to True instead of printing out the numbers in the list

list = []
for alpha in 'abc':
    for num in range (4):
        list.append((alpha, num))
    print(list)

list2 = [(alpha, num) for alpha in 'abc' for num in range (4)]
print(list2)

team = ['yanume', 'barbara', 'balogun', 'nyantakyiwaa', 'maryann']
member = ['harry', 'jude', 'rashid', 'cecil', 'efosa']
print(zip(team, member))
for t, m in zip(team, member):
    print(t, m)

#using the zip function, the two variables will be paired by their respective indices to create tuples. take note that when the first print is issued the zip function generates a zip object which is an iterator, thus in order to print the paired datat, there has to be an actual loop code

team_dict = {}
for team, member in zip(team, member):
    team_dict[team] = member
print(team_dict)

team_dict = {team: member for team, member in zip(team, member)}
print(team_dict)

#the same method of zipping can be used to create dictionaries by looping and list comprehensions. the list comprerhension in this situation produces an unexpected results which is yet to be rectified

set_num = [1, 2, 3, 1, 4, 2, 5, 6, 7, 8, 7, 9]
my_set_num = set()
for i in set_num:
    my_set_num.add(i)
    print(my_set_num)
    
set_comp = {i for i in set_num}
print(set_comp)

#set comprehensions work in similar ways as list and dictionary comprehensions
