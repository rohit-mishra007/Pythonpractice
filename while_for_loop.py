#23. Print numbers from 1 to N using a for loop.

#while loop
numbers=int(input("Enter the Number you want to print from 1 to = "))

i =1
while i <= numbers :
    print(f"Printing while Loop Numbers = {i}")
    i = i +1
    
    
# for loop 

for j in range (0,numbers) :
    print(f"Printing while Loop Numbers = {j+1}")