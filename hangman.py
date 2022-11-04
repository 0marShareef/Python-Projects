import random

hang = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
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
 /|   |
      |
      |
=========''', '''
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
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()
lives = 0
word = random.choice(word_list)
blanks = []
for i in word:
    blanks += '_'
print(blanks)
while True:
    guess = input("Guess a letter:").lower()
    for i in range(len(word)):
        if word[i] == guess:
            blanks[i] = guess
    print(blanks)
    if "".join(blanks) == word:
        print("You win!")
        break
    if guess not in word:
        print(hang[lives])
        lives += 1
    if lives == 7:
        print("You lose!")
        print(f"The word was {word}.")
        break
