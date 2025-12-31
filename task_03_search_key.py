data = {"name": "Ali", "age": 22}

key = input("Enter key: ")

if key in data:
    print("Value:", data[key])
else:
    print("Key not found")
