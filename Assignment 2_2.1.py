import random

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def generate_deck(deck):

    if deck == []:
        for suit in SUITS:
            for rank in RANKS:
                    card = [rank + ' of ' +  suit, suit, rank]
                    # brackets needed to create two dimensional list!
                    deck += [card]
    
    else:
        print('Please enter "deck" in the generating function')
   
    return deck

deck = []
generate_deck(deck)

# first index: deck position
# second index: card position
# print(deck[9][0])

"""
doesnt work like R: we need to run for loops to append stuff
card.append(deck[0:][0])
"""

# testing enumerator suits
"""
for card_clubs in range(0,13):
    deck[card_clubs][1] = 1

print(deck)
"""
# testing enumerator special cards
"""
lj = [9, 22, 35, 48]
for jacks in lj:
    deck[jacks][2] = 11
print(deck)

lq = [10, 23, 36, 49]
for queens in lq:
    deck[queens][2] = 12
print(deck)

lk = [11, 24, 37, 50]
for kings in lk:
    deck[kings][2] = 13
print(deck)

la = [12, 25, 38, 51]
for aces in la:
    deck[aces][2] = 14
print(deck)
"""
# defining card to call the function and create all possible cards and pasting it to orientation
card = []
for i in range(len(deck)):
    c = deck[i][0]
    c = f'"{c}" = card[{i}]'
    card.append(c)
# print(*card, sep= '\n')

"""
"2 of Clubs" = card[0]
"3 of Clubs" = card[1]
"4 of Clubs" = card[2]
"5 of Clubs" = card[3]
"6 of Clubs" = card[4]
"7 of Clubs" = card[5]
"8 of Clubs" = card[6]
"9 of Clubs" = card[7]
"10 of Clubs" = card[8]
"Jack of Clubs" = card[9]
"Queen of Clubs" = card[10]
"King of Clubs" = card[11]
"Ace of Clubs" = card[12]
"2 of Diamonds" = card[13]
"3 of Diamonds" = card[14]
"4 of Diamonds" = card[15]
"5 of Diamonds" = card[16]
"6 of Diamonds" = card[17]
"7 of Diamonds" = card[18]
"8 of Diamonds" = card[19]
"9 of Diamonds" = card[20]
"10 of Diamonds" = card[21]
"Jack of Diamonds" = card[22]
"Queen of Diamonds" = card[23]
"King of Diamonds" = card[24]
"Ace of Diamonds" = card[25]
"2 of Hearts" = card[26]
"3 of Hearts" = card[27]
"4 of Hearts" = card[28]
"5 of Hearts" = card[29]
"6 of Hearts" = card[30]
"7 of Hearts" = card[31]
"8 of Hearts" = card[32]
"9 of Hearts" = card[33]
"10 of Hearts" = card[34]
"Jack of Hearts" = card[35]
"Queen of Hearts" = card[36]
"King of Hearts" = card[37]
"Ace of Hearts" = card[38]
"2 of Spades" = card[39]
"3 of Spades" = card[40]
"4 of Spades" = card[41]
"5 of Spades" = card[42]
"6 of Spades" = card[43]
"7 of Spades" = card[44]
"8 of Spades" = card[45]
"9 of Spades" = card[46]
"10 of Spades" = card[47]
"Jack of Spades" = card[48]
"Queen of Spades" = card[49]
"King of Spades" = card[50]
"Ace of Spades" = card[51]
"""

# creating cards to run the evaluation
card = deck

def calculate_score(card):
    """
    This method is used to calculate the score of a card. The score is calculated based on the card's suit (2nd element
    of the list) and it's rank (3rd element of the list). The score is the sum of the points for the suit and the rank.
    For the suits the following points should be assumed: Clubs = 1, Diamonds = 2, Hearts = 3, Spades = 4.
    For the ranks the following points should be assumed: 1 = 1, 2 = 2, ..., 10 = 10, Jack = 11, Queen = 12, King = 13, Ace = 14.
    Hint: Use the int() method to convert the string representing a numerical rank of a card directly into an integer,
    e.g., int('2') = 2

    :param card: the card as a list with three elements (strings) in the form ['rank of suit','suit','rank']
    :return: the total score of a card as sum of its rank and suit
    """

    suit=card[1]
    rank=card[2]
    card_score = None
    
    """
    # enumerating suits
    for card_clubs in range(0,13):
        deck[card_clubs][1] = 1

    for card_diamonds in range(14,26):
        deck[card_diamonds][1] = 2 

    for card_hearts in range(27,39):
        deck[card_hearts][1] = 3
    
    for card_spades in range(40,52):
        deck[card_spades][1] = 4
    
    # enumerating special cards
    ## Jack with position list
    lj = [9, 22, 35, 48]
    for jacks in lj:
        deck[jacks][2] = 11

    ## Queen with position list
    lq = [11, 24, 37, 50]
    for queens in lq:
        deck[queens][2] = 12

    ## King with position list
    lk = [11, 24, 37, 50]
    for kings in lk:
        deck[kings][2] = 13

    ## Ace with position list
    la = [12, 25, 38, 51]
    for aces in la:
        deck[aces][2] = 14
    """

    if card[1] == 'Clubs':
        suit = 1
    
    elif card[1] == 'Diamonds':
        suit = 2
    
    elif card[1] == 'Hearts':
        suit = 3
    
    elif card[1] == 'Spades':
        suit = 4

    if card[2] == 'Jack':
        rank = 11
    
    elif card[2] == 'Queen':
        rank = 12

    elif card[2] == 'King':
        rank = 13

    elif card[2] == 'Ace':
        rank = 14

    card_score = suit + int(rank) 

    return card_score


print(calculate_score(card[0]))
print(calculate_score(card[49]))
