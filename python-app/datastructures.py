fruit_lists = ['apple', 'orange', 'mango', 'apple']

print("📋 Original fruit list:")
print(fruit_lists)

# List methods
print(f"📍 Index of 'apple': {fruit_lists.index('apple')}")
print(f"🧮 Count of 'apple': {fruit_lists.count('apple')}")

fruit_lists.append("tangerine")
print(f"🍊 After appending 'tangerine': {fruit_lists}")

fruit_lists.remove("mango")
print(f"🗑️ After removing 'mango': {fruit_lists}")

fruit_lists.reverse()
print(f"🔄 After reversing: {fruit_lists}")

fruit_lists.sort()
print(f"⬆️ After sorting: {fruit_lists}")

fruit_lists.insert(0, "banana")
print(f"➕ After inserting 'banana' at index 0: {fruit_lists}")

fruit_lists.pop(-1)
print(f"➖ After popping last element: {fruit_lists}")

print("\n🎓 Tuple: Grades")
grades = ('A', 'B', 'C')
print(f"Grades tuple: {grades}")
print(f"🧮 Count of 'A': {grades.count('A')}")
print(f"📍 Index of 'A': {grades.index('A')}")

print("\n👩‍🎓 Dictionary: Student")
students = {"name": "jane", "age": 10}
print(f"Student info: {students}")
print(f"Name: {students['name']}, Age: {students['age']}")

# Dict methods
keys = students.keys()
values = students.values()
items = students.items()
print(f"🔑 Keys: {keys}")
print(f"📦 Values: {values}")
print(f"🧾 Items: {items}")

students["grade"] = 'A'
print(f"📘 After adding 'grade': {students}")

students.pop("age")
print(f"❌ After removing 'age': {students}")

print("\n🍇 Set: Fruits")
fruit = set(fruit_lists)
print(f"Original fruit set: {fruit}")

fruit.add("peach")
fruit.remove("apple")        # Will raise error if 'apple' is not present
fruit.discard("mango")       # Won't raise error if 'mango' not in set

print(f"🍑 After adding 'peach' and removing 'apple': {fruit}")

vegetables = {"carrot", "salad", "beans"}

# Set operations
food = vegetables.union(fruit)
foodInt = vegetables.intersection(fruit)

print(f"\n🍽️ All food (union): {food}")
print(f"🥗 Common food (intersection): {foodInt}")
