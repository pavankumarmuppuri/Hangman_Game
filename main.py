
import random
word_list = ["prepinsta", "prime", "mohan"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
  display += '_'
lives = 6

Hangman_list = [
    """
    x-------x
    """,
    """
    x-------x
    |
    |
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    GAME OVER
    """
]


while '_' in display :
  Guess = input("Enter an alphabet : ")
  guess = Guess.lower()
  for index in range(len(chosen_word)) :
    alphabet = chosen_word[index]
    if alphabet == guess :
      display[index] = guess
  print(display)
  if guess not in chosen_word :
    print(f"{guess} is Not In The Word")
    #print(f"You Have {lives-1} Chances Left")
    print(Hangman_list[-lives])
    lives -= 1
  if lives == 0 :

    print("You Lost The Game")
    print(f"The Correct Word is {chosen_word} ")
    break

while "_" not in display :
  print("Yaay you won the game")
  break


