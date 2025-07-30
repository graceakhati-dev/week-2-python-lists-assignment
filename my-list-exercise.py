# Create an empty list
my_list = [] 

# Add numbers to the list one by one
my_list.append(10)  
my_list.append(20)  
my_list.append(30)  
my_list.append(40)  

# Insert the number 15 at position 1 (second place)
my_list.insert(1, 15) 

# Add more numbers using another list
my_list.extend([50, 60, 70])  

# Remove the last number from the list
my_list.pop()  # Removes 70

# Arrange the list ascending order
my_list.sort()  

# Find the position of number 30
index_of_30 = my_list.index(30)  

# Show the index of 30
print("The position of 30 is:", index_of_30)

# Show the final version of the list
print("Final list:", my_list)

