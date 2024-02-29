import random

name = input("What is your name?")
question = input("What is your question?(Yes or No questions only)?")
answer = ""
random_number = random.randint(1,9)
message1 = "Yes - definitely."
message2 = "It is decidedly so."
message3 = "Without a doubt."
message4 = "Reply hazy, try again."
message5 = "Ask again later."
message6 = "Better not tell you now."
message7 = "My sources say no."
message8 = "Outlook not so good."
message9 = "Very doubtful."

if random_number == 1:
  answer = message1
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
elif random_number == 2:
  answer = message2
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
elif random_number == 3:
  answer = message3
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
elif random_number == 4:
  answer = message4
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
elif random_number == 5:
  answer = message5
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
elif random_number == 6:
  answer = message6
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
elif random_number == 7:
  answer = message7
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
elif random_number == 8:
  answer = message8
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
elif random_number == 9:
  answer = message9
  print(f"{name} asks: {question}")
  print(f"Magic 8-Ball's answer is: {answer}")
else:
  print("Error")