courses = ['history', 'geography', 'maths', 'admin', 'physics'] #creating a list in python
course1 = ['sociology', 'english']

print(courses) # displays the elements of the list

print(len(courses)) #tells the total number of elements in the list
print(courses[2]) #accesses the elements of the list using their indexes. indexing starts at 0 always

print(courses [-1]) #accesses elements from the end of the list.

print(courses[0:2]) #outputs the first two elements of the list. this [:2] provides the same output as the above code since the indexing starts from zero automatically
courses.append('arts') #adds a new element to the end of the list
courses.insert(3, 'music') #adds a new element to a specific location of the list
courses.insert(0, course1) #this generates a list within a list
courses.extend(course1) #unlike the insert method, the extend only adds the elements of the new variable not the entire list
courses.remove('admin') #deletes element from list
courses.pop() #this removes the last element from the list. popped elements can also be stored in a variable and called later when needed.
popped = courses.pop()
courses.reverse() #prints the list in reversed order

course1.sort()#prints list in alphabetical order
course1.sort(reverse=True)

print(course1)
print(popped)
print(courses)


"""tuples are similar to lists however they are  immutable and thus their elements cannot be modified"""

tuple = (12, 4, 7, 32, 78, 10)
tuple1 = tuple
print(tuple)
print(tuple1)

"""sets are lists that are not ordered and can change the order in which elements appear whenever it runs, it also prevents duplicates"""
code_set = {'language', 'keyboard', 'console', 'editor', 'screen'}

