import time
import random
import colorama
from colorama import init, Fore, Back, Style ##everything after this defines the elevator 'story' generation, this similar to how 'Briery' (another project of mine) does it, but I'm using functions instead.
def elewait():
    colwall = random.choice(["white", "dark red", "black", "grey", "dark blue", "dark orange"])  # wall color
    matwall = random.choice(["wooden", "concrete", "stainless steel", "stone"])  # material of the wall
    music = random.choice(["C148's 'Subwoofer Lullaby'", "Frank Sinatra's 'My Way'", "Pink Floyd's 'The Gig in the sky'", "Soothing Elevator Music", "War's 'Why can't we be friends?"])  #music that plays (lol)
    volmusic = random.choice(["Loud", "Soft"])
    luxcolor = random.choice(["soft yellow", "soft white"])
    luxbright = random.choice(["dimly lit", "brightly lit", "extremely bright"])
    roomstatus = random.choice(["has reached a floor", "hasn't reached a floor yet"])  # status of whether the elevator is on a floor or not, very important later.
    elewaitmgen = f"You are standing in a {colwall} colored {matwall} Elevator which {roomstatus}, the elevator lights are {luxbright} with a {luxcolor} shade. The elevator's speakers are playing {music} at a {volmusic} Volume." 
    print(elewaitmgen)
    if roomstatus == "has reached a floor":
        roominput = input("Do you walk out the elevator doors? y/n ")
        if roominput.lower() == 'n':
            elewait()
        elif roominput.lower() == 'y':
            while True:
                elefloor(1)
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    time.sleep(4)  # waits 4 seconds before generating the next 'elewaitmgen' but only if roomstatus is in the 'hasn't reached a floor yet' state.
init()  
def elefloor(current_floor):
    current_floor = 1
    matflwall = random.choice(["stainless steel", "Stone", "Wooden", "Marble", "Concrete", "Log"])
    colfl = random.choice(["White", "Yellow", "Soft Yellow", "Dark Blue", "Soft Blue", "Dark Red", "Soft Red"])
    musicfl = random.choice(["Resonance by home", "Around the world by Daft Punk", "Fortunate Son by CCR", "Gymnopedie by Erik Saite", "Generic Lobby Music", "Dream On By Aerosmith", "Going Down by Jake Chudnow", "It's My Life By The Animals", "Heartaches By Al Bowly", "Less Than by Nine Inch Nails"])
    luxbrightfl = random.choice(["Dimly Lit", "Brightly Lit", "Averagly Lit"])
    flstructure = random.choice(["Mall", "Book Store", "Parking Garage", "Interior Plaza"])
    luxtype = random.choice(["Fluorescent", "Oil", "L.E.D"])
    volmusic2 = random.choice(["Loud", "Quiet", "Comfortable"])
    roomgenif = random.choice(["There is a room which you can enter that is located", "There is no room, you can continue to walk"])
    directiongen = random.choice(["left", "right"])
    elefloorgen = f"you are now located in a {colfl} {flstructure}. The {flstructure} has {luxbrightfl} {luxtype} lights. On the speakers, {musicfl} is playing at a {volmusic2} volume. {roomgenif} to your {directiongen}"
    print(Back.BLACK + elefloorgen + Back.RESET)
    if roomgenif == "There is a room which you can enter that is located":
        eleroomstatus = input("Do you enter the room (y/n) ")
        if eleroomstatus.lower() == 'n':
            elefloor(1) #patchnote1.2.6: this was all that was in this update really, and line 40
        elif eleroomstatus.lower() == 'y':
            eleroom() #works

    time.sleep(5) #does same thing as 'time.sleep(4)' on line 24.
def eleroom():
  roomtype = random.choice(["Hotel", "Hostel", "Lounge"])
  yearoomtype = random.choice(["1950s", "1960s", "1940s", "1930s"])
  musicrm = random.choice(["La Vie en rose by Louis Armstrong", "100 Years by Clover", "La Campanella by Chopin", "House of the Rising sun by The Animals", "It's just a burning memory by The Caretaker", "Libet's Delay by The Caretaker", "Betryal by Light", "The Existential Threat by Sparks", "Dead Weight by Jack Stauber", "Hello, World! by Louie Zong", "Mr. Sandman by The Chordettes"])
  musicplayrm = random.choice(["1950s Jukebox", "1930s Radio", "1930s Vinyl Record player", "Casette Player", "Discarded iPod"])
  colrm = random.choice(["White", "Yellow", "Soft Yellow", "Dark Blue", "Light Blue", "Dark Red", "Light Red"])
  rmwall = random.choice(["Wallpaper", "Vinyl", "Marble", "Wood"])
  luxtyperm = random.choice(["Oil", "Flourescent", "Incandescent", "Neon"])
  eleroomgen = f"you enter a {yearoomtype} {colrm} {roomtype}, the {roomtype} has {colrm} {rmwall} walls and {luxtyperm} lights, a {musicplayrm} is playing {musicrm}."
  print(eleroomgen)
  roomele = input("Do you exit the room (y/n) ")
  if roomele.lower() == 'n':
    print("You stay in the room")
   
  elif roomele.lower() == 'y':
    elefloor(1)
print(Back.BLACK + "A INFINITE ELEVATOR GAME" + Back.RESET)
print(Back.RED + "CREATED BY rayDEVL" + Back.RESET)
print(Back.BLACK + "STARTED ON 6/4/23" + Back.RESET)
print(Back.RED + "YOUR GAME WILL START IN 5 SECONDS" + Back.RESET)
print(Back.BLACK + "-----------------------" + Back.RESET)
print(Back.WHITE + "v1.2.8" + Back.RESET)
time.sleep(5)
while True:
    elewait()
