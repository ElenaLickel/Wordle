game_word = 'hello'
game_word = list(game_word)
print(game_word)
guess = list(input('Guess: '))
print(f'your guess was{guess}')

if guess == game_word:
    print('correct')


