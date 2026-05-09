# Course 6 - Mixing things up: loops and lists

  # Course 6a - Iterating over Lists
products = ['milk', 'eggs', 'apples']
print('bananas' in products)
print('milk' in products)

products = ['milk', 'eggs', 'apples']
for i in products:
  print(i)
  
new_users = ['Tom', 'Mery', 'Anna']
for zabada in new_users:
  print("Welcome, " + zabada)

prices = [2, 4, 8]
for price in prices:
    print (price + 2)
    
x = 15
x += 5
print(x)


 # Course 6b - Nested Loop
ranks = ["Ace", "King", "Queen"]
suits = ["Hearts", "Clubs", "Diamonds"]
for rank in ranks:
  for suit in suits:
    print(rank, suit)
    
vehicles = ['car', 'bike']
colors = ['red', 'blue']
for vehicle in vehicles:
  for color in colors:
    print(color, vehicle)
    
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
tasks = ['Gym', 'Homework', 'Pool']
for day in days:
  print(day + ':') 
  for task in tasks:
    print(task)
  print("\n")
  
meals = ["Breakfast", "Lunch", "Dinner"]
options = ["Salad", "Sandwich", "Pasta"]
for meal in meals:
  for option in options:
    print(meal + ' : ' + option)
  print("\n")
  
moves = ["Step Turn", "Jazz Hands", "Shuffle"]
for move in moves:
  for i in range(3):
    print(move)
    
    
  # Course 6c - Iterations and Selections
# Recap
age = 16
if age >= 18:
  print("Regular price")
else:
  print("Discount")
  
# Combining 'if' statement with list iteration
scores = [45, 67, 89, 34, 56, 77, 49, 91, 52]
for score in scores:
  if score >= 70:
    print(score) 

# To count occurrences of an item in a list
counter = 0
devices = ['PC', 'TV', 'PS', 'TV', 'PS', 'Xbox', 'TV']
for device in devices:
  if device == 'TV':
    counter = counter +1
print("Number of TVs:", counter)

# 'for' loop to iterate over strings
message = "You have a new message"
count = 0
for i in message:
  if i == 'a':
    count += 1
print(count)

scores = [7, 5, 8, 10, 8]
total = 0
for any_number in scores:
  total += any_number
print("Total:", total)


 # Course 6d - break and continue
# break statement - used to stop the loop when some condition is met
songs = ["Hello", "Yesterday", "Happy", "Hallelujah"]
for song in songs:
  print("Searching")
  if song == "Happy":
    print("Playing " + song)
    break

prices = [35, 80, 16, 100, 95, 76]
for price in prices:
  if price > 90:
    break
  print(price)

# You can set any condition to exit the loop
prices = [10, 54, 9, 44, 6, 26, 15]
total = 0
for price in prices:
  total+=price
  print(total)
  if total > 100:
    print("Limit exceeded")
    break

# The 'break' statement can be used with 'while' loop as well
x = 1
while x < 10:
  print(x)
  if x==5:
    print("Stop")
    break
  x+=1

while True:
  text = input()
  print(text)
  if text == 'Stop':
    break
    
while True:
  print("text")
  break 
  
# continue statement - allows you to skip the current iteration of a loop when a certain condition is true. 
ages = [13,19, 22, 8, 75, 34, 26, 41]
for age in ages:
  if age < 18:
    continue
  print(age)
  
animals = ["cat", "giraffe", "lion", "leopard", "mouse"]
for animal in animals:
  if animal[0] == "l":
    continue
  print(animal)
  
# You can use 'continue' statement with 'while' loops 
day_number = 1
while day_number <= 7:
  if day_number == 4:
    day_number += 1
    continue
  print(day_number, "Turn on the lights!")
  day_number += 1
  
  
# Exercise Attempt by KayCee - April 15th, 2025
# Class Grade Analyzer
exam_scores = [5,7,9,40,50,70,90,147]
for score in exam_scores:
    if score < 10:
        continue
    if score >= 100:
        break
    print("automatic pass")
    
# Grand Quant Exercise
# Market Data: [Pair Name, Current Price, Threshold]
market_data = [
    ["EURUSD", 1.0850, 1.0800],
    ["GBPUSD", 1.2650, 1.2700],
    ["USDJPY", 150.10, 149.50]
]
#1 iterate
for data in market_data:
    for data[0] in data:
     print(data[0])
#2 Unpack
names=["EURUSD","GBPUSD","USDJPY"]
prices=[1.0850,1.2650,150.10]
limits=[1.0800, 1.2700, 149.50]  
#3 Selection 
for name in names:
 #for price in prices:
   #for limit in limits:
     if prices > limits:
       print(f"{name} is Bullish. Executing Trade")
     else:
       print(f"{name} is Bearish. Skipping")
#4 Advanced (The Break)
     if name== "USDJPY":
       print("Found USDJPY, stopping scan.")
       break
      
# Corrections on Exercises
# The Class Grade Analyzer
exam_scores = [5, 7, 9, 40, 50, 70, 90, 147]
valid_scores = []
for score in exam_scores:
    if score < 10:
        continue # Skips 5, 7, 9
    if score >= 100:
        break    # Stops completely at 147
    valid_scores.append(score)
average = sum(valid_scores) / len(valid_scores)
print(f"Average of valid scores: {average}")

#Grand Quant
market_data = [
    ["EURUSD", 1.0850, 1.0800],
    ["GBPUSD", 1.2650, 1.2700],
    ["USDJPY", 150.10, 149.50]
]

for name, price, limit in market_data:
    if name == "USDJPY":
        print("Found USDJPY, stopping scan.")
        break
    if price > limit:
        print(f"{name} is Bullish. Executing Trade.")
    else:
        print(f"{name} is Bearish. Skipping.")










