# -*- coding: utf-8 -*-
"""
Name: Emily Ramirez
Kerberos: emilyram
Section: 5
"""
import random

VALUES = {"a":1, "b": 3, "c": 3, "d": 2, "e": 1, "f":4, "g": 2, "h":4,
          "i":1, "j":8, "k":5, "l":1, "m":3, "n":1, "o": 1, "p": 3, "q":10, 
          "r":1, "s":1, "t":1, "u": 1, "v": 4, "w":4, "x":8, "y":4, "z":10}

# HELPER FUNCTIONS
def load_valid_words(filename):
    """
    Loads words from a desired textfile into a list. These are the only
    valid words in the game.
    
    Inputs: filename (str) the .txt file you would like to pull words from
    
    Returns: a list of the words in the .txt file.
    """
    words = []
    with open(filename) as f:
        words = f.readlines()
    for i, word in enumerate(words):
        words[i] = word.strip()
    return words
    
def get_hand():
    """
    Gets a random hand for the player to use, containing
    four consonants and 2 vowels
    
    Returns: dict, mapping letter to number of times 
             it appears in the hand
    """
    my_hand = {}
    for i in range(2):
        new_letter = random.choice("aeiou")
        if new_letter in my_hand:
            my_hand[new_letter] += 1
        else:
            my_hand[new_letter] = 1
    for i in range(4):
        new_letter = random.choice("bcdfghjklmnpqrstvwxyz")
        if new_letter in my_hand:
            my_hand[new_letter] += 1
        else:
            my_hand[new_letter] = 1
    return my_hand

# END OF HELPER FUNCTIONS
# DO NOT CHANGE ANYTHING ABOVE THIS LINE

playable_words = load_valid_words("words.txt")
the_hand = get_hand()

def update_hand(word, hand):
    """
    Updates the hand based on the word the user played.
    The player should "use up" a letter in their hand when that 
    letter is in the word that the user has played.
    
    Inputs: word (str) The word that the user has played
            hand (dict {str:int}) The player's current hand
    
    Returns: nothing
    """
    for letter in word:
        hand[letter] = hand[letter] - 1
        if hand[letter] == 0:
            del hand[letter]  
    

def calc_word_score(word):
    """
    Calculates the score of the word that the user has played
    
    Inputs: word (str) The word that the user has played
    
    Returns: the score that the word earns (int)
    """
    score = 0    
    for letter in word:
        score += VALUES[letter]
    return score
  
def print_hand(hand):    
    """
    The function takes the player's hand and prints it in a friendly to read format
    by returning a string.
    
    Input: hand (dict) the hand the player was dealt
    
    Returns: The hand described as a string
    """
    string = ""
    for letter in hand:
        string = string + (letter + " ") * hand[letter]    
    print "Here is your hand:", string    

def is_valid_word(orig_hand, user_play, valid_words):    
    hand_copy = orig_hand.copy()  
    try: 
        update_hand(user_play, hand_copy)
    except KeyError:
        return False
    if user_play not in valid_words:
        return False
    return True
    
if __name__ == "__main__":

#Step 1: Draw a hand.
#Step 2: Play a word.
    #Show the new hand, show the score.
#Step 3: Ask if they would like to keep playing.
    #Check for valid play, loop.

#playable_words = load_valid_words("words.txt") already implemented
#the_hand = get_hand() already implemented

    total_score = 0
    print "Welcome to Scrabble!"
    
#    def active_play(player_move):
#        active = True
#        if player == "N":
#            active = False
#        if player != "Y" and player != "N":
#            player = raw_input("Would you like to play a hand? Y or N ")
#        return active
        
    active = True
    while active == True:
        player = raw_input("Would you like to play a hand? Y or N ")
        if player == "N":
            active = False
            break
        if player != "Y" and player != "N":
            player = raw_input("Would you like to play a hand? Y or N ")

        print_hand(the_hand)
        word_played = raw_input("What word would you like to play? ")
        valid = is_valid_word(the_hand, word_played, playable_words)
        if valid == False:
            print "That's not a valid move."
            continue            
        
        print "The word is", calc_word_score(word_played), "points."
        total_score += calc_word_score(word_played)
        print "Your total score is", total_score, "points."
        update_hand(word_played, the_hand)
    
    print "Your final score is", total_score, "points."
    
#    Once you have thought about your game design and come 
#    up with an implementation plan, add your name to the Checkoff Queue. 
#    Be prepared to talk an LA about what your design/plan is, what Python 
#    structures you think you will use, what information you will have to 
#    print for the user, what variables you might need, when your game would end, etc.
    
#    def new_hand():
#    """
#    Gets a random hand for the player to use, containing
#    four consonants and 2 vowels
#    
#    Returns: dict, mapping letter to number of times 
#             it appears in the hand
#    """
#    my_hand = the_hand
#    while len(my_hand) < 6:    
#        for i in range(2):
#            new_letter = random.choice("aeiou")
#            if new_letter in my_hand:
#                my_hand[new_letter] += 1
#            else:
#                my_hand[new_letter] = 1
#        for i in range(4):
#            new_letter = random.choice("bcdfghjklmnpqrstvwxyz")
#            if new_letter in my_hand:
#                my_hand[new_letter] += 1
#            else:
#                my_hand[new_letter] = 1
#    return my_hand
#    
#    
#    
#    
#    
#    