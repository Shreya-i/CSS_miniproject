alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
m = ["VIDYALANKAR","HELLO","PLANT","CIPHER","LAPTOP","SCIENCE","COMPUTER","KEYBOARD","INTELLIGENT","DIGITAL"]
c = ["YLGBDODQNDU","KHOOR","SODQW","FLSKHU","ODSWRS","VFLHQFH","FRPSXWHU","NHBERDUG","LQWHOOLJHQW","GLJLWDO"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
import random
chosen_word = random.choice(m)
index = m.index(chosen_word)
cc_word = c[index]
print(chosen_word)
print("key = 3")
lives =6
print("welcome to cipher hangman")
print("encrypt the given word using caesar cipher")
display = []
for letter in chosen_word:
    display += "_"
print(display)
end_of_game = False

while not end_of_game:
    guess = input("guess a letter: ").upper()
    if guess in display:
       print(f"You've already guessed the letter {guess}")  
    for position in range(len(cc_word)):
      letter = cc_word[position]
      if letter == guess:
        display[position] = letter
    if guess not in cc_word:
       print(f"you guessd {guess}, that'not in the word. you lose a life")
       lives -=1
       if lives == 0:
          end_of_game = True
          print("You lose")
    print(f"{''.join(display)}")
    if "_" not in display:
       end_of_game = True
       print("you win")
       print("you have successfully encrypted the given word")
    print(stages[lives])




