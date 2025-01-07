import random
print("----------WHO IS NO 1---------")
L1=[]
print("ENTER THE NAMES(4)")
for i in range(0,4):
    name=input(f"{i+1}:")
    L1.append(name)
print("LET's START!")
l=[["┌─────────┐",
    "│         │",
    "│    ●    │",
    "│         │",
    "└─────────┘"],
   ["┌─────────┐",
    "│ ●       │",
    "│         │",
    "│       ● │",
    "└─────────┘"],
   ["┌─────────┐",
    "│ ●       │",
    "│    ●    │",
    "│       ● │",
    "└─────────┘"],
   ["┌─────────┐",
    "│ ●     ● │",
    "│         │",
    "│ ●     ● │",
    "└─────────┘"],
   ["┌─────────┐",
    "│ ●     ● │",
    "│    ●    │",
    "│ ●     ● │",
    "└─────────┘"],
   ["┌─────────┐",
    "│ ●     ● │",
    "│ ●     ● │",
    "│ ●     ● │",
    "└─────────┘"]]
l2=[0,0,0,0]
for j in range(0,4):
    print("**********************************")
    print(f"{j+1}.")
    a=input(f"Press E to roll the dice:")
    if a=='E' or a=='e':
        b=random.choice(l)
        for i in b:
            print(i)
        k=int(input("enter the no:"))
        if k>=1 or k<=6:
            l2[j]=l2[j]+k
        else:
            print("INVALID INPUT,YOU LOOSE A CHANCE")
    
max=0
for i in l2:
    if max<i:
        max=i
a=l2.index(max)
print("-----------------------")
print(a)
print("-----------------------")