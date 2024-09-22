dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

quotient = 0
while dividend >= divisor:
    dividend -= divisor
    quotient += 1
print(f"The result of integer division is: {quotient}")
