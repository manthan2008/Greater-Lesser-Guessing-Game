import random

print('Welcome to the Greater Lesser Guessing Game\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('How many times do you want to play this game: ')
no_chances_input = int(input())
no_chances = no_chances_input
no_chances_used = 0
user_points = 0
computer_points = 0
 
	
while no_chances > no_chances_used:
	user_input = int(input('Guess Any number from 0 - 20:'))
	computer_input = random.choice(numbers)
	if user_input > 20:
		print('Enter a number between 0-20')

	elif user_input > computer_input:
		print('You got a point\n')
		user_points = user_points + 1
		print(f'Your points are - {user_points}')
		computer_points = computer_points
		print(f'Computer points are - {computer_points}\n')
		print(f'You guessed - {user_input}')
		print(f'Computer guessed - {computer_input}')
		no_chances_used = no_chances_used + 1
		print(f'Chances Used are - {no_chances_used}\n')

	elif user_input < computer_input:
		print('Computer got a point\n')
		user_points = user_points
		print(f'Your points are - {user_points}')
		computer_points = computer_points + 1
		print(f'Computer points are - {computer_points}\n')
		print(f'You guessed - {user_input}')
		print(f'Computer guessed - {computer_input}')
		no_chances_used = no_chances_used + 1
		print(f'Chances Used are - {no_chances_used}\n')

	elif no_chances_used == no_chances:
		print('Game over')
		break

if computer_points > user_points:
	print('Oops... Computer won\n')
	print(f'Computer points are - {computer_points}')
	print(f'Your points are - {user_points}')

elif computer_points < user_points:
	print('Yay... You won\n')
	print(f'Computer points are - {computer_points}')
	print(f'Your points are - {user_points}')

elif computer_points == user_points:
	print('Ohh... It tie\n')
	print(f'Computer points are - {computer_points}')
	print(f'Your points are - {user_points}')

else:
	print('No data..')
