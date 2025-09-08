from functools import reduce
numbers = [1, 2, 3, 4]

# square each number
squares = list(map(lambda x: x*x, numbers))
print(squares)  # [1, 4, 9, 16]


numbers = [1, 2, 3, 4]

# sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 10


numbers = [1, 2, 3, 4, 5]

# keep even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
