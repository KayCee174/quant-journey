# Course 12 - Object-Oriented Programming
# by KayCee - April 20th, 2026

  # Course 12a - Introduction to OOP
# blueprints - classes && instances - objects
# attributes (__init__ method) - properties that define an object's individuality within a class
class Car:
  # Initialize attributes
  def __init__(self, brand, color):
    # Assign values to attributes
    self.brand = brand
    self.color = color
# Create an object of the Car class
my_car = Car('Audi', 'yellow')
print(my_car)
# Display attribute values
print(my_car.brand)
print(my_car.color)

# behaviours - 
class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color
  def honk(self):
    print("Beep beep!")
my_car = Car('Audi', 'yellow')
my_car.honk()

# function vs method 
# functions are independent and can be called on their own, while methods are associated with a class and can be called only with its instance

#function
def greet():
  print("Welcome!")
#list
prices = [55, 68, 77, 36]
#data types
x = 5
city = "London"
is_open = True
print(type(greet))
print(type(prices))
print(type(x))
print(type(city))
print(type(is_open))


  # Course 12b - Inheritance
# Inheritance lets a new class reuse attributes and methods from an existing class,
# while also adding or modifying its own unique features.
class Animal:
  def __init__(self, name):
    self.name = name
  def move(self):
    print("Moving")
# Inherits from Animal class
class Dog(Animal):
  # Specific behavior
  def bark(self):
    print("Woof!")
# Creating an instance
my_dog = Dog("Bob")
# Inherited attribute and behavior
print(my_dog.name)
my_dog.move()
# Specific behavior
my_dog.bark()

# super().__init__() to inherit and then define any additional attributes
#parent class
class Animal:
  def __init__(self, name):
    self.name = name
  def move(self):
    print("Moving")
#child class
class Dog(Animal):
  def __init__(self, name, breed, age):
    # Initialize attributes of the superclass
    super().__init__(name)
    # Additional attributes specific to Dog
    self.breed = breed
    self.age = age
  def bark(self):
    print("Woof!")
my_dog = Dog("Jax", "Bulldog", 5)
#inherited attribute
print(my_dog.name)
#Additional attributes
print(my_dog.breed)
print(my_dog.age) 

# method overriding
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name
  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")
# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  # Overridden sound method for Dog
  def sound(self):
    print("Woof!")
# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  # Overridden sound method for Cat
  def sound(self):
    print("Meow!")
# Creating instances
my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)
# Using overridden methods
my_dog.sound()
my_cat.sound()

# super() - if you want to call a method from the parent class while overriding it
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name
  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")
# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age  
  # Overridden sound method for Dog
  def sound(self):
    # Call the sound method from Animal
    super().sound()
    # Additional functionality for Dog
    print("Woof!")
# Creating an instance of Dog
my_dog = Dog("Jax", "Bulldog", 5)
# Calling the overridden sound method
my_dog.sound()

# polymorphism - lets object use method in their own way, even if they share the same name
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name
  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")
# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  # Overridden sound method for Dog
  def sound(self):
    print("Woof!")
# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  # Overridden sound method for Cat
  def sound(self):
    print("Meow!")
# Creating instances
my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)
animals = [my_dog, my_cat]
for animal in animals:
  animal.sound()


  # Course 12c - Data Hiding
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    self.odometer = odometer
  def describe_car(self):
    print(self.year, self.model)
  def read_odometer(self):
    print("Odometer:", self.odometer, "miles")
my_car = Car('Audi', 2020, 15000)
my_car.describe_car()
my_car.read_odometer()
#changing a value of the attribute
my_car.odometer = 20000
my_car.read_odometer()
  
  
# single underscore '_' meant for internal use and should be viewed as protected
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'protected'
    self._odometer = odometer  
  def describe_car(self):
    print(self.year, self.model)
  def read_odometer(self):
    print("Odometer:", self._odometer, "miles")
my_car = Car('Audi', 2020, 15000)
my_car.describe_car()
my_car.read_odometer()
my_car.odometer = 20000
my_car.read_odometer() # odometer already protected
  
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'protected'
    self._odometer = odometer  
  def describe_car(self):
    print(self.year, self.model)
  def read_odometer(self):
    print("Odometer:", self._odometer, "miles")
