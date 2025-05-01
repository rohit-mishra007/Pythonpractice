#Python program to print numbers from 1 to n except 5 multiples

num=int(input("Enter the number you want to print from 1 to N= "))
for i in range (1,num):
    if i % 5 == 0:
        # print(" value")
        pass
    else:
        print(f"{i}")

# print(f"{11%5}")
# print(f"{5%5==0}")