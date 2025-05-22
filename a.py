import random
a=int(input("enter your choice 0-rock, 1- paper, 2-scissors "))
if(a>2):
    print("invalid input, enter ur choice between 0-2")
else:
    x=['rock','paper','scissors']
    b=random.randint(0,2)
    print(f"computer chose {b}")
   
    if(a==0):
        if(b==0):
            print("draw")
        elif(b==1):
            print("computer won")
        else:
            print("you won")

    if(a==1):
        if(b==0):
            print("you won")
        elif(b==1):
            print("draw")
        else:
            print("computer won")

    if(a==2):
        if(b==0):
            print("computer won")
        elif(b==1):
            print("you won")
        else:
            print("draw")