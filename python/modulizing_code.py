#Modulizing : breacking code into small reusable functions

import random
choices = ('r','p','s')

def get_user_choice():
    while True:
        user_choice = str(input("Rock, paper or scissors? (r/p/s)")).lower()
        if user_choice not in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choices(user_choice, computer):
    print(f'You chose {user_choice}')
    print(f'Computer chose {computer}')

def determine_winner(user_choice, computer):
    if user_choice == computer:
        print('Tie')
    elif ((user_choice == "r" and computer == "s") or 
        (user_choice == "s" and computer == "p") or 
         (user_choice == "p" and computer == "r")):
        print('You win')
    else : 
        print('You lose')

def play_game():
    while True:
        user_choice = get_user_choice()
        computer = random.choice(choices)

        display_choices(user_choice, computer)
        determine_winner(user_choice, computer)

        should_continue = input('Continue? (y/n):').lower()
        if should_continue == 'n':
            break
    
play_game()

        