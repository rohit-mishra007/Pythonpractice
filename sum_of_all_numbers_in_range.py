#Python program to print the sum of all numbers in the given range


num=int(input("Enter the number you want to print from 1 to N= "))
sum=0
for i in range (1,num+1):
    print(f"{sum}+{i}= {sum+i}")
    sum=sum+i
    
print(f"sum of all number from 1 to {i} = {sum}")    