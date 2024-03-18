import random

number_of_games = int(input(
    "Please enter the number of rounds you would like to play: "))

weapon_options = ["rock", "paper", "scissors"]

games_played = 0
computer_wins = 0
player_wins = 0

while games_played < number_of_games:
    player_choice = input(
        "Please enter your selection of rock paper or scissors: ").lower()

    if player_choice not in weapon_options:
        print("Invalid weapon, please try again")
        continue

    computer_choice = random.choice(weapon_options)
    print(f"You chose {player_choice} and I chose {computer_choice}.")

    if computer_choice == player_choice:
        print("We shall replay this point!")
        continue
    elif (player_choice == "rock" and computer_choice == "paper"
          or player_choice == "paper" and computer_choice == "scissors"
          or player_choice == "scissors" and computer_choice == "rock"
          ):
        computer_wins += 1
        print("I win this round")
    else:
        player_wins += 1
        print("You win this round")

    games_played += 1

print(f"You have won {player_wins} rounds and I have won {
      computer_wins} rounds.")
if player_wins > computer_wins:
    print("Congratulations, you have won overall!")
elif player_wins < computer_wins:
    print("Yay I have won overall!")
else:
    print("It's a draw overall!")
