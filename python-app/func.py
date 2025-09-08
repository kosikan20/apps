def printHello(name):
    print("hello "+name)

printHello("Jacks")

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7


def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()       # Hello, Guest
greet("Bob")  # Hello, Bob

def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=20, name="Jane")

# *args → variable number of positional arguments
def show_numbers(*args):
    for num in args:
        print(num)

show_numbers(1, 2, 3)

# **kwargs → variable number of keyword arguments
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Jane", age=22)


square = lambda x: x * x
print(square(5))  # 25



def outer():
    def inner():
        print("Inner function")
    inner()

outer()

def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
print(double(5))  # 10