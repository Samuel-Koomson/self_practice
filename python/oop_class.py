# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Car:
    """A program that manufactures and uses car vehicles"""
    def __init__(self, name, model):
        """Initializes name and model attributes"""
        self.name = name
        self.model = model
        self.odometer = 0 #default attribute created
    
    def move(self):
        """simulates a car moving"""
        print(f"new {self.name} car is now moving.")
    
    def stop(self):
        """simulates a car breaking to a stop"""
        print(f"my {self.name} has reduced speed and stopped")
    
    def mileage(self, age, speed):
        distance = age * speed
        print(distance)
        return distance

            
#methods are functions in a class that can be called and used by instances of the class 
    
#creating an instance/object/type of car
first_car = Car('Toyota', 'Landcruiser')
print(f"My first car modeled is {first_car.name}.")
print(f"My first car model is {first_car.model}.")

next_car = Car('Mercedese', 'G-wagon')
print(f"my second car was {next_car.name} {next_car.model}.")

#in OOP naming conventions, capitalised varaibles are considered classes while lower cased variables are considered instances or objects
first_car.model = 'specification'
print(first_car.model) #direct change
print(next_car.model)
#when values are changed for attributes, the changes affect only the instances in question.

first_car.move()
next_car.stop()
first_car.mileage(5, 100)


#another example
class Restaurant:
    """Making a food production company"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.serving = 1 
    
    def describe_restaurant(self):
        print(f"These pieces of information about {self.name}")
    def open_restaurant(self):
        print(f"We are always opened to server great meals {self.name}")
    def order(self, number):
        request = number + 0
        print(request)
        return request

restaurant = Restaurant('chillout', 'ghanaian')
print(f'Restaurant name {restaurant.name}.')
print(f'Restaurant meal {restaurant.cuisine}.')

old_restaurant = Restaurant('old_location', 'european')
old_restaurant.serving = 10
print (old_restaurant.serving)

restaurant.describe_restaurant()
old_restaurant.open_restaurant()
old_restaurant.order(3)

class Ice_cream_Stand(Restaurant):
    def __init__Ice_cream_Stand(self, restaurant_name, cuisine_type, flavor):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = flavor
    def sales_point(self):
        print('Ice cream is sold right here')
buyer = Ice_cream_Stand('strawberry', 'flavor')
buyer.sales_point()


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

user1.age = 54
print(user1.age)
print('\n')

class Family:
    """Describes the family as a unit"""
    def __init__(self, members, home, vehicles, budget):
        self.members = members
        self.home = home
        self.vehicles = vehicles
        self.budget = budget
    
    def direct_members(self, parent, child):
        print(f"These are the direct members of the family {parent}, {child}")
    
    def residence(self, house):
        print(f"Family lives in {house} house")
    
    def fada1(self, expenditure):
        self.budget = expenditure
    print(f"budget updated to {'expenditure'} in the family")
    
father = Family( 'Daddy', 'Accra', 'BMW', 5000)
print({father.members}, {father.home}, {father.vehicles}, {father.budget})

#I really had a tough time figuring out how to call the attributes of the class to be printed unto the console using instances. 
father.direct_members('Daddy', 'Ama')
father.residence('green')
print('\n')

class Language:
    """Develops family of programming languages"""
    def __init__(self, syntax, errors, types):
        self.syntax = syntax
        self.errors = errors
        self.types = types
        self.beginning = 'start with C'
    
    def characters(self, do, dont):
        if do == 'accept': print('Go ahead')
        else:
            if dont == 'unaccepted': print("there's an error")
    
    def clean_code(self, serious):
        print(f" Your code is all clean and nice {serious}.")

c_program = Language('hard', 'error ridden', 'strict data type')
print({c_program.syntax}, {c_program.errors}, {c_program.types})

c_program.characters('accept', 'reject')
c_program.clean_code('Good job')
print(c_program.beginning)

#concepts perfect to this point, the outstanding issues are syntaxes
#How to modify attribute values

java = Language('complex', 'better than c', 'dynamic')
java.errors = 'reduced'
java.clean_code('Good job')
c_program.errors = 'reduced'
print(c_program.beginning)
c_program.clean_code('Good job')
#The above codes modify the attributes of an instance by direct assignment.
def update_jave(self, correction):
    self.errors = correction
print(f"errors have been modified to {'data'} corrections")

#INHERITANCE
class Used_Cars(Car):
    """This creates a new class of cars that deals with second-hand used cars"""
    def __init__(self, name, model, year):
        """Initializes attributes of the parent class to the child, this allows the child class to inherit parts or all of the attributes, methods and instances of the parent"""
        super().__init__(name, model)
        self.maintenance = 'monthly'
    def schedule_maintenance(self, date):
        if self.maintenance == 30 and date >= self.maintenanc:
            return self.maintenance
print(f"You are due for maintenance, schedule {31} now")
home_user = Used_Cars.schedule_maintenance('self', 31)   
#the super initialisation allows for the child class to call the parent method.
        
refurb_car = Used_Cars('benz', 'citron', 1995)
print(refurb_car.move())
