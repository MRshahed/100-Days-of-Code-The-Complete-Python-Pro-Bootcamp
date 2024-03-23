import random
import Hangman_Words
import Hangman_Art


chosen_word = random.choice(Hangman_Words.word_list)
print(Hangman_Art.logo)
print(f"Chosen Word is: {chosen_word}")
blank = []    
stages = Hangman_Art.stages
lives = 6

for number in range(len(chosen_word)):
    blank+="_"
 
while lives!=0 and "_" in blank:
    answer = input("Choose a Letter: ").lower()
  
    for i in range(len(chosen_word)):
     if chosen_word[i] ==answer:
        blank[i]= answer
    
    if answer in blank:    
      print(blank) 
    else:
      print("You Chose Wrong!")
      lives-=1
      print(stages[lives]) 
   
   
    if lives<0:
        print("Game Over, You Loss!!!")
     
    elif "_" not in blank:
      print("You Won!")
    