'''

  Program:  Name of Program
  File name:  main.py
  Files imported:  None
  Author:  name here
  Team:  MB Overloaders
  Date created:  2016/04/02
  Date last modified:  2016/04/02
  Version:  0.0.1

'''

#from help import *

# Begin Code

def startGame():
  displayIntro()
  gameInPlay = true
  
  while gameInPlay != false:
    printNow(gameInPlay)
    userChoice = 0
    
    userChoice = requestString("Enter your move")
    if userChoice.lower() == "exit":
      userChoice = requestString("Are you sure you want to quit, yes/no.")
      if userChoice.lower() == "yes":
        printNow("Sorry to see you go, Thank you for playing.")
        gameInPlay = false
      else:
        printNow("Keep having fun!")
    
    
    
    
  
  
def displayIntro():
  printNow("*** Welcome to Adventure Game ***")
  printNow("In each location you will be given directions you can move.")
  printNow("You will enter each comman into the input dialog box.")
  printNow("You\'ll be able to move north, south, east, west, up, and down.")
  printNow("Type \"help\" to display the help dialog.")
  printNow("Type \"exit\" to quit at any time.")