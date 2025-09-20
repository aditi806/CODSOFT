import random

print("------ROCK PAPER SCISSOR------")
user = 0
computer = 0

choices = ['rock', 'paper', 'scissor']

while True:
    user_input = input("\nchoose Rock, Paper, or scissor: ").lower()

    if user_input not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer : {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")
    elif ((user_input == 'rock'and computer_choice == 'scissor')or
          (user_input == 'paper' and computer_choice == 'rock')or
          (user_input == 'scissor' and computer_choice == 'paper')
          ):
        print("YOU WIN!!")
        user+=1
    else:
        print("Computer WINS!")
        computer+=1

    again = input("Play again? (yes?no): ").lower()
    if again != 'yes':
        break
print("Thanks for playing! Final score:")
print(f"You: {user} | Computer: {computer}")

    

