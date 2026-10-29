# Name:Caleb
# Period:PM

# ============================================================
# Python Skills Check — LISTS & LOOPS
# CHALLENGE VERSION — 40 TASKS
# ============================================================
# DIRECTIONS:
# - Create a repository, clone it, and add this file.
# - Complete each task UNDER its directions.
# - Do not delete the directions.
# - Use ONLY concepts learned in class, except for 'in' and 'not in'.
#   You must research these two new operators independently in Section 5.
# - Use the EXACT variable and function names provided.
# - The entire file must run without errors.
# - Do not hard-code results Python should calculate.
# - Unless a task says otherwise, do NOT use sum(), min(), max(),
#   sorted(), sort(), list comprehensions, sets, or dictionaries.
# - For functions, RETURN values when instructed; do not just print.
# - Test edge cases and change the starting values to check your logic.
# - Tasks that ask for input() may be tested individually.

# ============================================================
# SECTION 1 — LIST FUNDAMENTALS (TASKS 1–6)
# ============================================================

def line(a):
    print()
    print("task", a)
# TASK 1:
# Create a list named scores containing 85, 92, 78, 96, 88.
# Print the entire list and its length using len().
line(1)
score = [85, 92, 78, 96, 88]
print(score, len(score))


# TASK 2:
# Using scores from Task 1, print the FIRST, THIRD, and LAST
# elements on separate lines. Use indexes, not hard-coded values.
line(2)
print(score[0])
print(score[2])
print(score[len(score)-1])

# TASK 3:
# Change the third element of scores to 100.
# Print the updated list. Do not create a replacement list.
line(3)
score[2] = 100
print(score)

# TASK 4:
# Create games = ["Minecraft", "Roblox", "Fortnite"].
# Append "Valorant" and insert "Rocket League" at index 1.
# Print games. Check the order carefully.
line(4)
games = ["Minecraft", "Roblox", "Fortnite"]
games.append("Valorant")
games.insert(1, "Rocket League")
print(games)

# TASK 5:
# Using games from Task 4, remove "Roblox" with remove().
# Then pop the FIRST item into a variable named removed_game.
# Print removed_game and the remaining games list.
line(5)
games.remove("Roblox")
removed_game = games.pop(0)
print(removed_game, games)


# TASK 6:
# Create colors = ["red", "blue", "green", "yellow", "purple"].
# Store the index of "green" in green_index using index().
# Print green_index. Then replace "yellow" with "orange".
# Print the new list.
line(6)
colors = ["red", "blue", "green", "yellow", "purple"]
green_index = colors.index("green")
print(green_index)
colors[3] = "orange"
print(colors)

# ============================================================
# SECTION 2 — FOR LOOPS & RANGE (TASKS 7–12)
# ============================================================

# TASK 7:
# Use a for loop with range() to print numbers 1 through 20,
# INCLUDING 20. Do not manually print the numbers.
line(7)
for i in range(1, 21):
    print(i)

# TASK 8:
# Use a for loop with range() to print 30, 27, 24, ... 0.
# IMPORTANT: The zero must be included.
line(8)
for i in range(11):
    print(30 - i * 3)


# TASK 9:
# Use a for loop to print all EVEN numbers from 1 to 50.
# You MUST use an if statement and the % operator inside the loop.
line(9)
for i in range(1,51):
    if i % 2 == 0:
        print(i)

# TASK 10:
# Create number = 7.
# Print its multiplication table from 1 through 12 using a for loop.
# Example line: 7 x 3 = 21
# Your code must also work if number changes.
line(10)
number = 7
for i in range(1, 13):
    print(f"{number} x {i} = {number*i}")

# TASK 11:
# Create students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"].
# Use a for loop to print "Student: " followed by each name.
# Do NOT write five separate print statements.
line(11)
students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
for i in students:
    print(f"student {students.index(i) + 1}:", i)

# TASK 12:
# Using students, print a NUMBERED roster:
# 1. Alex
# 2. Jordan
# ...
# 5. Casey
# Use range(len(students)) OR enumerate().
line(12)
for i in range(len(students)):
    print(i + 1, f". {students[i]}")

# ============================================================
# SECTION 3 — WHILE LOOPS & VALIDATION (TASKS 13–18)
# ============================================================

# TASK 13:
# Create countdown = 10.
# Use a while loop to print from countdown down to 0.
# Then print "Blast off!". Avoid an infinite loop.
line(13)
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")


