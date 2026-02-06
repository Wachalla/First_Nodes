# Array_Treasure_hunt

treasures = [12, 45, 99, 23, 8]

biggest_found = treasures[0]

# 2. Walk through each box
for item in treasures:
    if item > biggest_found:
        biggest_found = item #letss gooo

print("Biggest treasure is:", biggest_found)


# Time complexity wise, 
#This is O(n) speed. It means I have to look at 
# every box exactly once to be sure I found the best one.


