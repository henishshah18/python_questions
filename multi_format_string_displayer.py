# Variables
name = 'Alice'
age = 28
city = 'Delhi'

# 1️⃣ Using % formatting
print("My name is %s, I am %d years old, and I live in %s." % (name, age, city))

# 2️⃣ Using .format() method
print("My name is {}, I am {} years old, and I live in {}.".format(name, age, city))

# 3️⃣ Using f-strings (Python 3.6+)
print(f"My name is {name}, I am {age} years old, and I live in {city}.")
