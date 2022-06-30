import random
import blackJack_art
from os import system #for windows

clear = lambda: system('cls')
logo = blackJack_art.logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def random_card():
    card = random.choice(cards)
    return card 

def random_cards_generetor(how_many_cards, cards_for):
    for i in range(0,how_many_cards):
        cards_for.append(random_card())

def score(cards_of):
    sum = 0 
    for card in cards_of:
        sum += card
    return sum

random_cards_generetor(2, user_cards)
random_cards_generetor(2, computer_cards)

def game():
    clear()
    print(logo)
    print(f"Your cards : {user_cards}, current score : {score(user_cards)}")
    print(f"Computer first card : {computer_cards[0]}")
    if score(user_cards) == 21 and len(user_cards) == 2:
        print(f"BLACKJACK, You WON, your score {score(user_cards)}")
    else:
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_choice == "y":
            random_cards_generetor(1, user_cards)
            if score(user_cards) > 21 : 
                if 11 in user_cards:
                    index = user_cards.index(11)
                    user_cards[index] = 1
                    print(f"11 became 1, your current score: {score(user_cards)}")
                    game()
                print(f"BUST, your cards {user_cards}, score {score(user_cards)}, computer WON")
            elif score(user_cards) < 21: 
                game()
        else:
            while score(computer_cards) < 17 and score(computer_cards) != 21:
                random_cards_generetor(1, computer_cards)
                print(f"computer took card, computer score {score(computer_cards)}")
                if score(computer_cards) > 21 : 
                    print(f"You WON, computer score {score(computer_cards)} BUST!")
                    
            if score(user_cards) > score(computer_cards):
                print(f"You WON, your score {score(user_cards)}, computer score: {score(computer_cards)}")
            elif score(user_cards) == score(computer_cards):
                print(f"It's a DRAW, your score: {score(user_cards)}, computer score: {score(computer_cards)}")
            elif score(user_cards) < score(computer_cards) and score(computer_cards) <= 21: 
                print(f"You Lost, computer score: {score(computer_cards)} your score: {score(user_cards)}")

game() 