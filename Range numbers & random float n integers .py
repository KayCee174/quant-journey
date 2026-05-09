#range(start,stop,step)
prices=list(range(10,101,10))
print(prices)
prices=list(range(2,21,2))
print(prices)
prices=list(range(5,51,5))
print(prices)

#random.uniform = Decimals (Floats)
import random
prices = [random.uniform(150, 151) 
for _ in range(10)]
print (prices)
# This creates 10 random "Gold" prices between 150 and 151.

#random.randint = Whole Numbers (Integers)
import random
# Generate 10 random integers between 1 and 10
prices = [random.randint(1,10) 
for _ in range(10)]
print(prices)

#Non-Repeating Secret: random.sample()
import random
# Generate 10 unique integers between 1 and 100
unique_prices = random.sample(range(1, 11), 10)
print(unique_prices)

# Unique "pips" - unique integers divided by 100 to get unique floats
unique_floats = [x / 100 for x in random.sample(range(100, 200), 10)]
print(unique_floats)



