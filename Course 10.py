# Course 10 - Error Handling
# by KayCee - April 18th, 2026

  # Course 10a - Exceptions
# bugs are flaws or mistakes in a program's code, leading to incorrect or unintended behaviour
# bugs don't necessarily stop program's executions
name = "Mery"
surname = "Osborn"
print(name + surname)

# exceptions - specific errors that occurs during a program's execution
# exceptions stop program's execution at the line of the error
name = "Bob"
# name[0] = "R" strings are immutable
print(name) 

# NameError Exception - when a variable is not defined
# NameError - Variable is not defined
name = "Anna"
# print(names) names variable not defined

# SyntaxError Exception - missing punctuation
# SyntaxError - Incorrect Syntax
score = 85
#if score >= 80 ':' is misisng 
  #print("Passed")

# IndexError Exception - an attempt to access an element of a list and tuples using an index outside its valid range
# IndexError - Out-of-range Index
cars = ["BMW","Benz","Audi"]
# print(cars[3]) list index out of range

# TypeError Exceptions - a function called for an inappropriate type
message = 6
# length = len(message) int has no len

# ValueError Exceptions - a function receives a value of the correct type, but the value itself is inappropriate or unacceptable
# ValueError - Inappopriate Value


  # Course 10b - Exception Handling
# try/except statement - prevent program failure
# try block - holds code that might cause an exception
# except block - allow the program to continue running 
prices = [250, 300, "240", 400]
try:
  #block that may cause an exception
  total = sum(prices)
  print(total)
except TypeError:
  # to perform if there is an exception
  print("Invalid data type")
print("Happy Shopping")


colors = ['Red', 'Yellow', 'Green']
try:
  #index error
  print(colors[10])
  #wrong exception
except IndexError:
  print("Error")
#will not be executed
print("Happy Shopping")

# multiple except
colors = ['Red', 'Yellow', 'Green']
try:
  print(colors[10])
except IndexError:
  print("Out of range")
except NameError:
  print("Variable is not defined")
print("Happy shopping")

# handles all exceptions
colors = ["Red", "Yellow", "Green"]
try:
  print(colors[10])
except:
  print("Error")


price = input()
try:
  price_value = int(price)
except ValueError:
  print("Please enter a number")


 # Course 10c - More on Exception Handling
# finally statement - to perform an operation after the try/except block, no matter if an exception occured or not
prices = [559, 879, "N/A", 349]
try:
  print(sum(prices))
except TypeError:
  print("Check the prices")
finally:
  print("Need help? Contact us")
 
# else statement - in conjunction with the try/except and will execute only when no error occured in the try block
books = ['Harry Potter', 'Dune', 'Emma']
try:
  choice = books[1]
except IndexError:
  print("Out of range")
else:
  print(choice + " is a great choice!")

# raise statement - immediately stop the program's execution and indicate an error has error has occured
#print("Rate from 0 to 10")
rating = 15
#if rating > 10 or rating < 0:
  # raise ValueError("Rate from 0 to 10")



# Exercise 
#1 - Vending Machine Selection ✅ 6/10
drinks = ["Coffee", "Tea", "Water", "Juice", "Soda"]

  # task 1
user = input()
  # task 2
try:
    print(drinks[user])
except IndexError:
    print("Invalid Choice")
except TypeError:
    print("Numeric Input Only")
  # task 3 
finally:
    print("Thank you for using the machine")


#2 - The "Grand Quant" Exercise: The Safety-First Backtester ✅8/10
trades = [(100, 200), (150, 0), (200, 600), ("50", 150)]
for (Risk, Potential_Reward) in trades:
 # task 1
  try:
    rr = Potential_Reward / Risk
    if rr == 0:
      print("Skipping: No Reward Potential")
 # task 2 
  except TypeError:       
    print("Skipping: Invalid Data Type")
 # task 3
  finally: 
    if rr >= 3:
      print(rr)





# CORRECTION!
# Exercise 1 
user = input()
try:
    # You MUST convert the input to an integer first
    index = int(user) 
    print(drinks[index])
except ValueError: # Catch if they typed "abc" instead of "123"
    print("Numeric Input Only")
except IndexError: # Catch if they typed "99"
    print("Invalid Choice")
finally:
    print("Thank you for using the machine")

# Exercise 2 
trades = [(100, 200), (150, 0), (200, 600), ("50", 150), (0, 500)] # Added a 0 risk trade

for (Risk, Potential_Reward) in trades:
    try:
        # Move logic inside the try so the 'except' can catch it
        if Potential_Reward == 0:
            print("Skipping: No Reward Potential")
            continue # Move to next trade in the loop
            
        rr = Potential_Reward / Risk
        print(f"RRR: {rr}")

    except ZeroDivisionError: # Specific math error
        print("Skipping: Division by Zero (Risk cannot be 0)")
    except TypeError: # Specific data error
        print("Skipping: Invalid Data Type")


















