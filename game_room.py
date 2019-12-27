##################################################################
# This program display a game menu:                              #
# 1. Make Change                                                 #
# 2. High Card                                                   #
# 3. Deal Hand                                                   #
# 4. Save Dream Hand                                             #
# 5. Display Dream Hand                                          #
# 6. Word Guess                                                  #
# Prompts user for option and plays                              #
# the game chosen.                                               #
#                                                                #
# Make Change: will read a purchase amount and a payment amount  #
# and display the change due and the breakdown of the change     #
# into number of dollars, quarters, dimes, nickels and pennies   #
#                                                                #
# High Card: will deal one card to each of two players, display  #
# who got which card and who wins                                #
#                                                                #
# Deal Hand: Will display a 5 card hand                          #
#                                                                #
# Save Dream Hand: Prompts for user input for dream hand and saves
# selection to .txt file                                         #
#                                                                #
# Display Dream Hand: displays card selection from Save Dream Hand
#                                                                #
# Word Guess: User guesses letters making up hidden word         #
##################################################################

import random
import Card

def main():
    # Constants for menu options
    MAKE_CHANGE = 1
    HIGH_CARD = 2
    DEAL_HAND = 3
    SAVE_DREAM_HAND = 4
    DISPLAY_DREAM_HAND = 5
    WORD_GUESS = 6
    QUIT = 7

    choice = menu_display()
    while choice != QUIT:
        if choice == MAKE_CHANGE:
            make_change()
        elif choice == HIGH_CARD:
            high_card()
        elif choice == DEAL_HAND:
            deal_hand()
        elif choice == SAVE_DREAM_HAND:
            save_dream_hand()
        elif choice == DISPLAY_DREAM_HAND:
            display_dream_hand()
        elif choice == WORD_GUESS:
            word_game()
            
        choice = menu_display()

def menu_display():
    # Display welcome message and program description
    print('\n**************************************************')
    print("*          Welcome to the Lame Game              *")
    print('**************************************************')
    print('* This program displays a game menu:             *')
    print('* 1. Make Change                                 *')
    print('* 2. High Card                                   *')
    print('* 3. Deal Hand                                   *')
    print('* 4. Save Dream Hand                             *')
    print('* 5. Display Dream Hand                          *')
    print('* 6. Word Guess                                  *')
    print('* 7. Quit                                        *')
    print('*                                                *')
    print('* Prompts for option and plays the game chosen.  *')
    print('**************************************************\n')

    try:
        # Display the menu and read the first option
        print("\nWelcome to Lame Game Room")
        print("-------------------------------------")
        print("1. Make Change")
        print("2. Play High Card")
        print("3. Deal Hand")
        print("4. Save Dream Hand")
        print("5. Display Dream Hand")
        print("6. Word Guess")
        print("7. Quit")
        choice = int(input("\nEnter Choice: "))
        
        while choice < 1 or choice > 7:
            
            print("Invalid option")
            print("-------------------------------------")
            print("1. Make Change")
            print("2. Play High Card")
            print("3. Deal Hand")
            print("4. Save Dream Hand")
            print("5. Display Dream Hand")
            print("6. Quit")
            choice = int(input("Choose again: "))
            
    #statement to handle potential raised error
    except ValueError:
        print("You must enter a number!")
        # Set choice to 0 because an error has occurred

        # Function must always return a value, even

        # if there were an error
        choice = 0
    except Exception as error_msg:
        # Set choice to 0 because an error has occurred

        # Function must always return a value, even

        # if there were an error
        print("Error:", erro_msg)
        choice = 0

    return choice


#############################################################

# Function:	make_change                                 #

# Inputs:	none                                        #

# Outputs:	none                                        #

# Description:	This function will read a purchase amount   #

#               and a payment amount and display the change #

#               due and the breakdown of the change into    #

#               number of dollars, quarters, dimes, nickels #

#               and pennies                                 #

#############################################################

