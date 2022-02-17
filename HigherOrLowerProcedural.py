# Higher or Lower

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

# Main code
print('\nWelcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower'
      'than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.\n')

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True: # play multiple games
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']

    print(f'\nStarting card is: {currentCardRank} of {currentCardSuit}\n')

    for cardNumber in range(0, NCARDS): # play one game of this many cards
        answer = input(f'Will the next card be higher or lower than the '
                       f'{currentCardRank} of {currentCardSuit}? (enter h or l): ')
        answer = answer.casefold() # force lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print(f'Next card is: {nextCardRank} of {nextCardSuit}')

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('You got it right, it was lower')
                score += 20
            else:
                print('Sorry, it was not lower')
                score -= 15

        print(f'Your score is {score}\n')
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK, bye')

