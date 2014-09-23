"""Created by Joy Kimmel
9/16/2014: Rock, Paper, Scissors, Lizard, Spock """

#imports needed packages
import random
import numpy as np

#runs the game rock, paper, scissors, lizard, spock
#asks for entry by user
#prints both the user's and computer's choice, and annouces the winner (or says its a tie)
#asks user to play again or to quit
#also records win/ loss record and prints it out every time
def lets_play():
    
    #dictates whether or not user wants to play again, intialized at True so game will start
    play_again = True
    #records the users win record, intialized at 0
    win_record = 0
    #records the number of games the user has played, intialized at 0
    game_number = 0
    
    #while loop, when play_again is True the code enters the loop, when it is False the code quits the game and does not enter the loop
    while play_again is True:
        
        #asks user for their choice
        usr_input = raw_input("Please enter your choice (Rock, Paper, Scissors, Lizard, or Spock): ")       
        usr = usr_input.lower()
        
        #if the user has made of the correct 5 options, the game continues into this if loop
        if usr in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
            
            #adds a game played to the number of games already played
            game_number = game_number + 1
            
            #chooses a random number either 0,1,2,3 or 4 (and does not choose 5)
            random_number = random.randrange(0,5)
            
            #list of options for both the computer and user ~ to be used in both determining what the computer plays and well as the winner
            options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
            
            #determines the computers' play by finding the randomly generated position in the options list 
            computers_play = options[random_number]
            
            #prints out the two player's choices'
            print "You played: %s" % (usr)
            print "Computer played: %s" % computers_play
            
            #finds the position number associated with each player's choices to be used in determining the winner
            user_num = options.index(usr)
            computer_num = options.index(computers_play)
            
            #an array of 0, 1, 2 ( rows are users ~ in the same order as options list, and columns are computers ~ in the same order as options list)
            # 0 = user loses to computer
            # 1 = user wins
            # 2 = user and computer ties (because of the same entry)
            winners_array = np.array([[2,0,1,1,0],[1,2,0,0,1],[0,1,2,1,0],[0,1,0,2,1],[1,0,1,0,2]])
           
            #finds the 0, 1, or 2 associated with this specific game
            winning_number = winners_array[user_num][computer_num]
            
            #prints out the winner based off of what nummber was found in the array
            if winning_number == 0:
                print "The computer wins!"
            
            elif winning_number == 1:
                win_record = win_record+1
                print "You win!"
            
            else:
                print "Tie game!" 
            
        #this loop is entered when users enter an invalid entry
        else:
            print "ERROR: Incorrect entry, please play again"
        
        #asks users if they want to keep playing
        keep_playing = raw_input("Do you want to play again? (please answer yes (y) or no (n)): ")
        
        #if the user's entry decision is yes, returns how many wins out of how many games the user has won and continues through the while loop again
        if keep_playing.lower() in ['yes', 'y']:
            print "You've won %s out of %s games." % (win_record, game_number)
            play_again = True
        
        #if the user's entry is anything else, returns how many wins out of how many games the user won and terminates the program
        else:
            print "Thanks for playing! - You won %s out of %s games." % (win_record, game_number)
            play_again = False
    
    
lets_play()
