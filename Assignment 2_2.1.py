"""
a2_t1.card_came
XX-YYY-ZZZ
<Andre Bittencourt>
"""

import random

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def generate_deck(deck):

    """
    This method creates the initial card deck as a list with all possible combinations of suits and ranks.
    In contrast to the example on the lecture slides generating first all suits for a rank and continuing this for the next rank,
    start with generating first all ranks for a suit and continue with the next suit. We will test this order.
    You should represent each card as a list with three elements (strings) in the form ['rank of suit','suit','rank']
    e.g. ['2 of Clubs', 'Clubs', '2'] and ['Jack of Diamonds', 'Diamonds', 'Jack']. Add each card to the deck list,
    as a result the deck becomes a two-dimensional list with the cards being elements of the "outer" list and the
    attributes of an individual card being elements of the "inner" list.

    :param deck: an empty list
    :return: a list of all cards of the card deck generated according to the descriptions above
    """

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
#print(deck)

# Testing wether the list is 2-dimensional:
deck[0][1]

# creating cards to run the evaluation. Input in the function is going to be "card[number]"
card = deck

# all cards (possible inputs):
cards = []
for i in range(len(deck)):
    c = deck[i][0]
    c = f'"{c}" = card[{i}]'
    cards.append(c)
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

def store_score(deck):

    """
    This method is used to store the score assigned with each card in a new dictionary. We will call the calculate_score(card)
    method from here for each card of the deck (list) and store the card as key and its associated score as value in the dictionary.
    Use the first element of the "card" list as key for the dictionary. Dictionary entries will look like this: '2 of Clubs': 3
    and 'Jack of Diamonds': 13.

    :param deck: the deck of all cards
    :return: a dictionary of all cards and their individual scores, e.g. the card as key and its score as value
    """
        
    score_dict =  {}

    # changed the last term to run a forloop for all cards
    for card in range(len(deck)):
        
        # selecting each card and store it in key variable (until the end of the deck)
        key = deck[card][0]

        # assigning card as key through variable and value as it individual score
        score_dict[key] = calculate_score(deck[card])
        
        pass
    return score_dict

def shuffle(deck):

    """
    This method is used for shuffling a copy of the initial deck using the random.randrange() function (see lecture slides).

    :param deck: a copy the deck of all cards
    :return: the deck as list of shuffled cards
    """
    n = len(deck)
    for i in range(n):
        r = random.randrange(i, n)
        temp = deck[r]
        deck[r] = deck[i]
        deck[i] = temp
        pass
    return deck

# print(shuffle(deck))

def deal_cards(deck):
    
    """
    This method is used for dealing the cards of the shuffled deck to player1 and player2. Hand out the first ten cards
    in an alternating way to the decks of the players, i.e. player1 gets the cards with indices 0,2,4,6,8 and player2
    gets the cards with indices 1,3,5,7,9.
    Hint: use the modulus function '%' to determine whether the current list index is odd or even.

    :param deck: the deck of shuffled cards
    :return deck_player1: a deck of 5 cards from the shuffled cards for player 1 as list
    :return deck_player2: a deck of 5 cards from the shuffled cards for player 2 as list
    """
    deck_player1 = []
    deck_player2 = []
    
    # player 1: first iteration number = 1, second iteration number = 3 (not 2) so on
    for card in range(1,10,2):
        card = card
        card_player1 = deck[card]
        deck_player1.append(card_player1)

    # player 2:
    for card2 in range(0,10,2):
        card2 = card2
        card_player2 = deck[card2]
        deck_player2.append(card_player2)

    return deck_player1, deck_player2

#print(deal_cards(deck))

