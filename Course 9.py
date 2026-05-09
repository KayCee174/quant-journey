# Course 9 - Collection Types
# by KayCee - April 17th, 2026

  # Course 9a - Tuples
# Lists are mutuable
colors = ["Yellow", "Red", "Blue"]
print("Original list:")
print(colors)
#making changes
colors[1] = "Orange"
colors.append("Black")
print("Changed list:")
print(colors)

# Tuples are immutuable
eiffel_tower = (48.8584, 2.2945)
# eiffel_tower[0] = 56.7581 

  
  # Course 9b - Working with Tuples
# Tuples can contain duplicate items
# count() function - to calculate the number of occurrences of an item in a tuple
scores = (7, 9, 9, 8, 9)
print("# of 7:",scores.count(7))
print("# of 9:",scores.count(9))
print("# of 2:",scores.count(2))

# len() and max() and min() can be used., any function can be used as far as it doesn't try to modify the items in the tuple

# You can use tuples in a control flow structure - 'if else' and loops
points = (12, 14, 9, 10, 9)
for point in points:
  if point > 10:
    print(point, ": passed")

# Tuple unpacking - values assigned in the order they appear
birthday_date = (12, "August", 1993)
day, month, year = birthday_date
print(day)
print(month)
print(year)

# the * operator - used to gather multiple elements from a tuple to a list
scores = (98, 96, 91, 88, 64)
winner, *rest = scores
print(winner)
print(rest)


  # Course 9c - Sets
# set{} - unique and unordered and don't support indexing and slicing
guests = {"Mery", "Anna", "Jonathan"}
print(guests)
# print(guests[0])

dishes = ["Salad", "BBQ", "Spaghetti"]
guests = {"Mery", "Anna", "Jonathan"}
print(dishes[0])
# print(guests[0])

# set{} can't have duplicates
friends = {'Anna', 'Mery', 'Mery', 'Jonathan'}
print(friends)

# set{} are mutuable - you can use add() and remove()
guests = {'Anna', 'Mery', 'Jonathan'}
#adding 'Robert'
guests.add('Robert')
#removing 'Mery'
guests.remove('Mery')
print(guests)

# clear() function doesn't support an argument and remove all the items
students = {'Amanda', 'Robert', 'Alice'}
students.clear()
students.add('John')
print(students)

# union() - returns a new set with all the elements from both sides, omitting duplicates
set1 = {'apple', 'banana'}
set2 = {'banana', 'cherry'}
combined_set = set1.union(set2)
print(combined_set)

# difference() - returns a set containing elements that are only in the first and not in the second set
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
unique = set1.difference(set2)
print(unique)


  # Course 9d - Dictionaries 
# Dictionaries store data as key–value pairs, where each value is identified by a unique key.
# Dictionaries also use {} - key:value pairs seperated by ,
product = {
  "name": "pen",
  "color": "red",
  "price": 79
}
print(product)


# can have duplicate values but not duplicate keys
car = {
  "brand": "Audi",
  "model": "Q5",
  "model": "A5"
}
print(car)

# values can be accessed using indexes
car = {
  "brand": "Audi",
  "model": "Q5",
  "year": "2008"
}
print(car["brand"])
print(car["model"])
print(car["year"])

# .get() function

# .keys() and .values()
contact = {
  "name": "John",
  "company": "Google",
}
info_keys = contact.keys()
info_values = contact.values()

# .items() returns all the key:value pairs
car = {
  "brand": "Audi",
  "model": "Q5"
}
info = car.items()
print(info)
print(info_keys)
print(info_values)


  # Course 9e - Working with Dictionaries
# you can use keys to change values in a dict. 
user = {
  "Name": "Albert",
  "Age": 29
}
user["Age"] = 30
print(user["Age"])
print(user.items())

# .update() - updates the dict. with the items from the given argument
user = {
  "Name": "Albert",
  "Age": 29
}
# argument: dictionary {"Age": 30}
user.update({"Age": 30})
print(user["Age"])
print(user.items()) 

# .update() can accept dict. with multiple items
user = {
  "Name": "Albert",
  "Age": 29
}
# "Surname": "Johnson" will be added
user.update({"Age": 30, "Surname": "Johnson"})
print(user.items())

# .pop() - removes item with the specified key name
car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}
#removing the item with the "Color" key
car.pop("Color")
print(car)

# in operator - check if a key or a value occurs in a dict. 
car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}
print("Brand" in car)
print("red" in car.values())

# you can iterate with loop functions
car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}
for i in car:
  print(i)
for i in car.values():
  print(i)


  # Course 9f - List Comprehensions
