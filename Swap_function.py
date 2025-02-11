def swap(x, y):
    temp = x
    x = y
    y = temp
    return x ,y
# Driver code
x = 2
y = 3
print(x)
print(y)
print(f"{swap(x, y)}")
x,y =swap(x, y)
print(x)
print(y)
