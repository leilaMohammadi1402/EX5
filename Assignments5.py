shoro=int(input("Enter 1:start or 2:Exit  wich?"))
import random 

while True:
    if shoro==2:
        print("Exit")
        break


    elif shoro==1:
        tas=random.randint(1,6)
        print(" number1 your  tas is :",tas)
        if tas==6:
            for i in range(2):
                tas2=random.randint(1,6)
                print(" number 2 your tas is :",tas2)
            break
        else:
            break

    else:
        print("was a problem!")
        break