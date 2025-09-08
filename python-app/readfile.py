filename = input("Enter the filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
