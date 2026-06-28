from random import choice 
minip1 = ("Calculator",
"Joke generator","Shopping list program",
"Number guessing game","Password generator","Hello World / Name Generator",
    "Simple Calculator",
    "Guess the Number Game",
    "Mad Libs Generator",
    "Rock, Paper, Scissors Game",
    "Text-based Adventure Game",
    "Dice Rolling Simulator",
    "To-Do List CLI Application",
    "Password Generator",
    "Countdown Timer / Alarm Clock",
    "Unit Converter (Weight, Temp, Distance)",
    "Hangman Game",
    "Contact Book / Address Book",
    "Basic Web Scraper (using Beautiful Soup)",
    "Desktop Notification App",
    "Currency Converter (with a free API)",
    "Binary Search Algorithm Visualizer",
    "Simple Quiz Application",
    "Tic-Tac-Toe Game",
    "Expense Tracker (CSV or Text-file based)")
while True:
    project = input("Do you want project?\nEnter: yes/no  {").strip().lower()
    if project in ["y","yes"]:
                print(choice(minip1))
    elif project in ["n","no"]:
                break
    else:
         print(" In order to to run the program!\n","try","to enter [yes] or [no] else the program might not run")        