import random  #for creating random choices


while True:
  print("lets play rock, paper and scissors")
  print("1.rock", "2. paper", "3.scissors")
  player= int(input())

  if player ==1:
    print("you selected rock")
    player= "rock"

  elif player ==2:
    print("you selected rock")
    player= "paper"

  elif player ==3:
    print("you selected rock")
    player= "scissors"

  else:
    print("invalid choice")
    

    choices = ["rock", "paper", "scissors"]
    Comp_choice = random.choice(choices)  #make random choices
    print("computer selected " ,Comp_choice)

    if player==Comp_choice:
     print("its a tie!")

    elif (player=="rock" and Comp_choice== "scissors") or (player=="paper" and Comp_choice=="rock") or (player=="scissors" and Comp_choice=="paper"):
     print("You have won")

    else:
     print("you loose")

    user_choice = input("You wanna play again?(y/n).lower()")
    if user_choice =="y":
     continue
else:
