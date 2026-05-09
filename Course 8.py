# Course 8 - Mixing things up: Using Funtions
# by KayCee - April 17th, 2026

 # Course 8a - Functions and Lists
 # Custom function that takes a list as an argument
my_menu = ["Pizza", "Burger", "Salad"]
def show_menu(menu):
  print(menu)
show_menu(my_menu)

 # Reusability - Function
new_menu = [] #empty list
#dishes for the new menu
dish1 = "Pasta"
dish2 = "Pizza"
dish3 = "Salad"
#function definition
def add_to_menu(menu, dish):
    menu.append(dish)
#adding dish 1
add_to_menu(new_menu, dish1)
print(new_menu)
#adding dish 2
add_to_menu(new_menu, dish2)
print(new_menu)
#adding dish 3
add_to_menu(new_menu, dish3)
print(new_menu)

 # Taking inputs when calling a function
cart = []
def add_to_cart(cart):
  #taking user input
  product = input()
  cart.append(product)
  product = input()
  cart.append(product)
add_to_cart(cart)
print(cart)


 # Course 8b -  Funtions and Booleans
# Functions with boolean arguments
delivery = True
def to_deliver(delivery):
    if delivery == True:
        print("Enter your address")
to_deliver(delivery)
 
def my_function(score):
  if score >= 70:
    return True
print(my_function(65)) 

 # 'in' operator - allows you to check if an item is in a particular list
books = ['1984', 'War and Peace', 'The Great Gatsby']
book = 'Animal Farm'
def book_in_library(books, book):
  return book in books
print(book_in_library(books, book))


 # Course 8c - Useful Built-im Functions
 # Sum function - adds up all the elements in a list 
prices = [33, 49, 55, 14]
total = sum(prices)
print(total)

 # The combination of sum and len
prices = [33, 49, 55, 14]
#total price
total = sum(prices)
print("Total Price:", total)
#number of products
number_of_products = len(prices)
print("Count:", number_of_products)
#calculating the average
avg_price = total/number_of_products
print("Average Price:", avg_price) 
 
 # The max() and min() function - returns the maximum and minimum value in a list
prices = [33, 49, 55, 14]
min_price = min(prices)
max_price = max(prices)
print(min_price)
print(max_price)

  # sorted() function - takes an iterable as input and returns a list with the item sorted
ages = [25, 36, 33, 19, 56]
sorted_ages = sorted(ages)
print(sorted_ages)

prices = [503.9, 199.9, 254.5, 39.9]
srt_prices = sorted(prices)
print(srt_prices[1])

 # sorted() function handles both numerical and textual values. 
players = ["Zoe", "Liam", "Emma", "Noah", "Olivia"]
#sorting names
srt_players = sorted(players)
print(srt_players)


# ascending or descending order using reverse argument. 
# When reverse = True, the values are sorted in descending order



# Exercise 
#1 - Temperature/price Statistics
def analyze_data(data_list):
    x=max(data_list)
    y=min(data_list)
    z=len(data_list)
    return x, y, z 
x,y,z = analyze_data([100,110,120,130,140,150])
print(x,y,z) # this is correct

#2 - The Grand Quant
def is_breakout(current_price,price_history):
    peak=max(price_history)
    if current_price > peak:
        return True
    else: 
        return False
def scan_market(assets_dict):
    asset={"Gold": 2050, "Silver": 24, "Oil": 85}
    for name, price in asset:
        for i in price:
             if is_breakout == True:        
               print(f"{name} is breaking out")

  # Correction for #2
def is_breakout(current_price, price_history):
    peak = max(price_history)
    return current_price > peak # Pro tip: This automatically returns True/False!
def scan_market(assets_dict):
    # Let's assume the previous 5 days' high was 2000 for all assets
    history = [1900, 1950, 1980, 2000] 
    for name, price in assets_dict.items(): # Added .items()
        if is_breakout(price, history): # Calling the function with data
            print(f"{name} is breaking out at {price}!")

# Test it
my_assets = {"Gold": 2050, "Silver": 24, "Oil": 85}
scan_market(my_assets)

    
    
# Another real world correction
    
def is_breakout(current_price, price_history):
    peak = max(price_history)
    return current_price > peak


def scan_market(assets):
    for name, data in assets.items():
        current_price = data["current"]
        history = data["history"]

        if is_breakout(current_price, history):
            print(f"{name} is breaking out at {current_price}!")
# Test data (each asset has its own history)
assets = {
    "Gold": {"current": 2050, "history": [1900, 1950, 1980, 2000]},
    "Silver": {"current": 24, "history": [20, 21, 22, 23]},
    "Oil": {"current": 85, "history": [80, 82, 83, 84]}
}

scan_market(assets)
    
    
    
    
    
    
    










