age = input("Enter your age = ")
if int(age) < 10:
    print (f"you are minor , your age is {age}")
elif int(age) <18:
    print(f"you can't vote , your age is {age}")
else:
    print(f"you can vote , your age is {age}")