nums = []
for x in range(1,51):
  nums.append(x)
print(nums)

# <variable> = [<expression> for <item> in <iterable>] 
# <variable>: the variable that will store the newly created list 
# <expression>: an expression performed on each item. If no specific action is needed, the item itself is used 
# <item>: the current item being processed 
# <iterable>: any iterable object, such as ranges, lists, strings, tuples, and sets 
nums = [x for x in range(1,51)]
print(nums)

nums = [x*2 for x in range(10)]
print(nums)

tags = ["travel", "vacation", "journey"]
hashtags = ["#" + x for x in tags]
print(hashtags)

users = ["Brandon", "Emma", "Brian", 
"Sophia", "Bella", "Ethan",
"Ava", "Benjamin", "Mia", "Chloe"]
group = [x for x in users if x[0] == "B"]
print(group)


# Bonus Exercise
#1 - Filtering Lonsg Words
headline = "Federal Reserve Maintains Interest Rates Amidst Inflationary Pressures"

# Your Task: 
# a. Split the string into words.
# b. Use a List Comprehension to filter for length > 5.
# c. Ensure the output words are all lowercase.

filtered_words=[x.lower() for x in headline.split() if len(x) > 5]
print(filtered_words)

# 2 - The Grand Quant Exercise
portfolio = {"BTC": 0.5, "ETH": 10, "SOL": 100}
prices = {"BTC": 65000, "ETH": 3500, "SOL": 140, "DOT": 7}

# a. Calculate values of current holdings
values = [portfolio[asset] * prices[asset] for asset in portfolio]

# b. Find "Watchlist" items (Price exists but not in portfolio)
watchlist = set(prices.keys()) - set(portfolio.keys())

print(f"Total Value: {sum(values)}")
print(f"Watch these: {watchlist}")



# Main Exercise
# 1 The "Volatility Filter" (List Comprehension) ✅10/10
daily_returns = [0.002, -0.015, 0.031, -0.001, 0.008, -0.022, 0.011, 0.0005]
significant_moves = [returns for returns in daily_returns if abs(returns) > 0.01]
print(significant_moves)


# 2 - The "Trade Journal" (Dictionaries & Logic) ✅ 6/10 - see correction below
trade_log = {
    "trade_1": {"pair": "EURUSD", "type": "Buy", "pips": 45},
    "trade_2": {"pair": "GBPUSD", "type": "Sell", "pips": -20},
    "trade_3": {"pair": "USDJPY", "type": "Buy", "pips": 15},
    "trade_4": {"pair": "EURUSD", "type": "Sell", "pips": 60}
}
  # task 1 ✅
yoo=trade_log["trade_2"]
print(yoo["pips"])

  # task 2 ✅
trade_log.update({"trade_5" : {"pair": "AUDUSD", "type": "Buy", "pips": 10}})
print(trade_log)

  # task 3 ❌
check=[log for log in trade_log.keys() if log == "GOLD"]
print(check)


# 3 - The "Asset Auditor" (Sets) ✅ 10/10
watchlist = {"EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "GOLD", "BTC"}
active_trades = {"EURUSD", "USDJPY", "ETH"}
  # task 1
print(watchlist.difference(active_trades))
  # task 2 
print(active_trades.difference(watchlist))
  # task 3
print(watchlist.union(active_trades))



# Correction for 2 - The "Trade Journal"
# The "Trade Journal" - Professional Correction

trade_log = {
    "trade_1": {"pair": "EURUSD", "type": "Buy", "pips": 45},
    "trade_2": {"pair": "GBPUSD", "type": "Sell", "pips": -20},
    "trade_3": {"pair": "USDJPY", "type": "Buy", "pips": 15},
    "trade_4": {"pair": "EURUSD", "type": "Sell", "pips": 60}
}

# Task 1: Accessing nested data (Chained Key access)
# This is faster and cleaner than saving the inner dict first.
pips_trade_2 = trade_log["trade_2"]["pips"]
print(f"Pips for Trade 2: {pips_trade_2}")


# Task 2: Adding a new entry (Direct Assignment)
# .update() is great for merging two dicts, but direct assignment is better for a single item.
trade_log["trade_5"] = {"pair": "AUDUSD", "type": "Buy", "pips": 10}


# Task 3: Membership Testing (The 'in' keyword)
# You don't need a loop or list comprehension to check for a key.
# This check is O(1) time complexity (instant), which is why we use dictionaries!
is_gold_present = "GOLD" in trade_log

print(f"Is GOLD in the log? {is_gold_present}")




