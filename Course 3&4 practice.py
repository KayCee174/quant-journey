#Course 3 & 4 - python developer(Sololearn)
distance = 14
units = "km" 
print(True and True)
print (True and False)
print (False and True)
print (False and False)
print(True or True)
print (True or False)
print (False or True)
print (type(False or False))

heart_rate = 100
peak_rate = heart_rate > 120
print(peak_rate)

print(" ")

light_on= True
door_close= False
print(light_on or door_close)
print(' ')

#exercise to do
equity = 1000
margin_used = 200
can_trade = (equity > 500 and margin_used < 300)
print (can_trade)

#Define the number of iterations
for hey in range(2):
  #Statement that gets repeated
  print('hey')
  
  # Loop using i as internal variable
for i in range(3):
  print(i)

print("--")   #This is just a separator

#Loop using "something" as internal variable
for something in range(3):
  print(something)
  
  #While loops
seats = 5 # initial number of seats
while seats < 0: # seat available?
 print(seats) # ticket sold
 seats = seats + 1 # number of seats updated
 
for i in range(3):
  print(i >1) 
  
for i in range(3):
  print("First")
print("Second")

print (5 == 5) # is 5 equal to 5?
print (5 == 7) # is 5 equal to 7?
print (5 != 7) # is 5 different from 7?
print (5 != 5) # is 5 different from 5?
print (5 <= 5) # is 5 less than or equal to 5?
print (5 >= 5) # is 5 greater than or equal to 5?
  
password = "hi"
guess = input()
while guess != password:  
  guess = input() 
print("Access Granted")
  
for box in range(5):
  print("Package A")
print("Task complete")
  
#sets the value of age
age = 22
if age >= 18:
  # executed only if customer is over-age
  print("Regular price") 
else:
  #executed only if age is less than 18
  print("Discount")
  
  
age = 75
if age < 18: print("Junior discount")
elif age >= 75: print("Senior discount")
else: print("No discount")
print("Proceed to payment")
  
  
age = 16
is_student = True

if age < 18:
  #execute if age is less than 18
  if is_student:
    #execute if under 18 and also a student
    print("20% discount")
  else:
    #execute if under 18 and not a student
    print("10% discount")
else:
  #execute this code customer 18 or over
  print("Regular price")
  print('. ')
  
#exercise 1 - fasten your seatbelt
seatbelt_fastened = True
car_speed = 70
if car_speed > 0:
  if seatbelt_fastened:
    print ("Safe to drive")
else:
    print ("ALARM")
  
#exercise 2 - time's up
x=5
while x>0:
    print(x)
    x=x-1
print ("Time's up")

#exercise 3 - cell growth
for day in range(1,11):
    cell=2**day
    print(f"Day {day}: {cell} cells")
    
    
#exercise 4 - smart parking lot
spaces=5
while spaces>0:
    print (f"Car parked. {spaces} spaces left")
    spaces=spaces-1
print ("Lot full")
  
  
  
  
  
  
  
  
  


