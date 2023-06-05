import os
import time
import random
import colorama
from colorama import init, Fore, Back, Style


##everything after this defines the elevator 'story' generation, this similar to how 'Briery' (another project of mine) does it, but I'm using functions instead.
def elewait(
):  #defines a elewait function, this is the elevator slowly going down the several floors before arriving at one which will be defined by 'elefloor' which will lead to rooms which will then be defined by a 'eleroom' function
  colwall = random.choice(
    ["white", "dark red", "black", "grey", "dark blue",
     "dark orange"])  #wall color
  matwall = random.choice(["wooden", "concrete", "stainless steel",
                           "stone"])  #material of the wall
  music = random.choice([
    "C148's 'Subwoofer Lullaby'", "Frank Sinatra's 'My Way'",
    "Pink Floyd's 'The Gig in the sky'", "Soothing Elevator Music",
    "War's 'Why can't we be friends?"
  ])  #music that plays (lol)
  volmusic = random.choice(["Loud", "Soft"])
  luxcolor = random.choice([
    "soft yellow",
    "soft white",
  ])
  luxbright = random.choice(["dimly lit", "brightly lit", "extremely bright"])
  roomstatus = random.choice(
    ["has reached a floor", "hasn't reached a floor yet"]
  )  #status of weather the elevator is on a floor or not, very important later.
  elewaitmgen = f"You are standing in a {colwall} colored {matwall} Elevator which {roomstatus}, the elevator lights are {luxbright} with a {luxcolor} shade. the elevator's speakers are playing {music} at a {volmusic} Volume."
  print(elewaitmgen)
  if roomstatus == "has reached a floor":
    roominput = input("Do you walk out the elevator doors? y/n ")
    if roominput.lower() == 'n':
      elewait()
    elif roominput.lower() == 'y':
      while True:
        elefloor()
    else:
      print("Invalid input. Please enter 'y' or 'n'.")
  time.sleep(
    4
  )  #waits 4 seconds before generating next 'elewaitmgen' but only if roomstatus is in the 'hasn't reached a floor yet' state.


init()


def elefloor():  #defines the 'floor' which wil be generated when you say 'y'
  matflwall = random.choice(
    ["stainless steel", "Stone", "Wooden", "Marble", "Concrete", "Log"])
  colfl = random.choice([
    "White", "Yellow", "Soft Yellow", "Dark Blue", "Soft Blue", "Dark Red",
    "Soft Red"
  ])
  luxcolfl = random.choice([
    "White", "Yellow", "Soft Yellow", "Dark Blue", "Soft Blue", "Dark Red",
    "Soft Red"
  ])  ##the colfl's are needed to be seperate I swear!11!
  musicfl = random.choice([
    "Resonance by home", "Around the world by Daft Punk",
    "Fortunate Son by CCR", "Gymnopedie by Erik Saite", "Generic Lobby Music",
    "Dream On By Aerosmith", "Going Down by Jake Chudnow",
    "It's My Life By The Animals", "Heartaches By Al Bowly",
    "Less Than by Nine Inch Nails"
  ])
  luxbrightfl = random.choice(["Dimly Lit", "Brightly Lit", "Averagly Lit"])
  flstructure = random.choice(
    ["Mall", "Book Store", "Parking Garage", "Interior Plaza"])
  luxtype = random.choice(["Flourescent", "Oil", "L.E.D"])
  volmusic2 = random.choice(["Loud", "Quiet", "Comfortable"])
  elefloorgen = f"you have stepped out of the elevator and are located in a {colfl} {matflwall} {flstructure}, the {flstructure} has a series of 5 {luxbrightfl} {luxtype} lights. on the speakers {musicfl} is playing at a {volmusic2} volume."
  print(Back.BLACK + elefloorgen + Back.RESET) 
  time.sleep(5)
print(Back.BLACK + "A INFINITE ELEVATOR GAME" + Back.RESET)
print(Back.RED + "CREATED BY rayDEVL" + Back.RESET)
print(Back.BLACK + "STARTED ON 6/4/23" + Back.RESET)
print(Back.RED + "YOUR GAME WILL START IN 5 SECONDS" + Back.RESET)
print(Back.BLACK + "-----------------------" + Back.RESET)
time.sleep(5)
while True:
  elewait()
