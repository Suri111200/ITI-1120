from random import shuffle

class Blackjack:

#Dictionary assigns values to cards
 values={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
  
 def play(self):
    #Method initilizes game
    #GameOfCards object assigned to d
    #This initilizes a new deck
  d = GameOfCards()
    #Shuffle Deck
  d.mix()
      #Call 2 instances of "main" 2 initialize 2 players
      #This creates variables named 'Bank' and 'Player' with empty lists for their hands
  bank = Main('Bank')
  player = Main('Player')

  # gives two cards to the player and two to the bank
  for i in range(2):
      #Calls "addcard" in "Main", parameter is calling "getCard" method from "GameofCards" class
    player.addCard(d.getCard())
    bank.addCard(d.getCard())

  # show the hands of bank and player
  bank.showMain()
  player.showMain()

  # as long as the player ask for a Card!, The bank gets cards
  response = input('Card? Oui or non? (By default oui) ')
  while response in ['','o','O','oui','Oui']:
    c = d.getCard()
    print("You have:")
    print(c)
    player.addCard(c)

    #Call "total" method in "play" class
    if self.total(player) > 21:
       print("You have passed 21. You have lost.")
       return   
    response = input('Card? Oui or non? (by default oui) ')

  # the bank play with those rules  
  while self.total(bank) < 17:
    c = d.getCard()
    print("The bank has:")
    print(c)
    bank.addCard(c)
    if self.total(bank) > 21:
       print("The bank has passed 21. You have won.")
       return

  # if 21 is has not been passed, compare the hands to find the winner  
  self.compare(bank, player)

      
 def total(self, person):
    ''' (Main) -> int
    calculate the sum of all the cards' values in the hand
    '''
    #Have to be able to evaluate card as integer (haven't figured out hwo to do that)
    #Everything until this works

    sums = 0
    for i in range(len(person.Cards)):
        print(i)
        ################# DOESN'T WORK
        print(repr(person.Cards[i]))
        sums= sums+ person.Cards[i] in values
        print(sums)
    print(person.Cards)
    
#    return sum(cards)

 def compare(self, bank, player):
    ''' (Main, Main) -> None
    Compare the main of the player with the hand of the bank
    et affiche de messages
    '''
    #Calls "total" method to determine sum of all cards for both players
    banksum = self.total(bank)
    playersum = self.total(player)

    #Determine which player has the higher sum, print messages accordingly

    ####HAS NOT BEEN TESTED
    if banksum > playersum:
        print("You have lost.")
    elif playersum > banksum:
        print("You have won.")
    else:
        if ('A' in bank) and any(item in bank for item in ('10','J','Q','K')) and not(('A' in player) and any(item in player for item in ('10','J','Q','K'))):
            print("You have lost.")
        elif ('A' in player) and any(item in player for item in ('10','J','Q','K')) and not(('A' in bank) and any(item in bank for item in ('10','J','Q','K'))):
            print("You have won.")
        else:
            print("Equality.")

    # if the total of the bank > the total of the player display 'You have lost.'

    # ifthe total of the bank < the total of the player display 'You have won.'   

    # in case of equality, if the total is 21m if tha bank has a blackjack
    # display 'You have lost.'; if the playerer has a blackjack 'You have won.' 
    # otherwise, display 'Equality.'

#Main means HAND in French, to avoid confusion       
class Main(object):
    '''represents a main of cards to play'''

    def __init__(self, player):
        '''(Main, str)-> none
        initializes the player's name and the card list with list being empty'''
        self.player = player
        self.Cards=[]
        #Complete

    def addCard(self, card):
        '''(Main, Card) -> None
        add a card to the hand'''
        self.Cards.append(card)
        
        # Completed

    def showMain(self):
        '''(Main)-> None
        display the player's name and the hand'''
        print(self.player,":",self.Cards)
        # Completed
                
    def __eq__(self, other):
        '''returns True if the hands have tyhe same cards in the same order'''
        
        # to be completed

    def __repr__(self):
        '''returns a representation of the object'''
        
        # tp be completed

class Card:
    '''represente a card to play'''

    def __init__(self, value, color):
        '''(Carte,str,str)->None        
        initializes the value and the color of the card'''
        self.value = value
        self.color = color  # spade, heart, club or diamond

    def __repr__(self):
        '''(Carte)->str
        returns the representation of the object'''
        return 'Card('+self.value+', '+self.color+')'

    def __eq__(self, other):
        '''(Card,Card)->bool
        self == other if the value and color are the same'''
        return self.value == other.value and self.color == other.color

class GameOfCards:
    '''represente the game of 52 cards'''
    # values and colors are variables of class
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    colors = ['\u2660', '\u2661', '\u2662', '\u2663']
    # colors is a set of 4 symbols Unicode that represents the 4 colors
    # spade, heart, club ou diamond
    
    def __init__(self):
        'initializes the packet of 52 cards'
        self.packet = []          # packet is empty at the start
        for color in GameOfCards.colors: 
            for value in GameOfCards.values: # variables of the class
                # add a card of value and color
                self.packet.append(Card(value,color))

    def getCard(self):
        '''(GameOfCards)->Card
        distribute a card, the first from the packet'''
        return self.packet.pop()

    def mix(self):
        '''(GameOfCards)->None
        to mix the card game'''
        shuffle(self.packet)

    def __repr__(self):
        '''returns a representation od the object'''
        return 'Packet('+str(self.packet)+')'

    def __eq__(self, other):
        '''return True if the packets are the same cards in the same order'''
        return self.packet == other.packet
    
    
b = Blackjack()
b.play()

