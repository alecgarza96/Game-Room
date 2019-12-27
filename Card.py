#Class name: Card
#Data Attributes: __value
#Methods:
#__init__()
#deal()
#set_value()
#get_value()
#find_face_value()
#__str__()
import random

class Card:

    #initialize self parameter
    def __init__(self):
        self.__value = 0

    #generate random value to simulate card dealt
    def deal(self):
        self.__value = random.randint(1,13)

    #set value according to card argument
    def set_value(self, card):
        self.__value = card

    #retrieve value referenced by self
    def get_value(self):
        return self.__value
    #assign numeric value to card value
    def find_face_value(self):
        if self.__value == 1:
            print("Ace")
        elif self.__value == 2:
            print("Two")
        elif self.__value == 3:
            print("Three")
        elif self.__value == 4:
            print("Four")
        elif self.__value == 5:
            print("Five")
        elif self.__value == 6:
            print("Six")
        elif self.__value == 7:
            print("Seven")
        elif self.__value == 8:
            print("Eight")
        elif self.__value == 9:
            print("Nine")
        elif self.__value == 10:
            print("Ten")
        elif self.__value == 11:
            print("Jack")
        elif self.__value == 12:
            print("Queen")
        elif self.__value == 13:
            print("King")
        else:
            # This will catch any
            # invalid card value
            print("Invalid card")

    def __str__(self):
        return self
            
        
