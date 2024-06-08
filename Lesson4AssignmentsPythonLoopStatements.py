# Lesson 4: Assignments | Python Loop Statements
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!
# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!
# ________________________________________
# 1. The Range Riddle

# Objective: The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. You will correct a code snippet, simulate moods for different days, and create a countdown timer.

# Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.
# days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
program_days_of_week = []
for i in range(len(days_of_week)):
    if i%2 == 0:
        program_days_of_week.append(days_of_week[i])

print(program_days_of_week)



# 2. Loop Condition Logic
# Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.


# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).
while True:  # Infinite loop
    answer = input("Type 'exit' to stop: ")
    if answer.lower() == 'exit':
        print("Exiting the loop.")
        break  # exit
    else:
        print("You typed:", answer)

# Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)
i = 0
while i < 5:  # Loop continues as long as i is less than 5
  print("This is iteration", i)
  i += 1  # Increment the control variable after each iteration
print("Loop completed!") 




# ________________________________________

# 4. Python's Random Game Night (EXTRA CREDIT)
# Objective: The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.
# Task 1: Random Choice Game Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.

import random

# Define a list of items
print("You've won one of the following prizes. laptop, prize, car, job. ")
items = ["laptop", "prize", "car", "job"]

# Randomly select an item from the list
select_item = random.choice(items)

# Game loop (continues until the player guesses correctly)
while True:
  # Get the player's guess
  guess = input("Guess the item: ").lower()

  # Check if the guess matches the chosen item
  if guess == select_item:
    print("Congratulations! You guessed the item correctly.")
    break  # Exit the loop if the guess is correct
  else:
    print("No. Try again.")

print("Thanks for playing!")