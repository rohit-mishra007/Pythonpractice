#10. Perform arithmetic operations (+, -, *, /, %, //, **) on two numbers.


Number1=int(input("Enter Number 1 = "))
Number2=int(input("Enter Number 2 = "))
Operation=input("Enter The operation = ")

if Operation == '+':
    print(f"Addition of {Number1} and {Number2} = {Number1+Number2}")
elif Operation == '-':
    print(f"Substraction of {Number1} and {Number2} = {Number1-Number2}")
elif Operation == '*':
    print(f"Multiplication of {Number1} and {Number2} = {Number1*Number2}")
elif Operation == '/':
    print(f"Division of {Number1} and {Number2} = {Number1/Number2}")
else:
    print("Operation other than + - * /")
