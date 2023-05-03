from game_classes.ninja import Ninja
from game_classes.pirate import Pirate
import random

def pickCharacter(ninja, pirate):
    response = ""
    result = []
    while response != '1' and response != '2':
        response = input("Which one do you choose? \n 1)Ninja \n 2)Pirate \n >>> ")
    if response == '1':
        print("You are the Ninja!")
        result.append(ninja)
        result.append(pirate)
    else:
        print("You are the Pirate!")
        result.append(pirate)
        result.append(ninja)
    return result

ninja = Ninja()
pirate = Pirate()

print('Welcome to Ninja vs Pirate!')
result = pickCharacter(ninja, pirate)
yourPick = result[0]
computer = result[1]

while yourPick.health > 0 and computer.health > 0:
    response = ""
    while response != '1' and response != '2' and response != '3':
        response = input("Choose an action \n 1)Attack \n 2)Use Special \n 3)Use Buff \n >>>")

    if yourPick.stun == 1:
        yourPick.stun = 0
        print(f"{yourPick.name} got stun and can't move!")
    else:
        if response == '1':
            yourPick.attack(computer)
        elif response == '2':
            yourPick.use_special(computer)
        else:
            yourPick.use_buff()

    if computer.stun == 1:
        computer.stun = 0
        print(f"{computer.name} got stun and can't move!")
    else:
        computer_move = random.randint(1,3)
        if computer_move == 1:
            computer.attack(yourPick)
        elif computer_move == 2:
            computer.use_special(yourPick)
        else:
            computer.use_buff()

if yourPick.health > 0:
    print(f'You win! {computer.name} never saw it coming')
elif computer.health <= 0:
    print('it is a draw')
else:
    print('You lose, pilgrim')

# print('Welcome to Cowboy vs Kickboxer, you are the Cowboy!')
# while cowboy.health >= 0 and kb.health >= 0:
#     response = ''
#     while response != '1' and response != '2' and response != '3':
#         response = input("Choose an action \n 1)Attack \n 2)Use Special \n 3)Use Buff \n >>>")
    
#     if response == '1':
#         cowboy.attack(kb)
#     elif response == '2':
#         cowboy.use_special(kb)
#     else:
#         cowboy.use_buff()
#     kb_move = random.randint(1,3)
#     if kb_move == 1:
#         kb.attack(cowboy)
#     elif kb_move == 2:
#         kb.use_special(cowboy)
#     else:
#         kb.use_buff()

# if cowboy.health > 0:
#     print('You win! JD never saw it comin')
# elif kb.health <= 0:
#     print('it is a draw')
# else:
#     print('You lose, pilgrim')








