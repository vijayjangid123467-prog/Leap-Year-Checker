Leap Year Checker
Description:

>The Leap Year Checker is a simple Python program that determines whether a given year is a leap year or not. The user enters a year, and the program checks it using leap year rules before displaying the result.
>This project is ideal for beginners learning conditional statements, arithmetic operators, and user input handling in Python.

Features:
>Accepts a year as input from the user.
>Checks whether the year is a leap year.
>Displays the result instantly.
>Simple and beginner-friendly code.
>Requirements
>Python 3.x
Code Python:
>y = int(input("Enter year: "))
 
>if y % 400 == 0:
>print(f"{y} is a leap year.")
>elif y % 100 == 0:
>print(f"{y} is not a leap year.")
>elif y % 4 == 0:
>print(f"{y} is a leap year.")
>else:
>print(f"{y} is not a leap year.")

Note: In your original code, the elif y % 100 == 0 condition should print "not a leap year" because years divisible by 100 are not leap years unless they are also divisible by 400.

How to Run
>Save the code as leap_year_checker.py.
>Open a terminal or command prompt.
Run the program:
>Shell
>python leap_year_checker.py
>Enter a year when prompted.
>View the result.
>Example Output
Plain Text
Enter year: 2024
2024 is a leap year.
Plain Text
Enter year: 1900
1900 is not a leap year.
Plain Text
Enter year: 2000
2000 is a leap year.
Learning Concepts
User Input (input())
Type Conversion (int())
Conditional Statements (if, elif, else)
Modulus Operator (%)
Basic Problem Solving
Future Improvements
Allow checking multiple years in one run.
Add input validation.
Create a GUI version using Tkinter.
Display the next leap year automatically.
Author

Created as a beginner Python project to learn conditional statements and leap year calculations.
