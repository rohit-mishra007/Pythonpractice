#24. Print even and odd numbers within a range.
#count total number of Even and odd Number


#while loop
numbers=int(input("Enter the Number you want to print from 1 to = "))

i =1
even =0
odd = 0
while i <= numbers :
    if i % 2 == 0 :
        print(f"Even Number = {i}")
        even=even+1
    else:
        print(f"Odd Number = {i}")
        odd=odd+1
    i = i +1
print(f"total even No = {even}")
print(f"total odd No = {odd}")
    
# for loop 

# for j in range (0,numbers) :
#     print(f"Printing while Loop Numbers = {j+1}")