import random

while True:
    choices = ('r','p','s')
    
    person = str(input("Rock, paper or scissors? (r/p/s)")).lower()
    if person not in choices:
        print('Invalid choice!')
        continue

    computer = random.choice(choices)

    print(f'You chose {person}')
    print(f'Computer chose {computer}')

    if person == computer:
        print('Tie')
    elif ((person == "r" and computer == "s") or 
        (person == "s" and computer == "p") or 
         (person == "p" and computer == "r")):
        print('You win')
    else : 
        print('You lose')

    should_continue = input('Continue? (y/n):').lower()
    if should_continue == 'n':
        break
    

        