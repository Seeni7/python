import random
import time

player = random.randint(1,6)
ai = random.randint(1,6)
def dice():
    player = random.randint(1,6)
    print("You rolled"+ str(player))

  
    ai = random.randint(1,6)
    print("The computer rolls...")
time.sleep(2)

print("The computer has rolled a"+ str(player))

if player > ai:
     
    print("You Win")
elif player == ai:

    print("Tie Game.")
else:
    print("You lose")

# main loop 

while True:
    print("Press return to roll your die.")
    roll = input()

    dice() 