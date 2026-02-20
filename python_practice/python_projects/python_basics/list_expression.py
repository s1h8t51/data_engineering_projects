nums = [1, 2, 3, 4, 5]
filtered = [x for x in nums if x > 2]  # [3, 4, 5]
doubled = [x*2 for x in nums]  # [2, 4, 6, 8, 10]
new_nums = nums.append(7) 
print(new_nums)


items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart'] 

soups = ['minestrone', 'lentil', 'pho', 'laksa']
soups[-1]   # 'laksa'
soups[-3:]  # 'lentil', 'pho', 'laksa'
soups[:-2]  # 'minestrone', 'lentil'


 # 2D list of people's heights
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
# Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)

# Output
# 61


# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Removes the first occurance of "Chris"
shopping_line.remove("Chris")
print(shopping_line)

# Output
# ["Cole", "Kip", "Sylvana", "Chris"]

print(filtered)
print(doubled)


backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')

print(numPen)
# Output: 3


exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList) # original list sorted 
# Output: [1, 2, 3, 4]
unsortedList = [4, 2, 1, 3]
sortedList = sorted(unsortedList) # has to be new list 
print(sortedList)
# Output: [1, 2, 3, 4]

tools = ['pen', 'hammer', 'lever']
tools_slice = tools[1:3] # ['hammer', 'lever']
tools_slice[0] = 'nail'

# Original list is unaltered:
print(tools) # ['pen', 'hammer', 'lever']


# Here is a list representing a line of people at a store
store_line = ["Karla", "Maxium", "Martim", "Isabella"]

# Here is how to insert "Vikor" after "Maxium" and before "Martim"
store_line.insert(2, "Vikor")

print(store_line) 
# Output: ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

# Pop the last element
removed_element = cs_topics.pop()

print(cs_topics)
print(removed_element)

# Output:
# ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# 'Clowns 101'

# Pop the element "Baloon Making"
cs_topics.pop(2)
print(cs_topics)

# Output:
# ['Python', 'Data Structures', 'Algorithms']




#=================================================================

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

len(my_tuple) # returns length of tuple
max(my_tuple) # returns maximum value of tuple
min(my_tuple) # returns minimum value of tuple
my_tuple.index(123) # returns the position of the value 123
my_tuple.count('abc') # returns the number of occurrences of the value 'abc'