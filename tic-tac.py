#Working through "Automate the Boring Stuff with Python" by Al Sweigart
#Example / suggestion was to use a dictionary to simulate a tic-tac-toe board.
#The book's complete example is at http://inventwithpython.com/chapter10.html
#This is my own version.

import random

#dictionary to represent board, as described by book
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#displays the tic-tac board
def drawBoard():
  print(board['top-L'] + " | " + board['top-M'] + " | " + board['top-R'])
  print("--+---+--")
  print(board['mid-L'] + " | " + board['mid-M'] + " | " + board['mid-R'])
  print("--+---+--")
  print(board['low-L'] + " | " + board['low-M'] + " | " + board['low-R'])

#Checks to see if a space is clear
def isOpenSpace(space):
  return (board.get(space) == ' ')

#Computer will attempt a winning move
def tryToWin():
  #TO-DO
  print("To do: implement logic to attempt a winning move.")
  return False

#Computer will attempt to block the user from winning
def tryToBlock():
  #TO-DO
  print("To do: implement logic to block user's winning move.")
  return False

#Computer will randomly pic a cell
def placeRandomly():
  while True:
    #list(board.keys()) because dictionaries not indexed
    randLocation = random.choice(list(board.keys()))
    if isOpenSpace(randLocation):
      break
  board[randLocation] = 'X'

#Computer's turn (try to win, then try to block, then just place random)
def computerTurn():
  if isOpenSpace('mid-M'):
    board['mid-M'] = 'X'
    print("You didn't take the center? Okay...")
    drawBoard()
    return False
  if tryToWin():
    print("I win, you lose. Game over.")
    drawBoard()
    return True
  elif tryToBlock():
    print("I see what you did there...")
    drawBoard()    
    return False
  else:
    placeRandomly()
    print("Eh, this looks good.")
    drawBoard()
    return False

def userTurn():

  while True:
    uRow = input("Which row (top, mid, low)?")
    while ((uRow != 'top') and (uRow != 'mid') and (uRow != 'low')):
      uRow = input("Which row (top, mid, low)?")
      
    uCol = input("Which column (L, M, R)?")
    uCol = uCol.upper() #force uppercase
    while ((uCol != 'L') and (uCol != 'M') and (uCol != 'R')):
      uCol = input("Which column (L, M, R)?")
      uCol = uCol.upper() #force uppercase

    #if uCol is lowercase, isOpenSpace() doesn't work properly
    uSpace = uRow + "-" + uCol

    if isOpenSpace(uSpace):
      break

  board[uSpace] = 'O'
  drawBoard()

print("Starting the game.\n I'm playing 'X', you go first.")
for i in range(4):
  userTurn()
  if computerTurn() == True:
    break
