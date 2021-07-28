###Blackjack

logo = """ __            _    _            _
| |   | |          | |  (_)          | |
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /n
| |_) | | (_| | (__|   <| | (_| | (__|   <
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |
                      |__/
                                                """

import random
from time import sleep
from os import name, system

card_value = {'Ace': 11, 'Two': 2, 'Three': 3,
              'Four': 4, 'Five': 5, 'Six': 6,
              'Seven': 7, 'Eight': 8, 'Nine': 9,
              'Ten': 10, 'Jack': 10,
              'Queen': 10, 'King': 10}
card_name = ['Spades', 'Hearts', 'Clubs', 'Diamonds']


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def get_value(card):
    return card_value[card.split()[0]]


def get_totalvalue(cards):
    total = 0
    for card in cards:
        total += get_value(card)
    return total


class CardDeck:
    def __init__(self, value=None):
        # To avoid list assignment index out of range error
        self.suit = [None] * 52
        self.value = value
        self.user_cards = []
        self.computer_cards = []

    def generate_cards(self):
        i = 0
        for names in card_name:
            for cards in card_value:
                self.suit[i] = cards + ' of ' + names
                i += 1

    def get_card(self):
        card = random.choice(self.suit)
        return card

    def display(self):
        print('\n\nYour cards\n')
        print(self.user_cards)
        print("\nComputer's card\n")
        print(self.computer_cards[0])

    def display_full(self):
        print('\n\nYour cards\n')
        print(self.user_cards)
        print("\nComputer's card\n")
        print(self.computer_cards)


def main():
    while True:
        correct_input = False
        c = CardDeck()
        c.generate_cards()
        clear_screen()
        print(logo)
        game_on = input("Enter 'y' to play Blackjack, 'n' to quit\n")
        if game_on == 'y' or game_on == 'Y':
            c.user_cards.append(c.get_card())
            c.user_cards.append(c.get_card())
            c.computer_cards.append(c.get_card())
            c.computer_cards.append(c.get_card())
            c.display()

            while not correct_input:
                pick = input("Do you want to pick another card. Enter 'y' or 'n'\n")
                if pick == 'y' or pick == 'Y':
                    c.user_cards.append(c.get_card())
                    correct_input = True
                elif pick == 'n' or pick == 'N':
                    correct_input = True
                else:
                    print('Enter the correct input\n')

            t_user = get_totalvalue(c.user_cards)
            t_computer = get_totalvalue(c.computer_cards)
            c.display_full()
            if 21 >= t_user > t_computer:
                print('\nCongratulations!!! You won')
            else:
                print('\nSorry. You lost')
            sleep(5)
        else:
            break


if __name__ == '__main__':
    main()
