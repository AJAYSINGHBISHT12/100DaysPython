import random
list = ["mayank", "ajay","ayush"]
# # Todo 1 - Randomly choose a word from the list and assign it to variable called chosed word. then print it
chosen_word= random.choice(list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder +="_"

print(placeholder)
# # Todo 2 - Ask the user to enter the letter . and make it to lowercase

# for i in range(word_length + 1):
game_over = False
correct_letters = []
while not game_over:
    guess=input("Guess a letter:").lower()
# print(guess)

    display = ""
# # Todo 3- Check if the letter the user guessed is one of the letters in the chosen word. Print "Right"
    for letter in chosen_word:
        if letter == guess:
           display +=letter
           correct_letters.append(guess)
        elif letter in correct_letters:
            display +=letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("you Win!")
#todo 1- Create a "placeholder" with the same number of blanks as the chosen_word
# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder +="_"
#
# print(placeholder)

# todo 2- Create a "display" that puts the guess letter in the right position and _ in