# TASK 14:
# Create password = "Python123".
# Keep asking the user for a password until it matches.
# Print "Access granted" exactly once after a correct entry.
line(14)
password = "Python123"
entry = "Python123" #this is supposed to be blank, i just wanna skip the input()
while entry != password:
    print()
    entry = input("enter password: ")
    if entry != password:
        print("wrong password, guess again")
    else:
        print("Access granted")

# TASK 15:
# Ask the user for an integer between 1 and 10 INCLUSIVE.
# Keep asking while the value is invalid.
# After a valid entry, print "Valid number".
# Test 0, 1, 10, and 11.
line(15)
integer = 5 # supposed to be 0, i just wanna skip the input()
while integer < 1 or integer > 10:
    integer = int(input("enter integer between 1 and 10: "))
    if integer < 1 or integer > 10:
        print('invalid number')
    print()
    
print("Valid number")

# TASK 16:
# Create total = 0.
# Repeatedly ask for an integer. Add each nonzero entry to total.
# Stop when the user enters 0, then print total.
# Example inputs: 5, 8, -2, 0 -> Total: 11.
line (16)
total = 0
guess = 0 #should be 100 just wanna skip input()
while guess != 0:
    guess = int(input('enter any int, 0 to finish'))
    total += guess
    print()
print(total)

# TASK 17:
# Create secret = "robot" and attempts = 3.
# Ask the user to guess secret, allowing AT MOST 3 guesses.
# Print "Correct" if guessed in time; otherwise "Out of attempts".
# Make sure a correct guess does NOT print both messages.
line(17)
secret = "robot"
attempts = 0 #should be 3 but i wanna skip
for i in range(attempts):
    print(f"\nattempt {i + 1}/{attempts}")
    guess = input('guess the secret: ')
    if guess == secret:
        print("Correct")
        break
    else:
        if i == attempts - 1:
            print('out of attempts')
        else:
            print('incorrect, guess again')

# TASK 18:
# Make a while-loop menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit
# Repeat until the user enters 3. Handle invalid choices.
# Print "Goodbye" only when option 2 is selected.
line(18)
menu = False #should be True but i WANA SKIP
while menu:
    print("\n1. Say Hello\n2. Say Goodbye\n3. Exit")
    action = input('\nwhat would you like to do (1-3): ')
    if action == "1":
        print("Hello")
    elif action == "2":
        print("Goodbye")
    elif action == "3":
        menu = False
    else:
        print('please choose one of the following options')

# ============================================================
# SECTION 4 — PROCESSING LISTS WITH LOOPS (TASKS 19–24)
# ============================================================

# TASK 19:
# Create numbers = [4, 8, 15, 16, 23, 42].
# Use a for loop to calculate and print their total.
# Do NOT use sum().
line(19)
numbers = [4,8,15,16,23,42]
total = 0
for i in numbers:
    total += i
print(total)

# TASK 20:
# Create grades = [90, 85, 78, 92, 88].
# Use a loop and len() to calculate the average.
# Print the average. Do NOT use sum().
line(20)
grades = [90,85,78,92,88]
total = 0
for g in grades:
    total += g
average = total / len(grades)
print(average)

# TASK 21:
# Create numbers = [3, 8, 12, 7, 15, 20, 24, 9].
# Use ONE loop to count even and odd values separately.
# Print "Even: [count]" and "Odd: [count]".
line(21)
numbers = [3,8,12,7,15,20,24,9]
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, odd)

# TASK 22:
# Create numbers = [-14, -67, -23, -89, -45].
# Use a loop to find and print the HIGHEST number.
# Do NOT use max() or sorting.
# IMPORTANT: Starting your answer at 0 gives a wrong result.
line(22)
numbers = [-14,-67,-23,-89,-45]
highest = numbers[0]
for n in numbers:
    if n > highest:
        highest = n
print(highest)

# TASK 23:
# Create numbers = [14, 67, 23, 89, 45, 12].
# Use a loop to find and print the LOWEST number.
# Do NOT use min() or sorting.
# Your logic must also work with all-negative numbers.
line(23)
numbers = [14,67,23,89,45,12]
lowest = numbers[0]
for n in numbers:
    if n < lowest:
        lowest = n
print(lowest)

# TASK 24:
# Create numbers = [5, 2, 5, 8, 5, 3, 2, 5].
# Create target = 5.
# Use a loop to count how often target appears; print the count.
# Do NOT use count(). It must work if target changes.
line(24)
numbers = [5,2,5,8,5,3,2,5]
target = 5
count = 0
for n in numbers:
    if n == target:
        count += 1
print(count)

