"""
Filename: blackjack.py
Authors: Matt Matt's Coding by the Campfire Crew
"""


import random
from simpleimage import SimpleImage

#image = SimpleImage(filename)

MIN_RANDOM = 1
MAX_RANDOM = 11
NUM_RANDOM = 3



def main():
    # Let's get started with some liquid courage
    print("I still remember how to do a print statement!\nWhew - I deserve a drink!\n")

    # TODO: Hey Matt - how do we play Blackjack again?
    # type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    # suit value
    suits_value = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

    # What cards do I have?
    player_cards = []

    # Let's beat the dealer
    player_score = 0
    # print("player_score is type ", type(player_score))
    dealer_score = 0

    # TODO: Let's bring the Las Vegas Welcome to Matt
    welcome_sign = SimpleImage('images/welcome_sign.png')
    welcome_sign.show()

    print("Welcome to Vegas! Let's play Blackjack!\n")

    # dealing a card to the player
    print("Here are two cards.")

    # player_card_one = input(random.randint(MIN_RANDOM, MAX_RANDOM))
    player_card_one = random.randint(MIN_RANDOM, MAX_RANDOM)
    print("First card is ", str(player_card_one))
    # print("card one is type: ", type(player_card_one))

    # player_card_two = input(random.randint(MIN_RANDOM, MAX_RANDOM))
    player_card_two = random.randint(MIN_RANDOM, MAX_RANDOM)
    print("Second card is ", str(player_card_two))
    # print("card two is type: ", type(player_card_two))

    player_card_value = player_card_one + player_card_two
    print("You have " + str(player_card_value) + "\n")
    # print("player_card_value is type: ", type(player_card_value))

    # update the player score
    player_score += 1 # player_card_value

    # dealing a card to AI or dealer
    dealer_card_one = random.randint(MIN_RANDOM, MAX_RANDOM)
    dealer_card_two = random.randint(MIN_RANDOM, MAX_RANDOM)
    dealer_card_value = dealer_card_one + dealer_card_two

    # update the dealer score
    dealer_score += dealer_card_value

    # if player score is under 21, ask them if they want to hit or stand
    while player_score < 21:
        hit_choice = str(input("Would you like to hit or stand? "))
        if hit_choice == 'hit':
        # if choice == 'hit'
            player_card = random.randint(MIN_RANDOM, MAX_RANDOM)
            print("Next card is " + str(player_card))
            player_cards.append(player_card)
            player_card_value += player_card
            print("You have " + str(player_card_value))
        if hit_choice == 'stand':
        # elif choice == 'stand'
            # show both cards
            print("DEALER CARDS: ")
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_card_value[-1].card_value)

    print()

    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print("PLAYER SCORE = ", player_score)

    # Check for blackjack
    you_lose = SimpleImage('images/you_lose.png')
    you_lose.show()

    if player_score > 21 and total < 21:
        print("Sorry. You lose.")

    you_win = SimpleImage('images/you_win.png')
    you_win.show()

    if player_score == 21:
        print("YOU HAVE A BLACKJACK! YOU WIN")

    # Ask to play again
    play_again = input('Play again? "Yes" or "No"') == 'y'
    if play_again:
        return first_round


if __name__ == '__main__':
    main()

