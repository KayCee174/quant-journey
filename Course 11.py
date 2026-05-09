# Course 11 - Functional Programming
# by KayCee - April 18th, 2026

  # Course 11a - Introduction to Functional Programming
# Functions can take other functions as arguments. 
def welcome(name):
  return "Welcome, " + name
def process_user(name, func):
    return func(name)
print(process_user("Alice", welcome))


# Higher-Order Function - taking another function as an argument or return a function
def welcome(name):
  return "Welcome, " + name
def bye(name):
  return "Goodbye, " + name
def process_user(name, func):
  return func(name)
print(process_user("Alice", welcome))
print(process_user("Bob", bye))

def book_title(title):
  return "Book title: " + title
def info(title, func):
  return func(title)
print(info("The Great Gatsby", book_title))

# Pure Functions - gives the same result everytime you give it the same input
def total(price, count):
  return price * count
print(total(10, 5))
  
# Impure Functions - it depends on any external state that it modifies or that affects its output
products = ['pen', 'scissors', 'paper']
def add_item(products, item):
  products.append(item)
print(add_item(products, 'chalk'))


  # Course 11b - Lambda Expressions
# Lambda - quick to create and use - 1 line for small, simple task 
greet = lambda name: "Welcome, " + name
print(greet("Bob"))

# variable = lambda <argument> : <expression>
# you can assign lambda expression to a variable
discount = lambda price: price * 0.9 
print(discount(100))

# lambda can take multiple argument
area = lambda length, width : length * width
print(area(10,5))

# argument to lambda on-the-fly by adding them in parentheses
res = (lambda x, y: x + y) (2, 3)
print(res)

# lambda as an anonymous function inside another function
def mult(n):
  return lambda a : a * n
doubler = mult(2)
tripler = mult(3)

print(doubler(5))
print(tripler(5))



  # Course 10c - Map and Filter
# map() - applies a specific function to every element like lists or tuples
#List of names in various cases
names = ["alice", "bob", "CHARLIE", "dEborah"]
# Function to capitalize each name
def capitalize(name):
  return name.capitalize()
# Using map() to apply the capitalization to each name
capitalized = map(capitalize, names)
# Converting map object to a list
capitalized = list(capitalized)
print(capitalized)

prices = [25.99, 14.50, 8.75, 19.95]
def discount(price):
  discounted_price = price * 0.9
  return discounted_price
discounted_prices = list(map(discount, prices))
print(discounted_prices)

# map(<function>,<iterable>) like apply the function in the list
exam_scores = [85, 62, 95, 40, 78]
def is_passing(score):
  return score >= 70
status = list(map(is_passing,exam_scores))
print(status) 
# using filter() 
exam_scores = [85, 62, 95, 40, 78]
status = list(filter(lambda x: x>= 70, exam_scores))
print(status) 

numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

# filter() - apply a condition specified in a function to each item n return only those for which the function evaluates to True
products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]
# Filters products with name length equal to 4
filtered_prod = list(filter(lambda name: len(name) == 4, products))
print(filtered_prod)

# map transforms values, filter selects values
# map changes items, filter keeps matching items
# map applies a function, filter applies a condition
# map returns new values, filter returns matching originals

# map() transforms the item of an iterable, filter() returns items that meet a condition

# they can work with any iterable
products = {'Table': 110, 'Sofa': 120, 'Chair': 45, 'Lamp': 70}
#filtering products with prices less than 90
filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))
print(filtered_products)



  # Course 10d - args and kwargs
# using a list as an argument
def total(numbers):
  result = 0
  #iterating over the list
  for i in numbers:
    result+=i
  return result
nums = [1,2,3,4,5]
print(total(nums))

# *args - provides any number of arguments without the need to create a list befoe calling the function each time
def total(*args):
  result = 0
  for arg in args:
    result += arg
  return result
print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))

# def <func> (<argument>, <*args>) - function signature
def show_items(category, *items):
  print("Category: " + category)
  for item in items:
    print(item)
show_items("Electronics", "Laptop", "Smartphone", "Tablet")

# **kwargs - receives in form of a dict, consisting of key:value pairs
#**kwargs is a dictionary
def display_info(**kwargs):
  #kwargs.items() returns the key:valie pairs
  for key, value in kwargs.items():
    print(key, ":", value)
display_info(name="Alice", age=30, city="New York")

# *args - tuple, while **kwargs - dictionaries 
# def <func> (<argument>,<*args>,<**kwargs>)


  # Course 11e - Decorators
# functions can be nested
#outer function
def outer_function():
    print("Hello from the outer function")
    #inner function
    def inner_function():
        print("Hello from the inner function")
    inner_function()
outer_function()

# you can return the result of the nested function
def greet(name):
    print("Hey", name)
    def account():
        return "Your account is created!"
    message = account()
    return message
print(greet("Bob"))

# wrapper() - runs the original function, adds something before/after it
def greet():
    return "Welcome!"
#takes a function as an argument
def uppercase(func):
    #wrapper function to keep the
    #original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper
greet_upper = uppercase(greet)
print(greet_upper())

# apply a decorator to a functiong using the @ sign
def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper
@uppercase
def greet():
    return "Welcome!"
# Using the decorated function
print(greet())

# You can apply the same decorator to several different function
def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(result, ": stock status for", item)
        return result
    return wrapper
@stock_status_decorator
def restock_item(item):
    return "Restocked"
@stock_status_decorator
def sell_item(item):
    return "Sold"

print(restock_item("Laptop"))
print(sell_item("Smartphone"))

print('\n')



# Exercise
#1 - Survey Data ✅ 10/10
ages = [14, 18, 21, 16, 30, 24, 12, 17, 20]
Adult = list(filter(lambda age: age >= 18, ages))
print(Adult)

#2 - The "Grand Quant" ❌6/10: The Multi-Currency Fee Calculator
def trade_logger(func):
    def wrapper():
        return "Calculating trade costs..."
    return wrapper
@trade_logger 
def apply_commission(*args):    
    x=list(map(lambda trade: trade + 5, args))
    return "Calculation complete"
#print(trade_logger(apply_commission(100,250,400,150)))
    

# Correction for #2 - Grand Quant
def trade_logger(func):
    # The wrapper must accept the same args as the function
    def wrapper(*args):
        print("Calculating trade costs...")
        result = func(*args) # Actually RUN the function here!
        print("Calculation Complete")
        return result
    return wrapper
@trade_logger 
def apply_commission(*args):    
    # Using map and lambda to add $5
    return list(map(lambda trade: trade + 5, args))
# Now you just call the function normally
print(apply_commission(100, 250, 400, 150))

















