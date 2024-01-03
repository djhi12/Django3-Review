
# Variables:
# Example of creating variables
name = "John"
age = 25
height = 1.75
is_student = True


# Strings:
# Example of strings
name = "John"
message = 'Hello, ' + name + '!'


# Integers:
# Example of integers
age = 25
number_of_students = 100


# Print Statement:
# Example of using the print statement
name = "John"
age = 25
print("Name:", name)
print("Age:", age)


# Combining variables and strings in the print statement:
# Printing a combination of strings and variables
name = "John"
age = 25
print("My name is", name, "and I am", age, "years old.")


# Sample Program
# Sample program to get user input and print a personalized message

# Get user input for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert the input to an integer

# Print a personalized message
print("Hello, " + name + "!")
print("You are", age, "years old.")

# Check if the user is eligible to vote (assuming voting age is 18)
if age >= 18:
    print("You are eligible to vote. Exercise your right!")
else:
    print("You are not eligible to vote yet. Wait until you turn 18.")
