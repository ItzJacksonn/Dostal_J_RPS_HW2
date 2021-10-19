from random import randint

playerScore = 0
computerScore = 0

print("Welcome to the Rock, Paper, Scissors Game.")
print("First to three points wins")
print("--------------------------------------------")

if (playerScore == 3):
	print("Congratulaions, You Won The Game")
elif (computerScore == 3):
	print("Sorry, You Lost The Game")
else:
	player = input("Choose rock, paper, or scissors: ")
	print("Player chose: " + player)

	choices = ["rock", "paper", "scissors"]
	computer = choices[randint(0,2)]
	print("Computer chose: " + computer)

	if (computer == player):
		print("Its A Tie!")
	elif (player == "rock"):
		if (computer == "scissors"):
			print("Player wins!")
			playerScore = playerScore + 1
		else:
			print("Computer wins!")
			computerScore = computerScore + 1
	elif (player == "paper"):
		if (computer == "rock"):
			print("Player wins!")
			playerScore = playerScore + 1
		else:
			print("Computer wins!")
			computerScore = computerScore + 1
	elif (player == "scissors"):
		if (computer == "paper"):
			print("Player wins!")
			playerScore = playerScore + 1
		else:
			print("Computer wins!")
			computerScore = computerScore + 1

print("Player score is " + str(playerScore))
print("Computer score is " + str(computerScore))
