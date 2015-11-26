#Working through "Automate the Boring Stuff with Python" by Al Sweigart
#Example / suggestion was to use a dictionary to simulate a tic-tac-toe board.
#The book's complete example is at http://inventwithpython.com/chapter10.html
#This is my own version.

import random

#dictionary to represent board, as described by book
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#displays the tic-tac board
def drawBoard():
  print(board['top-L'] + " | " + board['top-M'] + " | " + board['top-R'])
  print("--+---+--")
  print(board['mid-L'] + " | " + board['mid-M'] + " | " + board['mid-R'])
  print("--+---+--")
  print(board['low-L'] + " | " + board['low-M'] + " | " + board['low-R'])

#Checks to see if a space is clear
def isOpenSpace(space):
  return board.get(space) == ' '

#Computer's turn (try to win, then try to block, then just place random)
def computerTurn():
  #Place random X
  while True:
    #list(board.keys()) because dictionaries not indexed
    randLocation = random.choice(list(board.keys()))
    if isOpenSpace(randLocation):
      break
  board[randLocation] = 'X'

  #Redisplay board
  drawBoard()