my_car = Car('Audi', 2020, 15000)
#accessing the protected attribute
print(my_car._odometer)
  
  
# double underscore '__' making an attribute private 
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  
  def describe_car(self):
    print(self.year, self.model)
  def read_odometer(self):
    print("Odometer:", self.__odometer, "miles")
my_car = Car('Audi', 2020, 15000)
#accessing the attribute within method
my_car.read_odometer()
#error
# print(my_car.__odometer) 
  
# name mangling for accessing private attributes
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  
  def describe_car(self):
    print(self.year, self.model)
  def read_odometer(self):
    print("Odometer:", self.__odometer, "miles")
my_car = Car('Audi', 2020, 15000)
#accesing using name mangling
print(my_car._Car__odometer)
  
  
# redesignate methods as protected or private
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  
  def _describe_car(self):  # Making the describe_car method 'protected'
    print(self.year, self.model)
  def __read_odometer(self):  # Making the read_odometer method 'private'
    print("Odometer:", self.__odometer, "miles")
my_car = Car('Audi', 2020, 15000)
#accessing protected method
my_car._describe_car()
#error when accessing a privet method
#my_car.__read_odometer()

  
  # Course 12d - Class and Static method
# Class methods 
# @classmethod -> def <function> (<cls>, )
# you don't need to create an instance to call a class method
# just call the class name, followed by a dot and the class method name
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)
  #class method
  @classmethod
  def books_in_series(cls, series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')
# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
# Using the instance method to describe the book
my_book.describe_book()
# Using the class method to display information about the series
Book.books_in_series("Harry Potter", 7)


# Static methods 
# @staticmethod - they don't recieve any additional argument 
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)
  #staticmethod
  @staticmethod
  def books_in_series(series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')
# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
# Using the instance method to describe the book
my_book.describe_book()
# calling the static method
Book.books_in_series("Harry Potter", 7)



# Exercise
# 1 - Library Management System ❌ 8/10
class Book:
    def __init__(self,title):
        self.__title = title
    def get_title(self):
        print(self.__title)
class LibraryBook(Book):
    def __init__(self,title,status):
        super().__init__(title)
        self.status = status
    def display_info(self,title, status):
        print('Title: ', title, 'status: ', status)
my_library=LibraryBook('Trading Psychology','Available')
my_library.display_info()


# 2 - The "Grand Quant" Exercise: ❌7/10 The Portfolio Engine
class QuantPosition:
    def __init__(self,entry_price,lot_size):
        self.__entry_price = entry_price
        self.lot_size = lot_size
    @staticmethod
    def market_status():
        return "Market is Open"
    @classmethod
    def forex_pair(cls, pair_name):
        print(f"Monitoring {pair_name}")
    def calc_notional(current_price):
        notional = (current price - entry_price)


# Correction
#1 
class Book:
    def __init__(self, title):
        self.__title = title
    def get_title(self):
        return self.__title # Return it so other methods can use it
class LibraryBook(Book):
    def __init__(self, title, status):
        super().__init__(title)
        self.status = status
    def display_info(self): # No need to pass title/status here
        # Use get_title() because __title is private
        print(f"Title: {self.get_title()}, Status: {self.status}")
my_library = LibraryBook('Trading Psychology', 'Available')
my_library.display_info()

#2 
class QuantPosition:
    def __init__(self, entry_price, lot_size):
        self.__entry_price = entry_price
        self.lot_size = lot_size
    @staticmethod
    def market_status():
        return "Market is Open"
    @classmethod
    def forex_pair(cls, pair_name):
        print(f"Monitoring {pair_name}")
    def calc_notional(self, current_price): # Added 'self'
        # Accessing the private entry price and public lot size
        notional = (current_price - self.__entry_price) * self.lot_size * 100000
        return notional
# Testing your Quant Engine
trade = QuantPosition(1.2500, 0.1) # Entry at 1.2500, 0.1 lots
print(trade.market_status())
trade.forex_pair("GBP/USD")
print(f"Notional Profit/Loss: ${trade.calc_notional(1.2550)}") # Price moved up 50 pips






















