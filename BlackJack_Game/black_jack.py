import random
import os

status = True

def clear_console():
    print("\n" * 50)

def random_number(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def draw_player(deck, player_hand):
    card = random_number(deck)
    player_hand.append(card)
    return sum(player_hand), player_hand

def draw_dealer(deck, dealer_hand):
    first_card = None
    while sum(dealer_hand) < 17:
        card = random_number(deck)
        dealer_hand.append(card)
        if first_card is None:
            first_card = card
    return first_card, sum(dealer_hand), dealer_hand

while status:
    # Reset everything for new game
    clear_console()
    num_list = [11,2,3,4,5,6,7,8,9,10,10,10,10] * 4
    dealer_list = []
    player_list = []
    count_tries = 0

    choice = input("Welcome to the blackjack game!!! Enter 'y' to start the game: ")

    while choice.lower() == "y":
        final_player, player = draw_player(num_list, player_list)
        count_tries += 1

        if count_tries == 1:
            # Draw dealer's first card only once
            dealer_first_card = draw_dealer(num_list, dealer_list)[0]
            print(f"Your cards are {player} and dealer's first card is {dealer_first_card}")
        else:
            print(f"Your player cards are: {player_list} and sum is {final_player}")

        if final_player > 21:
            print(f"Oops Busted!! Better luck next time. Your Cards = {player_list} and Dealer's cards = {dealer_list}")
            break

        choice = input("Enter 'y' to draw another card, 'n' to stand: ")

    # Dealer draws only after player stands or busts
    if final_player <= 21:
        _, final_dealer, dealer_list = draw_dealer(num_list, dealer_list)
        print(f"Dealer's final sum is: {final_dealer} and dealer's cards: {dealer_list}")

        # Determine winner
        if final_dealer > 21:
            print("Dealer busted! You win!")
        elif final_player > final_dealer:
            print("Congratulations, you win!")
        elif final_player < final_dealer:
            print("Oops you lost, dealer wins")
        else:
            print("It's a tie!")

    print(f"Your sum is: {final_player}")
    loop_choice = input("Do you want to start a new game? Press 'y' to start over, 'n' to exit: ")
    if loop_choice.lower() != "y":
        status = False

print("Thank you for playing!!!")
