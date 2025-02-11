#19. Find the largest of three numbers.

Number1 = int(input("Enter the Number1 = "))
Number2 = int(input("Enter the Number2 = "))
Number3 = int(input("Enter the Number3 = "))


if Number1 > Number2 and Number1 > Number3 :
	print(f"Number1 = {Number1} is larger than Number2 and Number3")
	
elif Number2 > Number1 and Number2 > Number3 :
	print(f"Number2 = {Number2} is larger than Number1 and Number3")
	
elif Number3 > Number1 and Number3 > Number2 :
	print(f"Number3 = {Number3} is larger than Number1 and Number2")

else:
	print(f" all 3 Numbers are same ")
