# SNAKE,WATER AND GUN GAME 
import random
user_win=0
computer_win=0
draw_macthes=0
n=int(input("How many matches will conduct between user and system = "))
while n>=1:
    user=['snake','water','gun']
    system=random.choice(user)
    a=input("enter the user choice:")
    if a=="snake":
        if system=='snake':
            print("Tie the match")
            draw_macthes=draw_macthes+1
        elif system=='gun':
            print("lose the match,sorry")
            computer_win=computer_win+1
        elif system=='water':
            print("won the match,congrats!!")
            user_win=user_win+1

    elif a=="water":
        if system=='water':
            print("Tie the match")
            draw_macthes=draw_macthes+1
        elif system=='snake':
            print("lose the match,sorry")
            computer_win=computer_win+1
        elif system=='gun':
            print("won the match,congrats!!")
            user_win=user_win+1
    elif a=="gun":
        if system=='gun':
            print("Tie the match")
            draw_macthes=draw_macthes+1
        elif system=='water':
            print("lose the match,sorry")
            computer_win=computer_win+1
        elif system=='snake':
            print("won the match,congrats!!")
            user_win=user_win+1
    else:
        print("invalid user")
    n=n-1
print("draw macthes beetween computer and user",draw_macthes)
print("computers won macth",computer_win,"times")
print("user won the match",user_win,"times")

print(input("congrats......"))

        
        
