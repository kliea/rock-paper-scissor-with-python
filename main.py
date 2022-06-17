#rock paper scissor game
import random
import sys
c_wins = 0
p_wins = 0
ties = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock"]:
        user_choice = "r"
    elif user_choice in ["Paper"]:
        user_choice = "p"
    elif user_choice in ["Scissors"]:
        user_choice = "s"
    else:
        print("try again!")
        Choose_Option()
    return user_choice
def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")
    if user_choice == comp_choice:
        print('It is a tie!')
        ties = ties + 1
    elif user_choice == 'r' and comp_choice == 's':
        print('You win!')
        p_wins +=1
    elif user_choice == 'p' and comp_choice == 'r':
        print('You win!')
        p_wins +=1
    elif user_choice == 's' and comp_choice == 'p':
        print('You win!')
        p_wins +=1
    elif user_choice == 'r' and comp_choice == 'p':
        print('You lose!')
        c_wins +=1
    elif user_choice == 'p' and comp_choice == 's':
        print('You lose!')
        c_wins +=1
    elif user_choice == 's' and comp_choice == 'r':
        print('You lose!')
        c_wins +=1
   


    print("")
    print("Player wins: " + str(p_wins))
    print("Computer wins: "+ str(c_wins))
    print("Ties: "+ str(ties))
    print("")
    
    print('Do you want to continue?')
    response = input(' (Y or N) ')
    if response == 'N':
        sys.exit()