def play_round(card1,card2,score_dict):

    """
    This method is used for playing one round comparing two cards with each other based on their calculated score.
    Use the score_dict dictionary to look up the score for each card. Compare scores, if player1's score is larger than player 2's then
    he/she wins, analogous for player2, or there is a tie if both scores are equal. Return the result as an Integer with:
    1 means player 1 won, 2 means player 2, 0 means tie. Also, print the result of a round on the console in the form:
    Player 1: 5 of Clubs, score=6
    Player 2: Jack of Hearts, score=14
    Hint: use f-strings or the format() function for strings to create the output strings.

    :param card1: the current card of player 1
    :param card2: the current card of player 2
    :param score_dict: the dictionary of scores for all cards 
    :return: the result of playing one round as Integer (0, 1 or 2)
    """

    res = None

    card1 = card1
    card2 = card2

    print(card1)
    print(card2)
    print(score_dict[card1[0]])

    if score_dict[card1[0]] > score_dict[card2[0]]:
        res = 1
    
    elif score_dict[card2[0]] > score_dict[card1[0]]:
        res = 2
    
    else:
        res = 0

    return res

def play_game(deck1,deck2,score_dict):
    """
    This method is used for simulating a complete game consisting of playing all the cards on player1 and player2's decks,
    i.e. 1 card each in 5 rounds. Call the play_round() function for each round with card1, card2 and the score dictionary
    as input. Use the returned value of th play_round() function to evaluate the result of one round. Print if Player 1 or Player 2
    won the round or there was a Tie on the console.
    Also, keep track of the number of of wins for player 1, player 2 and ties. Similarly to playing one round, return
    the total result of the game, with total=1 meaning that player 1 has won, total=2 meaning that player 2 has won,
    and total=0 meaning nobody has won.
    Print the result of a complete game on the console in the form:
    The total score is: Player 1: 2, Player 2: 3, Ties: 0
    Player 2 wins the game.
    Hint: use the format() function to create the output strings.

    :param deck1: the card deck of player 1
    :param deck2: the card deck of player 2
    :param score_dict: the dictionary of scores for all cards 
    :return: the result of playing a game as Integer (0, 1 or 2)
    """

    wins1=0
    wins2=0
    ties=0
    for i in range(len(deck1)):
        #Your code here
        pass
    print('The total score is: Player 1: {}, Player 2: {}, Ties: {}'.format(wins1,wins2,ties))
    if(wins1>wins2):
        print('Player 1 wins the game.')
        total=1
    elif (wins1 < wins2):
        print('Player 2 wins the game.')
        total=2
    elif (wins1 == wins2):
        print('Nobody wins the game.')
        total=0
    return total

def main():
    """
    The main method to be executed.
    """

    #1. We generate a new card deck with all cards.
    card_deck = generate_deck([])

    #2. We calculate the individual scores of each card and store them in a dictionary.
    score_dict = store_score(card_deck)

    cont='y'
    while(cont=='y'):

        #3. We create a copy of the original card deck.
        shuffle_deck = card_deck.copy()

        #4. We shuffle the copied deck.
        shuffled_deck = shuffle(shuffle_deck)

        #5. We deal cards from the shuffled deck to player 1 and player 2.
        deck_player1,deck_player2 = deal_cards(shuffled_deck)

        #6. We play a game of cards.
        play_game(deck_player1,deck_player2,score_dict)

        cont = input('Play again? Enter "y" to play another round. Press any other key to quit.')

if __name__ == '__main__': main()


# The complete output on the console for one exemplary game would look like this:
# Player 1: 10 of Diamonds, score=12
# Player 2: 8 of Diamonds, score=10
# Player 1 wins
# Player 1: 7 of Hearts, score=10
# Player 2: 3 of Diamonds, score=5
# Player 1 wins
# Player 1: 2 of Hearts, score=5
# Player 2: 8 of Spades, score=12
# Player 2 wins
# Player 1: King of Spades, score=17
# Player 2: Jack of Clubs, score=12
# Player 1 wins
# Player 1: 3 of Spades, score=7
# Player 2: Ace of Clubs, score=15
# Player 2 wins
# The total score is: Player 1: 3, Player 2: 2, Ties: 0
# Player 1 wins the game.
