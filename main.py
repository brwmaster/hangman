from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

print(f"{logo} \n")
word_list = ["ardvark", "baboon", "camel"]
chosen_word = choice(word_list)
word_length = len(chosen_word)
display = []
end_of_game = False
lives = 6
guessed_letters = []

for _ in range(word_length):
  display.append("_")

while not end_of_game:
  guess = input("Guess a letter: ").lower()
 

  if not guess in guessed_letters:
    guessed_letters.append(guess)
    # check if guessed letter is in the chosen_word
    for position in range(word_length):
      letter = chosen_word[position]
      if (guess == letter):
        display[position] = letter
    
    print(f"\n {' '.join(display)} \n")

    # if guess is not in chosen_word lose a life
    # when lives = 0 end the game
    if not guess in chosen_word:
      lives -= 1
      print(f"\n The letter {guess} is not in the word. You have {lives} lives left")
      if lives == 0:
        print("You lose!")
        end_of_game = True

    # if all the blanks are filled you win the game
    if not "_" in display:
      end_of_game = True
      print("You win!")
    
    print(f"{stages[lives]} \n")
  else:
    print(f"\nYou already tried the letter {guess} \n")

  

