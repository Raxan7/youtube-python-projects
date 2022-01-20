import random
import pyttsx3

engine = pyttsx3.init()
print("Welcome to our Rock, Paper, Scissors Game")
engine.setProperty('rate', 150)
engine.say("Welcome to our Rock, Paper, Scissors Game")
engine.runAndWait()

choices = ['R', 'P', 'S']
computer_choice = random.choice(choices)
player_choice = input("Play > ")

if computer_choice == 'R' and player_choice.upper() == 'S':
    print(f"The computer went for {computer_choice}, The computer beat you!")
    text = f"The computer went for {computer_choice}, The computer beat you!"
    engine.say(text)
    engine.runAndWait()
elif computer_choice == 'P' and player_choice.upper() == 'R':
    print(f"The computer went for {computer_choice}, The computer beat you!")
    text = f"The computer went for {computer_choice}, The computer beat you!"
    engine.say(text)
    engine.runAndWait()
elif computer_choice == 'S' and player_choice.upper() == 'P':
    print(f"The computer went for {computer_choice}, The computer beat you!")
    text = f"The computer went for {computer_choice}, The computer beat you!"
    engine.say(text)
    engine.runAndWait()
elif player_choice.upper() == 'R' and computer_choice == 'S':
    print(f"The computer went for {computer_choice}, You won, Congrats for beating the intelligent computer!")
    text = f"The computer went for {computer_choice}, You won, Congrats for beating the intelligent computer!"
    engine.say(text)
    engine.runAndWait()
elif player_choice.upper() == 'P' and computer_choice == 'R':
    print(f"The computer went for {computer_choice}, You won, Congrats for beating the intelligent computer!")
    text = f"The computer went for {computer_choice}, You won, Congrats for beating the intelligent computer!"
    engine.say(text)
    engine.runAndWait()
elif player_choice.upper() == 'S' and computer_choice == 'P':
    print(f"The computer went for {computer_choice}, You won, Congrats for beating the intelligent computer!")
    text = f"The computer went for {computer_choice}, You won, Congrats for beating the intelligent computer!"
    engine.say(text)
    engine.runAndWait()
else:
    print("Check the rules and try again")
    text = "Check the rules and try again"
    engine.say(text)
    engine.runAndWait()
