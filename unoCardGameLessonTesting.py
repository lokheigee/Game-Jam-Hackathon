import random
"""
Generate the 108 UNO card deck
Parameters: None
Return deck -> list
"""
def buildDeck():
    #Use a list od string to represent the cards
    # Sample card : "Red 7", "Green 8"
    deck = []
    colours = ["Red", "Green", "Yellow", "Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]
    #nested for loop for generate the card starting with colours
    for colour in colours:
        for value in values:
            # cardVal = colour + number
            cardVal = "{} {}".format(colour,value)
            deck.append(cardVal)
            # We want two cards for every number and power card except 0
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])

    return deck

"""
Shuffle a list of cards passed into it
Parameters: Deck -> list
return: deck 
"""
def shuffleDeck(deck):
    #swipe the position of each card to a random position
    for cardPos in range(len(deck)):
        randPos = random.randint(0,107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck

"""
Draw a specified number of cards off the top of the deck
Parameters: numCard -> int
return: cardDrawn -> list
"""
def drawCard(numCard):
    cardsDrawn = []
    for x in range (numCard):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

"""
print formatted list of player's hand
Parameter: player -> intyeger, playerHand -> list
return : null
"""
#encountered error index out of range (we increase player turn by 1 each turn but there's no enough players )
def showHand(player, playerHand):         
    print("Player {}'s turn ".format(player+1))
    print("Your Hand")
    print("----------------")
    y = 1 
    for card in playerHand:
        print("{} ) {}".format(y,card))   #formatting the showHand with an integer infront of every card
        y+=1    
    print("")

"""
Check whether a player can play a card
Parameters: colour -> String , value -> String, playerHand ->List
Return: Boolean
"""
def canPlay(colour,value,playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False



unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
discards =[]
print(unoDeck)

"""
Players to draw cards at the beginning of the game
Create a list for players to draw cards
"""

players = []   #For creating player's hand
colours = ["Red", "Green", "Yellow", "Blue"]
numPlayers = int(input("How many players? "))
while numPlayers < 2 or numPlayers > 4 :
    numPlayers = int(input("Invalid. Please enter a number between 2 - 4. How many players?"))
for player in range(numPlayers):
    players.append(drawCard(5))

"""
status of the game: etc which player turn , direction op player turn and if the game is ended
"""
playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColour = splitCard[0]
if currentColour!= "Wild":
    cardVal = splitCard[1]
else :
    cardVal = "Any"





while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile: {}".format(discards[-1]))
    if canPlay(currentColour,cardVal,players[playerTurn]):
        cardChosen = int(input("Which card do you want to play? "))
        # the outer [] is because players[playerTurn[cardChosen - 1]] is returning a string but canPlay need a list as parameter
        while not canPlay(currentColour,cardVal,[players[playerTurn][cardChosen - 1]]): 
             cardChosen = int(input("Not a valid card. Which card do you want to play? "))
        print("You played {}".format(players[playerTurn][cardChosen - 1]))
        discards.append(players[playerTurn].pop(cardChosen -1))
        #check for "wild" card
        splitCard = discards[-1].split(" ", 1)    #for knowing the card's colour and value by splitting the cards (from the top of dispost card) -1 for the latest card on the discard pile
        currentColour = splitCard[0]             #splitCard[0] equals to  colour "Blue", splitCard[1] equals to number 1
        if len(splitCard) == 1:                  # if the splitCard has only one value which is "Wild"
            cardVal = "Any"
        else:
            cardVal = splitCard[1]
        if currentColour == "Wild":              # "Wild" card (Change colour by the player)
            for x in range(len(colours)):        # print out all the colour for player
                print("{} ) {}".format(x + 1, colours[x]))     # x starts at 0 and print the colour list
        newColour = int(input("What colour do you want to change? "))
        while newColour < 1 or newColour > 4 :      # make sure the input is correct
            newColour = int(input("Invalid choice .What colour do you want to change? "))
        currentColour = colours[newColour -1 ] # point at the colour index required 
        if cardVal == "Reverse":
            playDirection = playDirection * -1     #changing the player turn by (playerTurn += playDirection)
        elif cardVal == "Skip":
            playerTurn += playDirection     #using direction as it can get negitive
        elif cardVal == "Draw Two":
            playerDraw = playerTurn + playDirection
            if playerDraw == numPlayers:
                playerDraw = 0
            elif playerDraw < 0:
                playerDraw = numPlayers - 1
            players[playerDraw].extend(drawCard(2))
        elif cardVal == "Draw Four":
            playerDraw = playerTurn + playDirection
            if playerDraw == numPlayers:
                playerDraw = 0
            elif playerDraw < 0:
                playerDraw = numPlayers - 1
            players[playerDraw].extend(drawCard(4))
            
            
    



       
         

        elif cardVal == "Draw Four":
         players[playerTurn].extend(drawCard(4))
        print("")

    else: #can't play any card
        print("You can't play. You have to draw a card")
        players[playerTurn].extend(drawCard(1))       # adding a list to the orginal list cuz drawCard return a list (merging two list)
   
    



    

    playerTurn += playDirection
    if playerTurn == numPlayers:        #make sure the player turn won't go out of range by looping back to the first player
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers - 1 




          




