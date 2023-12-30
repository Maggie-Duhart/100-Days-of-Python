import random
import game_data

#need to edit clear module 
from replit import clear

from art import logo, vs

print(logo)
#Get the lengts of the data from List
dict_length = len(game_data.data)

#Empy list for future opponents
opponents = []

#Keep track of score
score = 0


def play():
  global score
  #Randomly choose opponent until list has 2 items
  while len(opponents) < 2:
    random_index = random.randint(0, dict_length)
    famous_name = game_data.data[random_index]["name"]
    famous_followers = game_data.data[random_index]["follower_count"]
    famous_info = game_data.data[random_index]["description"]
    famous_country = game_data.data[random_index]["country"]
    option = {
      "name": famous_name,
      "followers_count": famous_followers,
      "description": famous_info,
      "country": famous_country
    }
    #Add item to opponents list
    opponents.append(option)

  #Display option A
  print(
    f"Compare A: {opponents[0]['name']}, a {opponents[0]['description']}, from {opponents[0]['country']} "
  )

  #Display VS art
  print(vs)

  #Display option B
  print(
    f"Against B: {opponents[1]['name']}, a {opponents[1]['description']}, from {opponents[1]['country']} "
  )

  #Ask for input from user to choose who has more followers
  choose = input("Who has more followers? Type 'A' or 'B': ").lower()
  if choose == "a":
    choose = 0
  else:
    choose = 1

  #Access followers values
  followers_A = opponents[0]["followers_count"]
  followers_B = opponents[1]["followers_count"]

  #Compare followers between A and B
  winner = 0
  if followers_A > followers_B:
    winner = followers_A
  else:
    winner = followers_B

  #Find out if user wins
  if opponents[choose]["followers_count"] == winner:
    score += 1
    clear()
    print(logo)
    print(f"You're right! Score: {score}")

    #Remove loser from list
    if choose == 0:
      opponents.pop(1)
    else:
      opponents.pop(0)
    play()
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


play()
