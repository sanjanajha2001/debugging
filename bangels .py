import random
def getSecretNum(numDigits):
# Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
      secretNum += str(numbers[i])
  print(secretNum)  
  return (secretNum)

def getClues(guess, secretNum):
# Returns a string with the pico, fermi, None clues to the user.
  if guess == secretNum:
    return 'You got it!'
  clue = []
  for i in range(len(secretNum)):
    if guess[i] in secretNum[i]:
      clue.append('Fermi')
    elif guess[i] in secretNum:
      clue.append('Pico')
    else:
        clue.append("none")
      # return 'None'
  return ' '.join(clue)

def isOnlyDigits(num):
# Returns True if num is a string made up only of digits. Otherwise returns False.
  if num == '':
    return False
  for i in num:
    if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return False

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
  play = input("Do you want to play again? Yes or No?") 
  return play.lower()

NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' % (MAXGUESS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')

while True:
  secretNum = getSecretNum(NUMDIGITS)
  print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
  numGuesses = 1
  # guess = input("Guess Again")
  while numGuesses <= MAXGUESS:
        guess = input("Guess again")
        if len(guess)==NUMDIGITS:
          clue=getClues(guess,secretNum)
          print(clue)
          numGuesses += 1
          if guess == secretNum:
            break
          if numGuesses > MAXGUESS:
            print("you are run out of guesses.the answer was"+secretNum)
  # play = input("Do you want to play again? Yes or No?")
  if playAgain ()=="yes":
      continue
  else:
      break