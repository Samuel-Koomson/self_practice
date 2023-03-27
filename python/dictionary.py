alien = {'age': 10, 'height': 7, 'color': 'black', 'point': 5} #defines a dictionary with key-value pairs.

alien['race1'] = 'black' #this code adds a new key-value pair to the dictionary

alien['color'] = 'blond' #changes the value of an existing key

alien.update({'age': 15, 'skin': 'chocolate', 'origin': 'ghana'}) #the update function can add a whole dictionary to the existying one by adding and modilfying it

del alien['skin'] #deletes key-value pairs from the dictionary. pop can also be used just like it was in the case of lists

print(alien)
print(alien['age']) # by calling the key 'age', the value of the alien's age is printed unto the console
print(alien.get('race')) #this returns a defualt answer that indicates that the key does not exist.
