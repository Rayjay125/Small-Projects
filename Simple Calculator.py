#Simple Calculator

print("Welcome")

#making a simple calculator
#input numbers and operation
first_integer = float(input("Enter first integer: "))
operation = input("Choose operation (+),(-),(*) or (/): ")
second_integer = float(input("Enter second integer: "))

#logic
if operation == "+":
    result=int(first_integer) + int(second_integer)
elif operation == "-":
    result = int(first_integer) - int(second_integer)
elif operation == "*":
    result = int(first_integer) * int(second_integer)
else:
    result=int(first_integer) / int(second_integer)

#print result
print("\nanswer:", result)