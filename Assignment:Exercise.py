u=10.2
a=10.01
t=4
v=u+a*t
print(v)
print('\n')

# we list all the natural numbers below 10 that are multiples of 3 and 5 we get 3,5,6 and 9. 
# The sum of these multiples is 23
# Implement and algorithm with Python to find the sum of all the multiples of 3 or 5 below 1000.

# Method 1 
total = 0
for i in range(1,10):
    if i % 3 == 0 or i % 5 == 0:
        total +=i
print(total)

total = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        total+=i
print(total)

# Method 2 
# N=range(1,10,1)
mult_3=range(3,10,3)
mult_5=range(5,10,5)
mult3_5=list(mult_3) + list(mult_5)
summ=sum(mult3_5)
print(summ)

# N=range(1,1000,1)
mult_3=range(3,1000,3)
mult_5=range(5,1000,5)
mult3_5=set(list(mult_3) + list(mult_5))
summ=sum(mult3_5)
print(summ)

# Method 3 
def sum_of_multiples(n):
  mult3 = list(range(3,n,3))
  mult5 = list(range(5,n,5))
  mult3_5 = set(mult3 + mult5)
  summ = sum(mult3_5)
  return summ
  
print(sum_of_multiples(10))
print(sum_of_multiples(1000))

print('\n')
 
# Method 4
def sum_of_multiples(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total 
print(sum_of_multiples(10))
print(sum_of_multiples(1000))





# Find the sum of the even fib sequence whose values do not exceed 4million
def even_fibonacci_sum(limit):
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total
print(even_fibonacci_sum(4000000))


# Fibonacci Sequence
def fibonacci(n):
    a, b = 1, 2
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(10))




