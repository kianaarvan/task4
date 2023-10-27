import random

pc_number=random.randint(0,100)
n=0
while True:
    
    your_number=int(input("enter your number:"))
    n+=1
    if pc_number==your_number:
            print("you guess a right number!")
            break
    elif pc_number>your_number:
            print("guess a larger number!")
    elif pc_number<your_number:
            print("guess a smaller number!")

print(pc_number)
print(n)
