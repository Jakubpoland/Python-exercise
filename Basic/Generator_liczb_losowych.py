import random
x = random.randint(0, 9)
print(x)

x = random.random()
print(x)

my_list = [1, 2, 3, 4, 5]
x = random.choice(my_list)
print(x)

mylist = ["apple", "banana", "cherry", "pineapple", "orange"]
print(random.sample(mylist, k=2))

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
