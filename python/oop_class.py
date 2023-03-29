class Car:
    """A program that manufactures and uses car vehicles"""
    def __init__(self, name, model):
        """Initializes name and model attributes"""
        self.name = name
        self.model = model
    
    def move(self):
        """simulates a car moving"""
        print(f"new {self.name} car is now moving.")
    
    def stop(self):
        """simulates a car breaking to a stop"""
        print(f"my {self.name} has reduced speed and stopped")
#methods are functions in a class that can be called and used by instances of the class 
    
#creating an instance/object/type of car
first_car = Car('Toyota', 'Landcruiser')
print(f"My first car modeled is {first_car.name}.")
print(f"My first car model is {first_car.model}.")

next_car = Car('Mercedese', 'G-wagon')
print(f"my second car was {next_car.name} {next_car.model}.")

#in OOP naming conventions, capitalised varaibles are considered classes while lower cased variables are considered instances or objects

first_car.move()
next_car.stop()

#another example
class Restaurant:
    """Making a food production company"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print(f"These pieces of information about {self.name}")
    def open_restaurant(self):
        print(f"We are always opened to server great meals {self.name}")
        
restaurant = Restaurant('chillout', 'ghanaian')
print(f'Restaurant name {restaurant.name}.')
print(f'Restaurant meal {restaurant.cuisine}.')

old_restaurant = Restaurant('old_location', 'european')

restaurant.describe_restaurant()
old_restaurant.open_restaurant()

class Users:
    """Program depicts users of a software"""
    def __init__(self, first_name, last_name, age, sex, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.country = country
    
    def describe_user(self):
        print(f"The user {self.first_name} is a software engineering student")
        
    def greet_user(self):
        print(f"Hello {self.first_name} you are welcome to this platform")

user1 = Users('Kofi', 'Koomson', 34, 'male', 'Ghana')
user2 = Users('Kwame', 'Ntaadu', 28, 'male', 'Togo' )
user3 = Users('Barbara', 'Agyekum', 50, 'female', 'Canada')

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
