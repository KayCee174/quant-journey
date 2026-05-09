print('Hello there')
print('my name is KayCee')
print('I am learning Python')
print("I started learning python on the 18th of September 2024")
print("I am learning with Alison and working with Replit")
print("I stopped for 18 months and now I'm back in April 2026")

# -> variable name=value 

age=22
print(age)
age=23
print(age)

print(type(age))

midage=age/2

print(midage)
print(type(midage))

# operators + - * / % // ** =
hi = 1
hi += 2
print (hi)

first_name = "kay"
last_name ="Cee"
print (first_name + last_name)
print(first_name + " " + last_name)
print(first_name * 2)


#collections -> lists
names = [2,4,6,8]
print(names[1])
print(len(names))
print(names)

names.append(12)
print(names)
names.insert(4,10)
print(names)
names.remove(12)
print(names)

del(names[3])
print(names)

names[0]=0
print(names[0:2])
print(names)
gb =[4,8,16]
print(gb)
gb.append(32)
print(gb)
gb.insert(4,64)
print(gb)
gb[0]=2
print (gb)
del(gb[0])
print(gb)
print(gb[0:1])
gb.remove(64)
print(gb)

#tuples
score =("Kc",100)
print(score)

score =("KayCee","Bright",110)
print(score)

name = score [0]
print(name)
print(len(score))

print("KayCee" in score)
print(score)

print(8 in gb)
print(name[0])
print(name[0:1])
print("A" in name)

name = input("what is your name? ")
print(name)

# Check if number is even or odd
num = int(input("Enter any number: "))
print(num)
if (num % 2) == 0:
    print("{0} is Even" .format(num))
else:
  print("{0} is Odd".format(num))