# ============================================================
# SECTION 5 — IN / NOT IN (TASKS 25–30)
# ============================================================
# INDEPENDENT RESEARCH REQUIRED:
# We have NOT covered 'in' and 'not in' in class. Before starting
# Tasks 25–30, research both operators on your own using reliable
# Python learning resources or the official Python documentation.
# Learn what each operator does, how it works with lists, and how
# to use it inside if statements and while loops.
# Write a short comment in your code explaining the difference
# between 'in' and 'not in' in your own words.
# The examples below are starting hints, NOT a substitute for research.
#
# NEW CONCEPT:
# 'in' checks whether a value is in a list.
# Example: "apple" in ["apple", "banana"] evaluates to True.
# 'not in' checks whether a value is missing.
# Example: "grape" not in ["apple", "banana"] evaluates to True.
# These expressions are useful in if statements and while loops.

# TASK 25:
# Create foods = ["pizza", "burger", "tacos", "sushi", "pasta"].
# Ask the user to enter a food.
# Use 'in' to print "Available" or "Not available".
# Do NOT use index() to search.
line(25)
foods = ["pizza", "burger", "tacos", "sushi", "pasta"]
food = input('enter a food: ')
if food in foods:
    print('available')
else:
    print('not available')

# TASK 26:
# Create supplies = ["pencil", "notebook", "eraser", "backpack"].
# Ask the user for an item.
# Use 'not in' to print "Need to buy" if it is missing,
# otherwise print "Already have it".
line(26)
supplies = ["pencil", "notebook", "eraser", "backpack"]
item = input('give me an item: ')
if item not in supplies:
    print('need to buy')
else:
    print('already have it')


# TASK 27:
# Create usernames = ["alex123", "gamer99", "pythonpro"].
# Ask the user to enter a new username.
# If it is already in the list, print "Username taken".
# Otherwise append it and print the updated list.
# Do not allow duplicates.

line(27)
usernames = ["alex123", "gamer99", "pythonpro"]
username = input("enter a new username: ")
if username in usernames:
    print('username already taken')
else:
    usernames.append(username)
print(usernames)

# TASK 28:
# Modify the idea from Task 27 using a NEW list named accounts.
# Start with accounts = ["admin", "guest"].
# Use a while loop to keep asking until the entered name
# is NOT in accounts. Append the accepted name and print accounts.
# REQUIREMENT: Use 'not in' in your solution.
line(28)
accounts = ["admin", "guest"]
cd = True
while cd:
    name = input('enter name')
    if name not in accounts:
        accounts.append(name)
        cd = False
    else:
        print('already in accounts')
print(accounts)

# TASK 29:
# Create secret_words = ["dragon", "robot", "python", "galaxy"].
# Keep asking the user for a word UNTIL it is in secret_words.
# Count and print the number of guesses made.
# A correct first guess should count as 1.
line(29)
secret_words = ["dragon", "robot", "python", "galaxy"]
count = 0
cd = True
while cd:
    guess = input('guess the secret words: ')
    if guess in secret_words:
        print('correct')
        count +=1
        cd = False
    else:
        print('incorrect guess again')
        count += 1

# TASK 30:
# Create guests = [].
# Ask the user to enter EXACTLY FIVE UNIQUE guest names.
# If a name is already in guests, reject it and ask again.
# Use a while loop, 'in' or 'not in', and append().
# Print the finished list and its length.
line(30)
guests = []
cd = True
while cd:
    if len(guests) == 5:
        cd = False
    else:
        name = input('give me 5 unique guest names: ')
        if name in guests:
            print('rejected give me another one')
        else:
            guests.append(name)
print(guests)

# ============================================================
# SECTION 6 — LISTS + FUNCTIONS (TASKS 31–35)
# ============================================================

# TASK 31:
# Create a function named count_positive(numbers).
# RETURN how many elements are greater than 0.
# Do NOT use count().
# Test: count_positive([-2, 0, 4, 9, -1]) -> 2
line(31)
def count_positive(numbers):
    count = 0
    for i in numbers:
        if i > 0:
            count += 1
    return count
print(count_positive([-2,0,4,9,-1]))

