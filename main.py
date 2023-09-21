import random

print("Do you want to play Black Jack")
answer = input()


def blackjack():
    print("cards")
    cardsList = ["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
    random.shuffle(cardsList)
    playerCards = []
    computerCards = []
    computerCards.append(cardsList[0])
    computerCards.append(cardsList[1])
    playerCards.append(cardsList[2])
    playerCards.append(cardsList[3])
    del cardsList [0:4]
    print("Dealer's Hand: ", computerCards[1])
    print("Your Hand: ", playerCards)
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
            print("Bust! You lose")
            exit()
        print("Do you want to stand or hit?")
        response = input()
        if(response.lower() == "hit"):
            playerCards.append(cardsList[0])
            del cardsList[0]
            print(playerCards)

    playerSum = 0 
    for card in playerCards:
        if(card ==  "Q" or card == "K" or card == "J"):
               playerSum += 10
        elif(card == "A"):
               playerSum += 1
        else:
                playerSum += card

    computerSum = 0 
    for card in computerCards:
        if(card ==  "Q" or card == "K" or card == "J"):
               computerSum += 10
        elif(card == "A"):
               computerSum += 1
        else:
                computerSum += card             
    while(computerSum < playerSum):
         computerCards.append(cardsList[0])
         del cardsList[0]
         print(computerCards)

         if(computerSum > 21):
            print("Bust! Dealer loses")
            exit()
         if (computerSum > playerSum):
              print("You lose! Dealer wins")
              exit()


         

if(answer.lower() == "yes"):
    print("Great! Let's Play Black Jack")
    blackjack()
else: 
    print("Screw you")    


