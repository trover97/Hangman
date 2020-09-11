# Write your code here
import random

state = ("play", "exit")
menu = ''
e = 0
errors = ('', 'You already typed this letter', 'It is not an ASCII lowercase letter'
          , 'You should input a single letter')
words = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(words)
g_word = []
[g_word.append('-') for c in word]
attempts = 8
dou = ''

print('H A N G M A N')
while menu != 'exit':
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu not in state or menu == 'exit':
        continue
    while attempts:
        print()
        print(''.join(g_word))
        letter = input('Input a letter: ')
        e = 0

        if len(letter) != 1:
            e = 3
        elif not (letter.isalpha() and letter.islower()):
            e = 2
        elif letter in dou:
            e = 1

        if e != 0:
            print(errors[e])
            continue
        dou += letter
        if '-' not in g_word:
            break
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    g_word[i] = letter
        else:
            print('No such letter in the word')
            attempts -= 1
    print("You are hanged!" if attempts == 0 else 'You guessed the word!\nYou survived!')
