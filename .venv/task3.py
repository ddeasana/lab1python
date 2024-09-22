a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = 0
i = 0
while i < b:
    result += a
    i += 1
print(f"The result of {a} multiplied by {b} is: {result}")
