import random

print("Do you want to play Black Jack")
answer = input()


def blackjack():
    cardsList = ["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
    random.shuffle(cardsList)

    playerCards = []
    computerCards = []

    computerCards.append(cardsList[0])
    computerCards.append(cardsList[1])
    playerCards.append(cardsList[2])
    playerCards.append(cardsList[3])
    del cardsList [0:4]

    print("Dealer's Hand: _ | ", computerCards[1])
    print("Your Hand: ", playerCards)

    # Stand/Hit logic for player. Bust if over 21.
    response = ""
    while(response.lower() != "stand"):
        sum = 0 
        for card in playerCards:
            if(card ==  "Q" or card == "K" or card == "J"):
                sum += 10
            elif(card == "A"):
                sum += 1
            else:
                sum += card    
        if(sum > 21):
            print("Bust! You lose.")
            exit()
        print("Do you want to stand or hit?")
        response = input()
        if(response.lower() == "hit"):
            playerCards.append(cardsList[0])
            del cardsList[0]
            print("Your cards: ", playerCards)

    # Calculate playerSum
    playerSum = 0 
    for card in playerCards:
        if(card ==  "Q" or card == "K" or card == "J"):
            playerSum += 10
        elif(card == "A"):
            playerSum += 1
        else:
            playerSum += card

    # Calculate computerSum
    computerSum = 0 
    for card in computerCards:
        if(card ==  "Q" or card == "K" or card == "J"):
            computerSum += 10
        elif(card == "A"):
            computerSum += 1
        else:
            computerSum += card  

    # Initial check if computer wins
    if (computerSum > playerSum):
        print("You: ", playerSum)
        print("Computer: ", computerSum)
        print("You lose! Dealer wins.")
        exit()

    while(computerSum <= playerSum):
        computerCards.append(cardsList[0])
        del cardsList[0]
        print("Computer Hand: ", computerCards)

        computerSum = 0 
        for card in computerCards:
            if(card ==  "Q" or card == "K" or card == "J"):
                computerSum += 10
            elif(card == "A"):
                computerSum += 1
            else:
                computerSum += card 

        if(computerSum > 21):
            print("You: ", playerSum)
            print("Computer: ", computerSum)
            print("Bust! Dealer loses, you win!")
            exit()
        if (computerSum > playerSum):
            print("You: ", playerSum)
            print("Computer: ", computerSum)
            print("You lose! Dealer wins, you lose.")
            exit()


         

if(answer.lower() == "yes"):
    print("Great! Let's Play Black Jack")
    blackjack()
else: 
    print("Screw you")    


