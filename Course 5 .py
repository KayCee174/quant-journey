# Course 5 - working with list (april 14th, 2026)

# Course 5a - lists
shopping_cart = [
  'laptop', 
  "smartphone", 
  "headphones", 
  "backpack"
]
print(shopping_cart)

countdown=[3,2,1]
print(countdown)


# Course 5b - indexing
last_calls = ["Mom", "Dave", "Lawyer"]
print(last_calls[0])
print(last_calls[1])

animals=['cat','dog','bird']
print(animals[1])
my_pet=animals[2]
print(my_pet)

  # Lists are mutuable
nums = [8, 6, 19]
nums[0] = 1
nums[1] = 2
nums[2] = 3
print(nums)

words = ['shelf', 'store', 'book']
print(words[2] + words[1])

nums=[1,4,7]
print(nums[2] + nums[0])


# Course 5c - using indexing
  # You can create a list with values that has been stored in variables
name = "Sarah"
age = 34
country = "Germany"
info = [name, age, country]
print(info[0])
print(info[1])
print(info[2])

products=['juice','chocolate','water']
user_choice=2
print((products[user_choice]))

products = ["juice", "chocolate", "water"]
choice = int(input())
print(products[choice])

  # Use indexing to access individual characters in a string
animal = "Dog"
print(animal[0])
print(animal[1])
print(animal[2]) 
  # Strings are immutable
word = "car"
# word[2] = "t"
# print(word) ≠ cat … you can't change the characters in a string 
print(word[2])
  # Lists are mutable
words = ["car", "dog", "bird"]
words[0] = "cat"
print(words)

x = "arctic"
print(x[2] + x[0] + x[3])


# Course 5d - Slicing
animals =["cat", "dog", "bird", "cow"]
print(animals[1:3])
  # slicing also works with strings
vehicle = "airplane"
print(vehicle[0:3])
  # slicing a list produces another list
colors = ['red', 'green', 'blue', 'yellow']
print(colors[2:3])


# Course 5e - Using Slicing
  # You can omit the starting index
cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[:3])
  # Eg2.,
vehicle = 'motorbike'
print(vehicle[:5])
  # You can omit the stopping index
cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[1:])
  # Eg2.,
vehichle = 'motorbike'
print(vehicle[5:])
  # You can omit the starting and stopping index
vehicle = 'motorbike'
print(vehicle[:])
  #Eg2., 
platform = ['iOS', 'Android', 'Web']
print(platform[:])


# Course 5f - Advanced Slicing and Indexing
  # Negative indexing - indexing from the end
animals = ["cat", "dog", "bird", "cow"]
print(animals[-1]) # Last element
print(animals[-2]) # Second last element
print(animals[-3:]) # Last 3 elements
print(animals[-3:-1])
  #Eg2.,
vehicle = 'motorbike'
print(vehicle[-1])
print(vehicle[:-4])
print(vehicle[-4:])
  # You can combine Positive and Negative Indexing when Slicing
c = ['$', '£', '€', '¥']
print(c[1:-1])
  # Remember, Lists are mutuable
c = ['$', '£', '€', '¥']
c[1] = '₣'
print(c)
  # Eg2.,
c = ['$', '£', '€', '¥']
c[:2] = ['₣', '฿']
print(c)
  # Remember, strings are immutable
vehicle = 'airplane'
#vehicle[:3] = 'water' 
#print(vehicle) ≠ waterplan
print('Course Done. Exercise Next')


# Exercises
  # Exercise 1 - Game Machine
games=['Chess', 'Poker', 'Ludo', 'Monopoly']
print(games[3])

  # Exercise 2 - Relay Race
Podium = [1,2,3,4,5,6,7,8,9,10]
print(Podium[:3])

  # Exercise 3 - Step Counter
hourly_step=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
print(hourly_step[::3])

  # Exercise 4 - The Grand Quant
prices = [2050.10, 2045.30, 2060.00, 2055.20, 2070.50, 2075.00, 2080.10] # last 7 days of closing prices for Gold (XAUUSD).
#1 Index: Print the latest price
print(prices[-1])
#2 Slicing: Create a new list called recent_trend that contains only the last 3 days of prices.
recent_trend=prices[-3:]
print(recent_trend)
#3 Logic + Indexing: 
opening_price = prices[0]
latest_price = prices[-1]
if latest_price > opening_price:
    print('Weekly Trend: Bullish')
#4 Loop - correction 
for prices in recent_trend:
    print(f"${prices}") 


