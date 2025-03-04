import random

word_list = ['hand', 'cobra', 'elbow', 'dog', 'snake', 'copy', 'subway', 'key']
word = random.choice(word_list)
print(f'Hint: Number of letter in word = {len(word)}')

blank_list = []
for i in range(len(word)):
    blank_list += '_' # will place a "_" in place of every letter.
level=input("Enter the mode: (Easy, Medium, Hard): ").title()  # Difficulty selector
if level == "Easy":
    lives = 6
elif level == "Medium":
    lives = 4
else:
    lives = 1
    game_over = False  
    while not game_over:   # game continues until game over is true
        guess_letter = input("Enter the letter: ").lower()

        for i in range(len(word)):  # will loop through every letter of word
            if i == guess_letter:  
          
                letter = word.index(guess_letter)
                blank_list[letter] = guess_letter
                print(blank_list)   # will place guessed letter in place of "_"

        if guess_letter not in word:  # if guessed letter is not in word
            lives -= 1
            if lives == 0:
                game_over = True
                print("You Lose!")

        if '_' not in blank_list:
            game_over = True
            print(f"You Win!! in the {level} mode")

        if lives== 0:
            print(f"You lose the game. the word was {word}")
            game_over= True

print("Thanks for playing!")

        