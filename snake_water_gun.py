import random

# snake, water , gun game
'''
1 for snake
2 for water
3 for gun

'''

computer= random.choice([1,2,3])
you=int(input("Enter your choice (1 for snake, 2 for water, 3 for gun) : "))
dict={1:"snake",2:"water",3:"gun"}

print(f"You chose {dict[you]} and computer chose {dict[computer]}")

if(computer==you):
    print("Draw")
else:


    '''if(computer==1):
        if(you==2):
            print("You lose")
        elif(you==3):
            print("You win")
    elif(computer==2):
        if(you==1):
            print("You win")
        elif(you==3):
            print("You lose")
    elif(computer==3):
        if(you==1):
            print("You lose")
        elif(you==2):
            print("You win")
    else:
        print("Invalid input")'''
    
    if(computer-you==-1 or computer-you==2):
        print("You lose")
    else:
        print("You win")