def make_change():
    print("\n Make Change")
    print("------------")
    # Read the amount of the purchase
    price = float(input('\nEnter the amount of the purchase '))

    # Read the amount of the payment
    paid = float(input('Enter the amount of payment '))

    # Check to see if the payment is enough to cover the purchase
    if paid < price:
        print('You did not pay enough')
            
    else:

        # Calculate the change due
        change = paid - price

        # Display the change due
        print('\nChange due: ',format(change,'.2f'))
        #print('   unformatted: ',change)
        print('This breaks down into:')

        # Calculate the number of dollars due
        dollars = int(change//1)
        print('\tDollars:\t',dollars)

        # Isolate the change amount and convert it to an integer.
        # To account for precesion lost converting to an integer,
        # force rounding of the 100ths digit by adding .005
        # to the change portion
        change = int(((change - dollars) + .005)* 100)
        #print('change is now ',change)

        # Calculate the number of quaters due
        quarters = change // 25
        print('\tQuarters:\t',quarters)
        change = change - (quarters * 25)

        # Calculate the number of dimes due
        dimes = change // 10
        print('\tDimes:\t\t',dimes)
        change = change - (dimes * 10)

        # Calculate the number of nickels due
        nickels = change // 5
        print('\tNickels:\t',nickels)
        change = change - (nickels * 5)

        # The number of pennies due will be all that is left
        pennies = change
        print('\tPennies:\t',pennies)
        print()

        
#############################################################

# Function:	high_card                                   #

# Inputs:	none                                        #

# Outputs:	none                                        #

# Description:	This function will read the name of each of #

#               2 players deal 2 cards to each player and   #

#               determine who wins:                         #

#               the player with the highest card            #

#############################################################

def high_card():
    print("\n High Card")
    print("-----------")

    # Read each player's name
    player1 = input("What is your first name player one? ")
    player2 = input("What is your first name player two? ")

    # Create card objects
    player1_card = Card.Card()
    player2_card = Card.Card()

    #deal cards
    player1_card.deal()
    player2_card.deal()
    
    # Display face value of card for player 1
    print("Card for", player1, ": ", end=' ')
    player1_card.find_face_value()

    # Display face value of card for player 2
    print("Card for", player2, ": ", end=' ')
    player2_card.find_face_value()
    
    # Determine who won and display a message
    if player1_card.get_value() > player2_card.get_value():
        print("Contratulations ", player1, ", YOU WON!", sep='')
    elif player2_card.get_value() > player1_card.get_value():
        print("Contratulations ", player2, ", YOU WON!", sep='')
    else:
        print("The game is a draw; both cards are the same")


#############################################################

# Function:	deal_hand                                   #

# Inputs:	none                                        #

# Outputs:	none                                        #

# Description:	This function will deal a five card hand    #

#               using a random number function then         #

#               displays the face value of each card        #

#############################################################

def deal_hand():
    #empty list to hold cards
    hand = []
    
    #generate card objects and add them to list
    card1 = Card.Card()
    card1.deal()
    hand.append(card1)

    card2 = Card.Card()
    card2.deal()
    hand.append(card2)

    card3 = Card.Card()
    card3.deal()
    hand.append(card3)

    card4 = Card.Card()
    card4.deal()
    hand.append(card4)

    card5 = Card.Card()
    card5.deal()
    hand.append(card5)

    #display the cards
    print("The 5-card hand is:")
    display_hand(hand)

    hand_stats(hand)
    

def display_hand(hand):
    #display card values that are stored in list
    for card in hand:
        card.find_face_value()
        

def hand_stats(hand):
    #create accumulator variable
    total = 0

    #sum the total of the hand
    for card in hand:
        total += card.get_value()

    #average value of cards
    average = total // len(hand)

    print("The Card Value Average is:", average)


##############################################################

# Function:	save_dream_hand                              #

# Inputs:	none                                         #

# Outputs:	none                                         #

# Description:	This function get a file name from the user  #

#               and their favorite 5-card hand, and saves    #

#               the cards in the file.  The cards are given  #

#               by numeric value:                            #

#               Ace = 1                                      #

#               Two = 2 ... Ten = 10                         #

#               Jack = 11                                    #

#               Queen = 12                                   #

#               King = 13                                    #

##############################################################

def save_dream_hand():
    print("Save Dream Hand")
    print("------------------")
    dream_hand = []
    try:
        for card in range(1,6):
            card = int(input("Enter a numeric card value: "))
            while card < 1 or card > 13:
                print("Error: card must be between 1 and 13")
                card = int(input("Enter a numeric card value: "))
            #store hand in list
            dream_card = Card.Card()
            dream_card.set_value(card)
            dream_hand.append(dream_card)

        # Get file name from user
        file_name = input("Enter the file name to save your hand: ")
        outfile = open(file_name, 'w')

        # Write cards to file
        for card in dream_hand:
            outfile.write(str(card.get_value()))

        # Close file
        outfile.close()



    # Error trap for invalid value for card

    except ValueError:
        print("Error: Invalid input")

    except Exception as error_msg:
        print("Error:", error_msg)

    
##############################################################

# Function:	display_dream_hand                           #

# Inputs:	none                                         #

# Outputs:	none                                         #

# Description:	This function reads and displays the 5-card  #

#               hand stored in the file given by the user    #

#               and displays the face value of the card.     #                                                        #

##############################################################

def display_dream_hand():
    print("Display Dream Hand")
    print("---------------------")
    #request for dream hand file to be opened
    card_file = input("Enter the filename for your dream hand (.txt extension): ")

    #statements to handle exceptions
    try:
        #open requested file
        file = open(card_file,'r')

        dream_hand = []
        
        #read each line and display the value associated with the data
        
        for card in file:
            dream_card = Card.Card()
            dream_card.set_value(card)
            dream_hand.append(dream_card)
            
        print(dream_hand)
        display_hand(dream_hand)

        file.close()
    except IOError:
        print("An error occurred trying to read")
        print("the file:", card_file)


##############################################
#                                            #
#Function: word_game                         #
#                                            #
#inputs: none                                #     
#                                            #
#outputs: none                               #    
#                                            #
#Description: This function gets a word from #
#the user and gives the user unlimited tries #
#to input the correct letters to the word    #
#                                            #
##############################################

def word_game():
    print("----------------------")
    #get user input for word to be guessed
    word = input("Enter a word:\n")
    print("\n"*100)
    
    #asterisk string equal to the length of word
    word_hidden = '*' * len(word)

    #string to catch already guessed letters    
    guessed_letters = ''

    
    #while loop to prompt for user guesses
    #ends when only alphabetic characters in word_hidden
    while word_hidden.isalpha() == False:

        #prompt for user guess
        letter = input("Enter a letter: ")

        #check if letter already guessed
        if letter.lower() in guessed_letters.lower():
            print("You have already guessed that letter, try again!")

        #replace asterisk with letter according to index position
        elif letter.lower() in word.lower():
            
             word_lower = word.lower()
             letter_lower = letter.lower()
             
             #get index of letter in word
             index = word_lower.index(letter_lower)

             #replace asterisk with letter according to index
             word_hidden = word_hidden[:int(index)] + letter + word_hidden[int(index)+1:]
             print("Now you have:")            
             print(word_hidden)

             guessed_letters += letter

    print("CORRECT")

    
    
main()

        
    


