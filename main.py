# THIS IS EXAMPLE



print('Welcome to Rock, Paper, Scissors!')

user_choice = input('Enter rock, paper, or scissors:').lower()

     
valid_choices = ['rock', 'paper', 'scissors']
if user_choice not in valid_choices:
    print("Oops! That's not a valid move. Please try again next time.")
    exit()


computer_choice = 'Rock'


print(f'Computer chose: {computer_choice}')

print(f'You chose: {user_choice}')


result = ''


if user_choice == computer_choice:
    result+='Draw!'
elif user_choice == 'rock' and computer_choice == 'scissors':
    result+='You win!'
elif user_choice == 'scissors' and computer_choice =='paper':
    result+='You win!'
elif user_choice == 'paper' and computer_choice =='rock':
    result+='You win!'
else:
    result+='You lose!'
print(result)