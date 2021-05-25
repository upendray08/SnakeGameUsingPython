import random

def gamewin(comp,player):
    if comp == player:
        return None
    elif comp == 's':
        if player=='w':
            return False
        elif player=='g':
            return True
    elif comp=='g':
        if player=='s':
            return False
        elif player=='w':
            return True
    elif comp=='w':
        if player=='g':
            return False
        elif player=='s':
            return True
    

randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='g'
else:
    comp='w'
player=input("enter snake(s),gun(g) and water(w):\n")
a = gamewin(comp,player)
print(f"Computer choose {comp}")
print(f"You choose {player}")
if a==None:
    print("You tie the game!")
elif  a:
    print("you win !")
else :
    print("You loose !")


