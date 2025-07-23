fruits_list = ['apple', 'banana', 'orange', 'apple', 'grape']
fruits_tuple = ('apple', 'banana', 'orange')
fruits_set = {'apple', 'banana', 'orange', 'grape'}
fruits_dict = {'apple': 5, 'banana': 3, 'orange': 8, 'grape': 2}

print("apple" in fruits_list)
print("apple" in fruits_tuple)
print("apple" in fruits_set)
print("apple" in fruits_dict)

print(len(fruits_list))
print(len(fruits_tuple))
print(len(fruits_set))
print(len(fruits_dict))

for fruit in fruits_list:
    print(fruit)

for fruit in fruits_tuple:
    print(fruit)

for fruit in fruits_set:
    print(fruit)

for fruit, count in fruits_dict.items():
    print(fruit, count)

for item in fruits_list:
    print(item)

for item in fruits_tuple:
    print(item)

for item in fruits_set:
    print(item)

for key in fruits_dict:
    print(key)

for value in fruits_dict.values():
    print(value)

for key, value in fruits_dict.items():
    print(key, value)
