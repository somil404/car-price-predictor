import random

i = 0

while i<5:
    choice = input("Enter your choice: ")
    b = random.choice([1,2,3])
    choices = {"r":1, "p":2, "s":3}
    a = choices[choice]
    reverseDict = {1:"Rock", 2:"Paper", 3:"Scissor"}
    print(f"Your choice is {reverseDict[a]} and computer's choice is {reverseDict[b]}\n")
    if(a == b):
        print("Tie\n")
        i += 1
    else:
        if(a == 1 and b == 2):
            print("YOU LOSE\n")
        elif(a == 1 and b == 3):
            print("You WIN\n")
        elif(a == 2 and b == 1):
            print("You WIN\n")
        elif(a == 2 and b == 3):
            print("You LOSE\n")
        elif(a == 3 and b == 1):
            print("You LOSE\n")
        elif(a == 3 and b == 2):
            print("You WIN\n")
        i +=1
        