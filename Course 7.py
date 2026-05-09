# Course 7 - Functions - by KayCee April 15, 2026 
 # Course 7a - Functions
# function(argument) we pass information into functions as arguments
# A function can take multiple arguments
print("Your seat:", 4)

 
 # Course 7b - Function Arguments
# print() function accept argument of any data type
print("Online:", True) # string and boolean
print("Credit:", 385.91) # string and float
print(2, "bananas") # integer and string

# functions can take operations as arguments
print(55 * 3) #math
print(5 > 7) #comparison
print(True and False) #logical
print("motor" + "bike") #concatenation

# a function can be an argument for another function
print(type("word"))
#type("word") is an argument of print()

print(int(5.5)) # 5
print(int('5')) # 5
print(str(5)) # 5
# print(int('pencil')) you can't convert a str to int

num = '45' # string
print(int(num) + 3)


 # Course 7c - String Functions
# upper() and lower() can only be used on str and in this format string.function()
print('SmArTpHoNe'.lower())
print('SmArTpHoNe'.upper()) 

# capitalize() - first character of a string to upper case
print("happy birthday".upper())
print("happy birthday".lower())
print("happy birthday".capitalize()) 

# Remember Strings are immutable and functions won't change them
item = "smartwatch"
print(item.upper())
print(item) #original string
item2 = item.upper()
print(item2)

# find() - checks if a character is present in a string and returns the index position 
print("Bee".find("e")) 

print('roBot'.upper())
print('roBot'.lower())
print('roBot'.capitalize())
print('roBot'.find("b")) # if character is not in the string, it returns as -1
 

 # Course 7d - List Functions 
# lens() - means length and when used on list, it returns the numbers of items in the list
movies = ["Avatar", "Titanic", "Avengers"]
print(len(movies))

# append() adds a new item to the end of a list
songs = ["Yesterday", "Hello", "Believer"]
songs.append("Imagine")
print(songs)
for song in songs: # my extra haha
    print(song)
    
movies = ["Avatar", "Titanic", "Avengers"]
movies.append("Alien")
print(movies[3])

# insert () allows you to add an element to a list at a specific postion
items = ["book", "pen", "pencil"]
items.insert(2,"marker")
print(items)
print(items[2])

colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])
    
# pop() removes an element from a list
items = ["book", "pen", "pencil"]
items.pop(1)
print(items)
print(items[1])
    
    
 # Course 7e - Custom Functions
#function definition
def greet():
  print("Hello from a function")
  print("Have a great day")
  print(147)
#function call
greet()

#function definition
def personal_greet(name): 
  print("Hello", name)
  print("Have a great day")
#function calls
personal_greet("Bright") 
personal_greet('KayCee')

def double(number):
 print(number*2)
double(6)

def bmi(weight, height):
    index = weight / (height * height)
    print(index)
bmi(8,2)

#Defining function
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back
#Calling function and using return value
patient_5 = bmi(61, 1.83) #stores return value
print("underweight:", patient_5 < 18.5)
#Another call
patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)


 # Course 7f - More on Custom Functions
# A function can return multiple values
def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter #2 values
x, y = rect(50, 100) #2 variables
print(x, y)

def rect(d1, d2):
  area = d1 * d2
  perimeter = 2 * d1 + 2 * d2
  return area, perimeter
x, y = rect(5,10)
print("Area:", x)
print("Perimeter:", y)

def profitable(d1, d2):
  area = d1 * d2
  invest = area > 700
  return invest
buy = profitable(90, 120)
print(buy)

def rect(d1, d2):
  area = 0
  return area
  #End of function execution
  area = d1 * d2 #Not executed
x = rect(50, 50)
print(x)

# if a function is called withou the argument, it gets its default value
def greet(name="Guest"):
  print("Welcome", name)
greet() # Welcome Guest
greet("John") # Welcome John


# Exercise 
#1 Survey Data & Hashtag Generator
def clean_tag(text="  #GoldTrade  "):
  print(text.lower())
clean_tag()

#2 Queue Management
queue =[150,155,160,165,170]
def update_queue(current_queue,new_tick):
    current_queue=queue.pop(0)
    new_tick=queue.append(175)
print(queue)
update_queue(150,170)


#3 Shipping Cost
def calc_fee(volume):
#   fee = amount * volume
   if volume > 1000:
     fee = 0.005 * volume
   else:
     fee = 0.01 * volume 
   return fee
calc_fee(500)
calc_fee(1900)

#The Grand Quant Exercise
def manage_position(price_history, entry_price, direction):
    latest_price = price_history[-1]
    price_difference = latest_price - entry_price
    if price_difference > 0.02 * entry_price:
        print("Take Profit")
    elif price_difference < 0.01 * entry_price:
        print("Stop Loss")
    else:
        print("Hold")
#price_history=[2000, 2010, 2050]
#entry_price=2000
#direction="BUY"
manage_position([2000, 2010, 2050], 2000, "BUY")
    
# Exercise Correction
#1
def clean_tag(text): # Remove the specific text from here
    return text.strip().lower() # .strip() removes the extra spaces
# Now you can use it for ANY tag
print(clean_tag("  #GoldTrade  "))
print(clean_tag("  #FOREX  "))


#2
queue = [150, 155, 160, 165, 170]

def update_queue(current_queue, new_tick):
    current_queue.pop(0)    # Remove the first
    current_queue.append(new_tick) # Add the variable passed in
update_queue(queue, 175) # Pass the actual list and the new number
print(queue)


#3
def calc_fee(volume):
    if volume > 1000:
        return 0.005 * volume # Use RETURN, not just a variable
    else:
        return 0.01 * volume
# Now you can store the result in a variable
my_fee = calc_fee(1900)
print(f"Fee is: {my_fee}")


#4 - Grand Quant
def manage_position(price_history, entry_price, direction):
    latest_price = price_history[-1] # Use square brackets []
    # Calculate percentage change
    change = (latest_price - entry_price) / entry_price
    if direction == "BUY":
        if change >= 0.02: return "Take Profit"
        elif change <= -0.01: return "Stop Loss"
        else: return "Hold"
print(manage_position([2000, 2010, 2050], 2000, "BUY"))



    

    


    
    
    
    
    
    
    
    
    
    
    
    
    