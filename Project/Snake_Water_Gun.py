import random

def gameWin(comp, You):
    if comp == You:
        return None

    elif comp == 'S':
        if You == 'W':
            return False
        elif You == 'G':
            return True

    elif comp == 'W':
        if You == 'G':
            return False
        elif You == 'S':
            return True

    elif comp == 'G':
        if You == 'S':
            return False
        elif You == 'W':
            return True 


print("Computer's Choice: Snake(S), Water(W), and Gun(G)")

randNo = random.randint(1, 3)

if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'W'
elif randNo == 3:
    comp = 'G'

You = input("Enter Your Input (S, W, or G): ")

a = gameWin(comp, You)

print(f"Computer Choice: {comp}")
print(f"Your Choice is: {You}")

if a == None:
    print("The Match is a Tie!")
elif a:
    print("You won the match!")
else:
    print("You lost the match!")
