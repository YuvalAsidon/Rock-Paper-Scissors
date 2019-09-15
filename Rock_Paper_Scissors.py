from random import choice

WINNER_SCORE=2
score=[0,0]
while score[0]<WINNER_SCORE and score[1]<WINNER_SCORE: 
    print(f"User Score: {score[0]}      Computer Score:{score[1]}")
    print("...rock...\n...paper...\n...scissors...")
    computer=choice(['rock','paper','scissors'])

    user_choice=input("(Enter your choice): ").lower()
    if user_choice in ["quit", 'q']:
        break
    print(f"the computer plays: {computer}")
    
    if user_choice == computer:
        print("It's a draw!")
    elif user_choice == 'paper':
        if computer == 'rock':
            score[0]+=1
            print("User wins!")
        elif computer == 'scissors':
            score[1]+=1
            print("Computer wins!")
    elif user_choice == 'scissors':
        if computer == 'paper':
            score[0]+=1
            print("User wins!")
        elif computer == 'rock':
            score[1]+=1
            print("Computer wins!")
    elif user_choice == 'rock':
        if computer == 'scissors':
            score[0]+=1
            print("User wins!")
        elif computer == 'paper':
            score[1]+=1
            print("Computer wins!")
    else:
        print("Something went wrong")

if score[0]==WINNER_SCORE:
    print("CONGRATS, YOU WON!")
elif score[0]==score[1]:
    print("It's a draw!")
else:
    print("OH NO THE COMPUTER WON")
