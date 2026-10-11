import random

#Using the random function to select a computer number
secret_number = random.randint(1, 50)

#A number is obtained from the user using a loop.
for i in range(1, 6):

    #The user can provide the number using their Input Function.
    user = int(input("Choose any number between 1 and 50. :"))

    #This if statement checks whether the user's number is correct or not.
    if secret_number == user:
        print(f"You are a winner; your chosen number is {user}, and the computer's chosen number is {secret_number}.")
        break
    elif secret_number < user:
        print("Choose a small number.")
    elif secret_number > user:
        print("Choose a large number.")

    #The remaining chances for the user are printed.
    print(f"You have {5 - i} chances left.")

    #If the user completes 5 attempts without finding the answer, this will be printed.
    if i == 5 and user != secret_number:
        print(f"The number selected by the computer is {secret_number}.")