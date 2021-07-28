import random
from time import sleep
from os import system, name

list_of_words = ["zigzag", "oxygen",
                 "mystify", "polka",
                 "rowing", "Cinderella",
                 "migrate", "bargain"
                 ]


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
          """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                   """
          ]


def main():
    while True:
        try:
            clear_screen()
            game_on = input("Do you want to play Hangman\nEnter 'y' for yes and 'n' to exit\n")
        except:
            print('Enter correct input\n')
        if game_on == 'y' or game_on == 'Y':
            word_choice = random.choice(list_of_words)
            blank_list = []
            chances = 6
            won = 0
            for letter in word_choice:
                blank_list.append("_")
            while chances > 0 and not won:
                print(blank_list)
                print(stages[chances])
                guess = input('\nGuess a letter\n')
                found = 0
                for i, char in enumerate(word_choice):
                    if guess.lower() == char:
                        blank_list[i] = char
                        found = 1
                if found == 0:
                    print('Wrong guess\n')
                    chances -= 1
                elif "_" not in blank_list:
                    print(blank_list)
                    won = 1
            if won == 1:
                print('Congratulations!!! You won\n')
            else:
                print(stages[chances])
                print('Sorry You lost.Game over\n')
            sleep(5)
        elif game_on == 'n' or game_on == 'N':
            break
        else:
            print('Enter correct input\n')


if __name__ == '__main__':
    main()
