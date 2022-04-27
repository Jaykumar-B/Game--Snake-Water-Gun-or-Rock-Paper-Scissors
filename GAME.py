import random

# Snake Water Gun or Rock Paper Scissors
def Game(comp,you):
    a=comp
    b=you
    # If two values are equal, declare a tie!
    if a==b:
        return None

     # Check for all possibilities when computer chose W    
    elif a=='W':
        if b=='G':
            return False
        elif b=='S':
            return True

     # Check for all possibilities when computer chose S
    elif a=='S':
        if b=='G':
            return True
        elif b=='W':
            return False

     # Check for all possibilities when computer chose G
    elif a=='G':
        if b=='W':
            return True
        elif b=='S':
            return False



print("Comp's Turn choose Water(W)  Snake(S)  Gun(G) :")
rand=random.randint(1, 3)
if rand==1:
    comp='W'
elif rand==2:
    comp='S'
elif rand==3:
    comp='G'
you=input(("Your Turn choose Water(W) Snake(S) Gun(G) : "))

print(f"comp's choice is {comp} ")
print(f"Your choice is {you} ")

c=Game(comp, you)
if c==None:
    print('The Game is Tie!')
elif c:
    print('You won!')
else:
    print("You Lose!")
