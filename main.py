import art
import random
from game_data import data 
from replit import clear



Compare_A = []
Against_B = []
score = 0

def random_order():
  list = []
  for i in range(len(data)):
    list.append(i)
  random.shuffle(list)
  return list
  

def add_score():
  global score
  score += 1
  return score


def pick_A_or_B():  

  correct_type = True
  while correct_type:
      
    A_or_B = input("Who has more followers? Type 'A' or 'B' ")
    if A_or_B == 'A' or A_or_B == 'a':
      return 'A'
      correct_type = False
    elif A_or_B == 'B' or A_or_B == 'b':
      return 'B'
      correct_type = False
    else:
      print("Wrong Type. Try again.")

def compare(followers_1, followers_2, pick_one):

    followers_1 = followers_1['follower_count']
    followers_2 = followers_2['follower_count']
    
    if pick_one == 'A':
      the_pick_one = followers_1

    elif pick_one == 'B':
      the_pick_one = followers_2
  
  
    if the_pick_one == max(followers_1, followers_2):           
      add_score()
      return True
    else:
      print("O-oh. You lose. 😤😤😤")
      print(f"You got {score}!!! 😎😎😎")
      
      return False


def play_game(): 
  
  list = random_order()
  game = 0
  game_over = False
  while not game_over:
    clear()
    
    print(art.logo)  
    print(f"Level: {game + 1} ",👾"*(game + 1))
      
    followers_1 = data[list[game]]
    followers_2 = data[list[game + 1]]
    
    print(f"Campare A: {followers_1['name']}\nDescription: {followers_1['description']} from {followers_1['country']} \nthey have {followers_1['follower_count']} followers")
    
    
    print(art.vs)
    
    print(f"Against B: {followers_2['name']}\nDescription: {followers_2['description']} from {followers_2['country']}")

    pick_one = pick_A_or_B()

    guess_correct = compare(followers_1, followers_2, pick_one)
    if guess_correct:
      game += 1
    else:
      game_over = True
      print(f"they have {followers_2['follower_count']} followers")

   
while input("Wanna play a game? 👾 type 'y' start the game ") == 'y':
  clear()
  play_game()

