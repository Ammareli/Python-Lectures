# # what are methods?
# # Methods are functions that are associated with a particular data type or class in programming.
# # They are used to perform specific operations or actions on objects of that data type.
# # Methods are called on an object using dot notation, where the method name is preceded by the
# # object it is being called on.
# list_1 = [5, 2, 9, 1, 5, 6]
# # Using the sort() method to sort the list in ascending order
# list_1.sort(reverse=True)
# print("Sorted list:", list_1)

# # pop method
# popped_item = list_1.pop()  # Removes and returns the last item from the list
# print("Popped item:", popped_item)
# print("List after popping an item:", list_1)


# # WHAT IS MENT BY CALL?
# # In programming, "call" refers to the action of invoking or executing a function or method.
# def add(a, b):
#     return a + b

# # Calling the add function with arguments 3 and 5
# result = add(3, 5)
# print("Result of addition:", result)

# list of most used methods in python LIST METHODS
""" 
1- append() - Adds an item to the end of the list.
2- extend() - Extends the list by appending elements from another iterable.
3- insert() - Inserts an item at a given position.
4- remove() - Removes the first occurrence of a specified value.
5- pop() - Removes and returns an item at a given index (default is the last item).
6- clear() - Removes all items from the list.
7- index() - Returns the index of the first occurrence of a specified value.
"""
# Example usage of some list methods
# my_list = [1, 2, 3]
# my_list.append(4)  # Adds 4 to the end of the list
# print("After append:", my_list)

# my_list.remove(2)  # Removes the first occurrence of 2
# print("After remove:", my_list)

# popped_value = my_list.pop()  # Removes and returns the last item
# print("Popped value:", popped_value)
# print("Final list:", my_list)

# my_list.insert(1, "Ammar")  # Inserts 5 at index 1
# print("After insert:", my_list)

# my_list.extend([5, 6, 7,7])  # Extends the list with another list
# print("After extend:", my_list)

# index_of_3 = my_list.index(3)  # Returns the index of the first occurrence of 3
# print("Index of 3:", index_of_3)

# my_list.clear()  # Removes all items from the list
# print("After clear:", my_list)

# String METHODS
"""
1- upper() - Converts all characters in the string to uppercase.
2- lower() - Converts all characters in the string to lowercase.
3- strip() - Removes leading and trailing whitespace from the string.
4- replace() - Replaces occurrences of a specified substring with another substring.
5- split() - Splits the string into a list of substrings based on a specified
"""

# Example usage of some string methods
my_string = "  Hello, World!  "
upper_string = my_string.upper()  # Converts to uppercase
print("Uppercase string:", upper_string)

lower_string = my_string.lower()  # Converts to lowercase
print("Lowercase string:", lower_string)

stripped_string = my_string.strip()  # Removes leading and trailing whitespace
print("Stripped string:", stripped_string)

replaced_string = my_string.replace("World", "Python")  # Replaces "World" with "Python"
print("Replaced string:", replaced_string)

split_string = my_string.split(",")  # Splits the string at the comma
print("Split string:", split_string)
