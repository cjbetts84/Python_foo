#Working through "Automate the Boring Stuff with Python" by Al Sweigart
#Example / suggestion was to use a dictionary to simulate a tic-tac-toe board.
#The book's complete example is at http://inventwithpython.com/chapter10.html
#This is my own version.

import random

#dictionary to represent board, as described by book
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#Lists describing rows, columns, and diagonal lines for blocks and wins
rows = [['top-L', 'top-M', 'top-R'],
        ['mid-L', 'mid-M', 'mid-R'],
        ['low-L', 'low-M', 'low-R']]
cols = [['top-L', 'mid-L', 'low-L'],
        ['top-M', 'mid-M', 'low-M'],
        ['top-R', 'mid-R', 'low-R']]
diags = [['top-L', 'mid-M', 'low-R'],
         ['top-R', 'mid-M', 'low-L']]

#Resets the board
def resetBoard():
  for k in list(board.keys()):
    board[k] = ' '

#Displays the tic-tac board
def drawBoard():
  print(board['top-L'] + " | " + board['top-M'] + " | " + board['top-R'])
  print("--+---+--")
  print(board['mid-L'] + " | " + board['mid-M'] + " | " + board['mid-R'])
  print("--+---+--")
  print(board['low-L'] + " | " + board['low-M'] + " | " + board['low-R'])

#Checks to see if a space is clear
def isOpenSpace(space):
  return (board.get(space) == ' ')

#Computer will attempt to place a winning move.
#If it can, it will return True as a flag to end the game
#If it cannot win, it will return False
def tryToWin():
  xCount = 0
  oCount = 0

  #Check for win on a row
  for r in rows:
    for s in r:
      if board.get(s) == 'X':
        xCount += 1
      elif board.get(s) == 'O':
        oCount += 1
      else:
        openSpace = s
    #end: for s in r

    if xCount == 2 and oCount == 0:
      board[openSpace] = 'X'
      return True #Able to win
    else:
      xCount = 0
      oCount = 0
      openSpace = None
  #end: for r in rows

  #Check for win on a column
  for c in cols:
    for s in c:
      if board.get(s) == 'X':
        xCount += 1
      elif board.get(s) == 'O':
        oCount += 1
      else:
        openSpace = s
    #end: for s in c

    if xCount == 2 and oCount == 0:
      board[openSpace] = 'X'
      return True #Able to win
    else:
      xCount = 0
      oCount = 0
      openSpace = None
  #end: for c in cols

  #Check for win on a diagonal
  for d in diags:
    for s in d:
      if board.get(s) == 'X':
        xCount += 1
      elif board.get(s) == 'O':
        oCount += 1
      else:
        openSpace = s
    #end: for s in d
        
    if xCount == 2 and oCount == 0:
      board[openSpace] = 'X'
      return True #Able to win
    else:
      xCount = 0
      oCount = 0
      openSpace = None
  #end for d in diagonals
      
  return False #Unable to win

#Computer will attempt to block the user from winning
#Returns True if able, False if it cannot
def tryToBlock():
  xCount = 0
  oCount = 0

  #Check to block user on a row
  for r in rows:
    for s in r:
      if board.get(s) == 'O':
        oCount += 1
      elif board.get(s) == 'X':
        xCount += 1
      else:
        openSpace = s
    #end: for s in r

    if xCount == 0 and oCount == 2:
      board[openSpace] = 'X'
      return True #Able to block
    else:
      xCount = 0
      oCount = 0
      openSpace = None
  #end: for r in rows

  #Check to block user on a column
  for c in cols:
    for s in c:
      if board.get(s) == 'O':
        oCount += 1
      elif board.get(s) == 'X':
        xCount += 1
      else:
        openSpace = s
    #end: for s in c

    if xCount == 0 and oCount == 2:
      board[openSpace] = 'X'
      return True #Able to block
    else:
      xCount = 0
      oCount = 0
      openSpace = None
  #end: for c in cols

  #Check for blocking a diagonal win
  for d in diags:
    for s in d:
      if board.get(s) == 'O':
        oCount += 1
      elif board.get(s) == 'X':
        xCount += 1
      else:
        openSpace = s
    #end: for s in d

    if xCount == 0 and oCount == 2:
      board[openSpace] = 'X'
      return True #Able to block
    else:
      xCount = 0
      oCount = 0
      openSpace = None
  #end: for d in diags
      
  return False  #Unable to block

#Computer will pick a corner cell
def takeCorner():
  corners = ['top-L', 'top-R', 'low-L', 'low-R']

  for i in range(4):
    c = random.choice(corners)
    if isOpenSpace(c):
      board[c] = 'X'
      return True #Placed a corner
    else:
      corners.remove(c) #So we don't try it again

  return False

#Computer will randomly pic a cell
def placeRandomly():
  #Loop until an open space is randomly chose
  while True:
    randLocation = random.choice(list(board.keys()))

    #Break from while True when open space is selected
    if isOpenSpace(randLocation):
      break
    
  board[randLocation] = 'X'

#Computer's turn...........
#Computer will try the following, in order, (1) take the center,
#(2) try to play a winning move, (3) try to block the user,
#(4) take an available corner, (5) place a random X.
def computerTurn():
  if isOpenSpace('mid-M'):
    board['mid-M'] = 'X'
    print("You didn't take the center? Okay...")
    drawBoard()
    return False 
  if tryToWin():
    print("I win, you lose. Game over.")
    drawBoard()
    return True #Signals game over
  elif tryToBlock():
    print("I see what you did there...")
    drawBoard()    
    return False
  elif takeCorner():
    print("Eh, this corner looks good.")
    drawBoard()
    return False
  else:
    print("Oh, what the hell..")
    placeRandomly()
    drawBoard()
    return False

#Checks if the user has won
#Returns True if user has three in a row
def hasWon():
  oCount = 0
  for r in rows:
    for s in r:
      if board.get(s) == 'O':
        oCount += 1
      else:
        oCount = 0
        break
    #end: for s in r

    if oCount == 3:
      return True #Signals game over
  #end: for r in rows

  for c in cols:
    for s in c:
      if board.get(s) == 'O':
        oCount += 1
      else:
        oCount = 0
        break
    #end: for s in c

  if oCount == 3:
    return True #Signals game over
  #end: for c in cols

  for d in diags:
    for s in d:
      if board.get(s) == 'O':
        oCount += 1
      else:
        oCount = 0
        break
    #end: for s in d

    if oCount == 3:
      return True #Signals game over
  #end: for d in diags
    
  return False

#User's turn............
#The user will be prompted to enter a row and column to place a mark.
#The user will continue to be prompted if the space chosen is unavailable
#or if the input is invalid.
def userTurn():
  #Loop for user choosing an open space
  while True:
    uRow = input("Which row (top, mid, low)?")
    uCol = input("Which colum (l, m, r)?")
    uSpace = uRow + "-" + uCol.upper()
    if uSpace not in board:
      print("I don't understand...")
    else:
      if not isOpenSpace(uSpace):
        print("That space is already used.")
      else:
        break

  board[uSpace] = 'O'
  drawBoard()

#Main game loop.........
#Each player gets at most four turns before the game would end
#as a draw or win/lose. If either userTurn() or computerTurn()
#return True, that signals they have won the game, and the loop
#will break.
def game():
  print("Starting the game.\n I'm playing 'X', you go first.")
  for i in range(4):
    if userTurn():
      break
    if computerTurn():
      break
  resetBoard()
