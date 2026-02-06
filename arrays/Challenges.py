#Challenge 1:Find the maximum value in an array without using max()
numbers = [
    187, 314, 256, 299, 102, 238, 301, 275, 223, 309,
    194, 283, 217, 324, 266, 198, 305, 249, 312, 231,
    207, 298, 276, 220, 317, 201, 284, 310, 234, 293,
    218, 300, 263, 191, 308, 242, 279, 305, 225, 296,
    210, 313, 254, 286, 203, 319, 221, 287, 299, 230
]
highest_number=number[0]
#traversal
from n in numbers:
   if n > highest_number
   highest = t

print(f"The highest recorded temp is: {highest}")

# #Challenge 2 :Find the second largest number in one single walk (O(n)).
numbers = [
    187, 314, 256, 299, 102, 238, 301, 275, 223, 309,
    194, 283, 217, 324, 266, 198, 305, 249, 312, 231,
    207, 298, 276, 220, 317, 201, 284, 310, 234, 293,
    218, 300, 263, 191, 308, 242, 279, 305, 225, 296,
    210, 313, 254, 286, 203, 319, 221, 287, 299, 230
]
largest = float('-inf')
second = float('-inf')
for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n < largest:
        second = n
print(second if second != float('-inf') else None)
   
