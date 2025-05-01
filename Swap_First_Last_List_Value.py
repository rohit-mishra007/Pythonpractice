

# To interchange first and last elements in a list
my_list = [1, 2, 3, 4, 5]

print(f"My List After Change {my_list}")
my_list[0],my_list[-1]=my_list[-1],my_list[0]
#my_list[-1]=my_list[0]

print(f"My List After Change {my_list}")



""" Below is Output of execution
My List After Change [1, 2, 3, 4, 5]
My List After Change [5, 2, 3, 4, 1]
"""

