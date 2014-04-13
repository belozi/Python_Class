# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
target_number = 0
guesses = 0

# helper function to start and restart the game
def new_game():
    f.start()
    range100()

# define event handlers for control panel
def range100():
    
    global target_number
    global guesses

    # button that changes range to range [0,100) and restarts
    target_number = random.randrange(0, 101)
    guesses = 7
    
    print " "
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is ", guesses   

def range1000():
    
    global target_number
    global guesses
    # button that changes range to range [0,1000) and restarts
    target_number = random.randrange(0, 1001)
    guesses = 10
   
    print " "
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is ", guesses
    
def input_guess(guess):
    global target_number
    global guesses
    guess = int(guess)
    guesses -= 1
    
    print " "
    print "Guess was ", guess
    print "number of remaining guesses is ", guesses
    
    if guess < target_number:
        print "Higher!"       
    elif guess > target_number:
        print "Lower!"
    else:
        print "You win"
    
    if guesses <= 0:
        print "You have lost."
        new_game()
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
new_game()


