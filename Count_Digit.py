#Count Number of Digit

number=int(input("Enter the Number= "))
count=0
if number > 0 :
    while number > 0 :
        number=number//10
        count=count+1
    print(f"Number of Digit for given number is {count}")    
    
else :
    print(f"Given numbe is not valid ineteger number")