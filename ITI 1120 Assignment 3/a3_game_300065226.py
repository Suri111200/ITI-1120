import random

# Initializes game

def start_game(size_change):
    if size_change == "yes":
        num = int(input("Enter a number between 3 and 99 for the number of ranks: "))
        if num < 100 or num > 2:
            deck = make_deck(num)
            print("You are playing with a deck of ",num*4," cards.")
        else:
            deck = make_deck(13)
            print("You are playing with a deck of 52 cards.")
    else:
        deck = make_deck(13)
        print("You are playing with a deck of 52 cards.")

    deck = shuffle_deck(deck)

    return deck

#Rolls dice
def roll_dice():
    import random

    dice = random.randint(1,6)

    return dice
    
def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    
    '''
    #Adds one card for each suit for number specified
    deck = []
    for i in range(1,num+1):
        deck.append(100+i)
        deck.append(200+i)
        deck.append(300+i)
        deck.append(400+i)

    return deck
    

def shuffle_deck(deck):
    '''Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    import random

    random.shuffle(deck)

    return deck

def deal_cards_start(deck):
     '''(list of int)-> list of int

     Returns a list representing the player's starting hand.
     It is  obtained by dealing the first 7 cards from the top of the deck.
     Precondition: len(dec)>=7
     '''
    #Deals player 7 cards from top of deck
     player=[]

     for i in range(7):
         player.append(deck[len(deck)-1])
         del deck[len(deck)-1]

     return deck, player


def deal_new_cards(deck, player, num):

    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If  the number  of cards in the deck is less than num then then all the remaining cards are from the deck.
    Precondition: 1<=num<=6l deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    #Gives num new cards from deck to player
    if len(deck)< num:
        for i in range(len(deck)):
            player.append(deck[len(deck)-1])
            del deck[len(deck)-1]
    else:
        for i in range(num):
            player.append(deck[len(deck)-1])
            del deck[len(deck)-1]

def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    #Sort into ascending order
    hand.sort()
    numsort = hand

    #Sort based on final digit
    String = ''
    sort_order = [1,2,0]
    final_order = [2,0,1]
    splitted = []
    joined = []
    rearranged = []
    suitsort = []

    #Take each item in list, convert int (item) to str (String)
    #Split String and assign to list (splitted)
    #Rearrange contents in order [2,0,1],
    #Join as one element in new list "joined"
    for item in hand:
        String = str(item)
        splitted = list(String)
        rearranged = [splitted[i] for i in sort_order]
        joined.append(''.join(rearranged))

    #Sort into ascending order
    joined.sort()

    #Take each item in rearranged list (joined) and split into list(splitted)
    #Rearrange back to initial order
    #Convert back to integer
    #Append to final list(suitsort)
    for item in joined:
        splitted = list(item)
        rearranged = [splitted[i] for i in final_order]
        integer =''.join(rearranged)
        suitsort.append(int(integer))

    print("\n",numsort,"\n\n",suitsort)


def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    #Return False if card not in player
    for item in cards:
        if item not in player:
            print(item," is not in your hand. Invalid input")
            return False
    #Return True if all cards in player
    return True

def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    #Chack if 2 or more cards are provided
    if len(cards) < 2:
        print("Invalid meld. Discardable set needs to have at least 2 cards.")
        return False

    #For each card, find the modulo of 100 (to remove the suit value), then assess if it is same as modulo of 100 of first card 
    for i in range (1,len(cards)):
        if cards[i]%100 != cards[i-1]%100:
            print ("Invalid meld. ",cards[i]%100," is not the same value as ", cards[i-1]%100)
            return False
        
    #Return true if previous tests are passed
    return True
    


def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''
    #Test if 3 or more cards are in list
    if len(cards) < 3:
        print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
        return False
    #Sort cards numerically
    cards.sort()

    #Check if adjacent cards have a difference of 1. If not, return false
    for num in range(1, len(cards)):
        if cards[num] != (cards[num-1]+1):
            print("Invalid sequence. Cards are not of same suit.")
            return False
    #Return true if previous tests are passed
    return True
    
def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in the deck. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 

    '''
    complete = False

    print("Discard any card of your choosing.")

    #While loop repeats until a card that is within the deck is entered
    while complete == False:
        #Ask user which card they would like to discard
        discard_card = int(input("\nWhich card would you like to discard? "))
        #Check player if card entered is within deck
        for player_hand in player:
            #If it is, the card will be removed from player, and while loop will be exited
            if player_hand == discard_card:
                complete = True
                player.remove(player_hand)
        #If entered discard card not present in deck, card will be printed with error message. Loop will repeat
        if complete == False:
            print(discard_card,"\nNo such card in deck. Try again.")

    #If user exits loop, new hand with discard card removed will be printed
    print("Here is your new hand printed in two ways:")
    print_deck_twice(player)
            
    return player

def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid meld: 11 is not equal to 12
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''

    yesorno = ''
    #Continue asking question until input is yes or no
    while yesorno != "yes" and yesorno != "no":
        yesorno = input("Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? ")

    #if yes, ask which cards
    while yesorno == "yes":
        raw_input = input("Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space:").strip().split() 
        #Convert raw input to integers
        int_input = []
        for num in raw_input:
            int_input.append(int(num))
        int_input.sort()

        #Exit if cards are invalid
        if not is_valid(int_input, player):
            print()
        #if cards are valid, check if first 2 cards for sequence
        elif int_input[1]-1 == int_input[0]:
            #if true, then call function
            if is_discardable_seq(int_input):
                #if function returs true, remove appropriate cards
                for cards in int_input:
                    player.remove(cards)
                #Print deck in 2 ways
                print("Here is your new hand printed in two ways:")
                print_deck_twice(player)
        #If first 2 cards do not form sequence, test for melds
        elif is_discardable_kind (int_input):
            #if function returs true, remove appropriate cards
            for cards in int_input:
                player.remove(cards)
            #Print deck in 2 ways
            print("Here is your new hand printed in two ways:")
            print_deck_twice(player)
        #reset yesorno to continue while loop
        yesorno = ''
        while yesorno != "yes" and yesorno != "no":
            yesorno = input("Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? ")     

# main
print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()

deck = start_game(size_change)

deck, player = deal_cards_start(deck)

Round = 0

print ("Here is your starting hand printed in 2 ways: ")
print_deck_twice(player)

#Continue game until player hand has 0 cards
while len(player) > 0:
    #Increase round # each time while loop runs
    Round+=1
    print ("Welcome to round ",Round)
    #If length of deck above 0, roll dice
    if len(deck) > 0:
        roll = roll_dice()
        print ("Please roll the dice.\nYou rolled the dice and it shows: ",roll)
    #Else continue in empty deck phase   
    else:
        print ("The game is in empty deck phase")
        #Simulate dice roll of 1
        roll=1
    #Call rolled_one_round if roll is equal to 1
    if roll == 1:
        rolled_one_round (player)
    #Else add number of cards equal to die number to player hand, then call rolled_nonone_round
    else:
        print("\"Since you rolled,",roll, "the following", roll, "or", len(deck), "(if the deck has less than", roll, "cards) will be added to your hand from the top of the deck.\"")
        print("Here is your starting hand printed in two ways:\n")
        deal_new_cards(deck, player, roll)
        print_deck_twice(player)
        rolled_nonone_round(player)
    #Show user message stating round completed when done
    print("Round ",Round," completed.")

#Print ending message once user is out of cards
print("Congratulations, you completed the game in", Round, "rounds.")
  
