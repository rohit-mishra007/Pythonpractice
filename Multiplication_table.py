#32. Print multiplication table of a given number.



#while loop
numbers=int(input("Enter the Number you want table = "))

i =1
while i <= 10 :
    print(f"{numbers}*{i}={numbers*i}")
    i = i +1

    
# for loop 

# for j in range (0,numbers) :
#     print(f"Printing while Loop Numbers = {j+1}")