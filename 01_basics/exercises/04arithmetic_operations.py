"""
Write a program which asks the user for a number.
The program then prints out the number multiplied by five.
Example:
    Please type in a number: >> 7
    7 times 5 is 35
"""
number_type = 7 * 5

print(f"Please type in a number: {number_type}")


"""
Write a program which asks the user for their name and year of birth.
The program then prints out a message as follows:
    What is your name? >> Frances Fictitious
    Which year were you born? >> 1990
    Hi Frances Fictitious, you will be 34 years old at the end of the year 2024
"""
name = input("What is your name?")
birth_year = input("Which year were you born?")
age = 2024 - int(birth_year)

print(f"Hi {name}, you will be {age} years old at the end of the year 2024 ")
"""
Write a program which asks the user for a number of days.
The program then prints out the number of seconds in the amount of days given.
Example:
    How many days? >> 7
    Seconds in that many days: >> 604800
"""
days_in_number = input("How many days?")
seconds_in_days = 60 * int(days_in_number)

print(f"Seconds in that many days: {seconds_in_days}")



"""
This program asks the user for three numbers.
The program then prints out their product, that is, the numbers multiplied by each other.
There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it.
Please fix it.
"""
# Fix the code
number3 = int(input("Please type in the first number: "))
number7 = int(input("Please type in the second number: "))
number8 = int(input("Please type in the third number: "))

product = number3 * number7 * number8

print("The product is", product)


"""
Write a program which asks the user for four numbers.
The program then prints out the sum and the mean of the numbers.
Example:
    Number 1: >> 2
    Number 2: >> 1
    Number 3: >> 6
    Number 4: >> 7
    The sum of the numbers is 16 and the mean is 4.0
"""
# Write your solution here


"""
Write a program that asks the user for a three-digit number input.
Reverse the given number by using modulo and division operator.
Example:
    Enter a number: >> 123
    The reversed number is: >> 321
"""
# Write your solution here
