"""
Gemini said
Python’s datetime module is a classic "aha!" moment for students. It moves them away from treating dates as simple strings and into the world of objects and methods.

Here is a structured exercise you can give your students, ranging from basic retrieval to logic-based calculations.

Python Exercise: The "Time Traveler" Challenge
Part 1: The Basics
Goal: Import the module and extract specific components.

Current Stats: Write a script that prints the current date and time.

The Breakdown: From that current date, print only the Year, the Month, and the Day of the week (e.g., Monday).

Specific Date: Create a datetime object for January 1, 2000, at 12:00 PM.

Part 2: Formatting (The strftime Wizard)
Goal: Master the formatting codes.

Convert the current date into the following strings:

"MM/DD/YYYY" (e.g., 12/31/2025)

"Month Day, Year" (e.g., December 31, 2025)

"The current ISO week number is X."
"""
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.strftime("%A"))
print(x.strftime("%B"),x.strftime("%d"),x.strftime("%Y"),x.strftime("%X"),x.strftime("%p"))
z = datetime.datetime.now()
print(z.month,z.day,z.year)
print(z.strftime("%B"),z.day,z.year)
print("The current ISO week number is", z.strftime("%u"))