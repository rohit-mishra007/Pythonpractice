#14. Swap two numbers without using a temporary variable.

Number1 = 15
Number2 = 10
print(f"Number1 value before swap {Number1}")
print(f"Number2 value before swap {Number2}")

temp=Number2
Number2=Number1
Number1=temp

print(f"Number1 value After swap {Number1}")
print(f"Number2 value After swap {Number2}")