import sys , random


Diamonds =chr(9830)
Hearts =chr(9829)
Spades =chr(9827)
Clubs = chr(9824)
Backside = 'backside'


        
        
def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com
    
        Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')
    
  
    Money = int(input('Enter your amount -->'))
    
    
    while True:
        if Money <= 0:
            print('''First go to a Job and earn money 
                  then come to bet''')
            sys.exit()
            
        print('Money : ',Money)
        
        bet = getBet(Money)
        
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        
        print('Bet : ', bet)
        
        while True :
            displayHands(playerHand , dealerHand,False)
            print()
            
            if getValueOfHand(playerHand)> 21:
                break
            move = Move(playerHand,Money - bet)
            if move == 'D':
                addBet = getBet(min(bet,Money-bet))
                bet += addBet
                print("Bet increase to %s"%bet)
                print("Bet : ",bet)
                
                
            if move in ('H' , "D"):
                newCard = deck.pop()
                rank , suit = newCard
                print('You drew {} of {}'.format(rank,suit))
                playerHand.append(newCard)
                
                if getValueOfHand(playerHand) > 21:
                    continue
            if move in ("S","D"):
                break
        if getValueOfHand(playerHand) <= 21:
            while getValueOfHand(dealerHand) < 17:
                print("Dealer hits......")
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)
                
                
                if getValueOfHand(dealerHand) > 21:
                    break
                input('Press Enter to continue.....')
                print('\n\n')
                
                 # Show the final hands:
        displayHands(playerHand, dealerHand, True)
 
        playerValue = getValueOfHand(playerHand)
        dealerValue = getValueOfHand(dealerHand)
         # Handle whether the player won, lost, or tied:
        if dealerValue > 21:
             print('Dealer busts! You win ${}!'.format(bet))
             Money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
             print('You lost!')
             Money -= bet
        elif playerValue > dealerValue:
             print('You won ${}!'.format(bet))
             Money += bet
        elif playerValue == dealerValue:
             print('It\'s a tie, the bet is returned to you.')
 
        input('Press Enter to continue...')
        print('\n\n')
            
                
                
                
                
                
                
                
#Fuction which will get us a Valid Bet
def getBet(maximum_Bet):
    while True:
        print('How much do you Bet?(1 - {} OR Quit[Q]). '.format(maximum_Bet))
        bet = input(':->').upper().strip()
        if bet == 'Q' or bet == 'Quit':
            print("Thank You for playing")
            sys.exit()
        
        if not bet.isdecimal():
            continue
        
        bet = int(bet)
        if 1 <= bet <= maximum_Bet:
            return bet
        


#Fuction for Deck

def getDeck():
    deck = []
    for suits in (Hearts, Diamonds , Spades ,Clubs):
        for rank in range(2,11):
            deck.append((str(rank),suits))
        for rank in ('J','Q','K','A'):
            deck.append((rank , suits))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print("Dealer: ", getValueOfHand(dealerHand))
        displayCards(dealerHand)
    else:
        print("Dealer:  ???")
        displayCards([Backside] + dealerHand[1:])
        
    print('Player: ',getValueOfHand(playerHand))
    displayCards(playerHand)
    
def getValueOfHand(cards):
    value = 0 
    Aces = 0
    for card in cards :
        rank = card[0]
        if rank == 'A':
            Aces += 1
        elif rank in ('K','Q','J'):
            value += 10
        else:
            value += int(rank)
            
    value += Aces
    for i in range(Aces):
        if value + 10 <= 21:
            value += 10
    
    return value
            
    
def displayCards(cards):
    rows = ['','','','','']
    for i , card in enumerate(cards):
        rows[0] += ' ___  '
        if card == Backside:
            rows[1] =  '|## | '
            rows[2] =  '|###| '
            rows[3] =  '|_##| '
            
        else:
            rows[1] =  '|{} | '.format(card[0].ljust(2))
            rows[2] =  '| {} | '.format(card[1])
            rows[3] =  '|_{}| '.format(card[0].rjust(2,'_'))
    
    for row in rows:
        print(row)

def Move(playerHand , Money):
    while True :
        moves = ['(H)it','(S)tand']
        
        if len(playerHand) == 2 and Money > 0:
            moves.append('(D)ouble Down')
            
            
        movePrompt =', '.join(moves) + '-->'
        move = input(movePrompt).upper()
        if move in ('H' , 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move
            
        
if __name__ == '__main__':
    main()
            
    

