from random import choice


word_list = ["ardvark", "baboon", "camel"]
chosen_word = choice(word_list)
word_length = len(chosen_word)
display = []

print(chosen_word)

for _ in range(word_length):
  display.append("_")

while "_" in display:
  guess = input("Guess a letter: ").lower()
  
  for position in range(word_length):
    letter = chosen_word[position]
    if (guess == letter):
      display[position] = letter

print("You win!")