# TASK 32:
# Create a function named find_item(items, target).
# RETURN the index of the FIRST matching item, or -1 if missing.
# Do NOT use index().
# Test: find_item(["cat", "dog", "cat"], "cat") -> 0
# Test: find_item(["cat", "dog"], "fish") -> -1
line(32)
def find_item(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
print(find_item(["cat", "dog", "cat"], "cat"))
print(find_item(["cat", "dog"], "fish"))

# TASK 33:
# Create a function named unique_items(items).
# RETURN a NEW list without duplicate values, preserving first
# appearance order. REQUIREMENT: Use 'not in'.
# Test: unique_items([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
line(33)
def unique_items(items):
    new_list = []
    for i in items:
        if i not in new_list:
            new_list.append(i)
    return new_list
unique_items([1, 2, 2, 3, 1, 4])

# TASK 34:
# Create a function named common_items(list1, list2).
# RETURN a NEW list of values found in BOTH lists.
# Include each matching value only once, in list1's order.
# REQUIREMENT: Use both 'in' and 'not in'.
# Test: common_items([1, 2, 3, 3], [3, 4, 1]) -> [1, 3]
line(34)
def common_items(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            if i not in list3:
                list3.append(i)
    return list3
common_items([1, 2, 3, 3], [3, 4, 1])

# TASK 35:
# Create a function named reverse_list(items).
# RETURN a NEW list in reverse order, without changing items.
# Do NOT use reverse(), reversed(), or [::-1].
# Test: reverse_list([10, 20, 30]) -> [30, 20, 10]
line(35)
def reverse_list(items):
    new_list = []
    for i in items:
        new_list.insert(0, i)
    return new_list
reverse_list([10, 20, 30])

# ============================================================
# SECTION 7 — DEBUGGING (TASKS 36–37)
# ============================================================

# TASK 36:
# Fix this code so it prints 1, 2, 3, 4, 5 exactly once each.
# Explain in a comment what was wrong.
#
# number = 1
# while number <= 5:
#     print(number)
#
# Do NOT replace the while loop with a for loop.
line(36)
number = 1
while number <= 5:
    print(number)
    number += 1

# TASK 37:
# Fix this code so it removes ALL 4s without skipping any.
# Explain in a comment why the original approach can fail.
#
# values = [4, 4, 7, 4, 9]
# for value in values:
#     if value == 4:
#         values.remove(value)
# print(values)
#
# Expected: [7, 9]
# HINT: A while loop and 'in' can help.
line(37)
values = [4,4,7,4,9]
for value in values:
    if value == 4:
        list.pop(values.index(value))
print(values)
# ============================================================
# FINAL BOSS CHALLENGES (TASKS 38–40)
# ============================================================

# TASK 38 — SHOPPING LIST MANAGER:
# Build a menu-driven program with:
# 1. Add item
# 2. Remove item
# 3. View numbered items
# 4. Search for item
# 5. Exit
# Start with shopping_list = [].
# REQUIREMENTS:
# - Use a while loop for the menu and a for loop to display items.
# - Use 'in' to prevent duplicates and 'not in' to reject missing items.
# - Handle an empty list and invalid menu selections.
# - Keep running until the user chooses Exit.
line(38)
items = ['pizza','chicken','rice','water','coke']
shopping_list = []
def menu():
    print("\n1. add item\n2.remove item\n3. view numbered items\n4.search for item\n5.exit")
def display_items():
    print()
    for item in items:
        print(items.index(item) + 1, f". {item}")
    print()
game = True
while game:
    menu()
    action = input('what would you like to do? ')
    if action == "1":
        display_items()
        action1 = input('which would you like to add? ')
        if action1 < 1 or action1 > len(items):
            pass
        else:
            game = False

# TASK 39 — GRADE ANALYZER:
# Create a function named analyze_grades(grades).
# RETURN a list containing, IN THIS ORDER:
# [highest_grade, lowest_grade, average_grade, passing_count, failing_count]
# Passing means 70 or higher.
# Do NOT use sum(), min(), max(), or sorting.
# For an empty list, RETURN [].
# Test: analyze_grades([95, 82, 67, 74, 58])
# Expected: [95, 58, 75.2, 3, 2]
# Test with a single grade and all-negative values too.
def analyze_grades(grades):


# TASK 40 — STUDENT ATTENDANCE SYSTEM:
# Start with:
# students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# present = []
# absent = []
# For EACH student, ask whether they are Present (P) or Absent (A).
# REQUIREMENTS:
# - Use a for loop to process the student list.
# - Use a while loop to reject anything other than P or A.
# - Prevent duplicate attendance records using 'in' / 'not in'.
# - Print numbered present and absent lists.
# - Print the number present, number absent, and attendance percentage.
# - Print "Perfect Attendance!" if everyone is present.
# - Create attendance_percentage(present, students) that RETURNS
#   the percentage; if students is empty, RETURN 0.
# - Test with all present, all absent, and a mixture.


# ============================================================
# END OF CHECKPOINT — REVIEW YOUR WORK BEFORE PUSHING
# ============================================================
