# The script of the game goes in this file.

#Character Images
image mc= im.FactorScale("images/characters/inui/home_neutral.png", 0.5)
image mc dog= im.FactorScale("images/characters/inui/dog_neutral.png", 0.5)
image mc dog happy=im.FactorScale("images/characters/inui/dog_hungry_happy.png", 0.5)
image mc dog hungry=im.FactorScale("images/characters/inui/dog_hungry_happy.png", 0.5)
image mc dog confused=im.FactorScale("images/characters/inui/dog_confused.png", 0.5)
image mc dog sad=im.FactorScale("images/characters/inui/dog_sad.png", 0.5)
#Mathilda Images
image mathilda= im.FactorScale("images/characters/mathilda/neutral.png", 0.5)
image mathilda happy=im.FactorScale("images/characters/mathilda/happy.png", 0.5)
image mathilda sad pensive=im.FactorScale("images/characters/mathilda/sad_pensive.png", 0.5)
image mathilda sad resigned=im.FactorScale("images/characters/mathilda/sad_resigned.png", 0.5)
image mathilda stern=im.FactorScale("images/characters/mathilda/stern.png", 0.5)

#background images
#TODO: Bring the background up after the transformation CG
image blank = "images/backgrounds/blank.jpg"
image mathildas house= "images/backgrounds/mysterious_mathilda_s_house.jpg"

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define pov = Character("[povname]", kind=adv, image="mc")                     # The player character
define n = Character("")                                # The narrator
define mathilda = Character("mathilda_name", kind=adv, image="mathilda", dynamic=True)   # Mathilda

define fabien = Character("Fabien LeBlanc")             # Fabien LeBlanc
define tatianna = Character("tatianna_name", dynamic=True)
define levy = Character("levy_name", dynamic=True)
define mira = Character("mira_name", dynamic=True)
define claudia = Character("claudia_name", dynamic=True)
define unknown = Character("???")
define follow1 = Character("Follower 1")
define follow2 = Character("Follower 2")
define girl1 = Character("Girl Student 1")
define girl2 = Character("Girl Student 2")
define girl3 = Character("Girl Student 3")
define girl4 = Character("Girl Student 4")