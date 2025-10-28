"""
LOOPS....

LIST : 
DATA TYPE WHICH STORES MULTIPLE ITEMS IN A SINGLE VARIABLE.

NAMES = ["ALICE", "BOB", "CHARLIE", "DAVID"]

FOR LOOP. -> ITRATAEBLES.

FOR variable IN ITRATAEBLES:
    # CODE TO BE EXECUTED

"""

NUMBERS = [1, 2, 3, 4, 5]   

# print(NUMBERS[0])
# print(NUMBERS[1])

# print(NUMBERS[2])

# print(NUMBERS[3])

# print(NUMBERS[4])

# for number in range(1, 6):
#     print(number)

"""
while condition:
    # CODE TO BE EXECUTED

"""

number = 1

while True:
    print("This will run forever unless we break the loop.")
      # This will ex!it the loop immediately
    i = input("Type 'e' to stop the loop: ")
    if i == 'e':
        break
    if i == 'c':
        continue
    print(f"Current number is: {number}")
    number += 1

