#Magic 8-Ball Project

import random

name = input("Enter your name: ")
question = input("Ask Magic 8-Ball a question: ")
answer = ""


random_number = random.randint(1,20)

if random_number == 1:
    answer = "Yes, definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "It is certain."
elif random_number == 5:
    answer = "Signs point to yes."
elif random_number == 6:
    answer = "Reply hazy, try again."
elif random_number == 7:
    answer = "Better not tell you now."
elif random_number == 8:
    answer = "Cannot predict now."
elif random_number == 9:
    answer = "Ask again later."
elif random_number == 10:
    answer = "Don't count on it."
elif random_number == 11:
    answer = "My sources say no."
elif random_number == 12:
    answer = "Very doubtful."
elif random_number == 13:
    answer = "My reply is no."
elif random_number == 14:
    answer = "Outlook not so good."
elif random_number == 15:
    answer = "Lol no."
else:
    answer = "Error"


if name == "":
    print(question)
    print("Magic 8-Ball's answer: ", answer)
elif question == "":
    print("Ask Magic 8-Ball a question: ")
else:
    print("Magic 8-Ball's answer: ", answer)
