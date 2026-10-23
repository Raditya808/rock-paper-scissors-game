print('Welcome to Rock, Paper, Scissors!')

user_choice = input('Enter rock, paper, or scissors:')

computer_choice = 'rock'


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