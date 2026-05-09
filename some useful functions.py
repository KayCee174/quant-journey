# SOME USEFUL FUNCTIONS FROM FCC 
# by KayCee - April 21st, 2026

# round() to nearest whole int
print(round(1.47))
# round() with 2 argument, the next one is the number of dp to be approximated to
print(round(3.14159))
print(round(3.14159,3))
print(round(3.14159,4))
print(round(3.14159,2))

# divmod(x,y) - outputs the quotient and the remainder in a tuple
print(27//5) #quotient
print(27%5) #remainder
print(divmod(27,5))

# isinstance() - returns True, if the first argument is an instance of that class
print(isinstance(1,int))
print(isinstance(1.0,int))
print(isinstance('Hey',str))
print(isinstance(1.0,(int,float))) #either this type or that type
print('\n')
test=[2,4,8,2.1,'hey',2+3j]
print(isinstance(test[4],str))
print(isinstance(test[5],complex))
print(isinstance(test,(int,float,str,complex)))
print(isinstance(test[3],(int,float,str,complex)))
print(isinstance(test,list))

# pow(x,y,z) - x raise to the power y and remainder by z
# x**y is same as pow(x,y)
# (x**y)%z is same as pow(x,y,z)
print(pow(2,4))
print(pow(2,3,3))

# input() 
x=input('Enter your name:')
print(f"My name is {x}")
y=int(input('What year were you born?'))
age = 2026 - y
print(f'My name is {x}, and I am {age} years old')

help(pow)


