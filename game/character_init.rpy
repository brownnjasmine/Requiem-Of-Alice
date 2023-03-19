#Character Images Start
#MC Images
image mc= im.FactorScale("images/characters/inui/home_neutral.png", 0.5)
image mc dog= im.FactorScale("images/characters/inui/dog_neutral.png", 0.5)
image mc dog happy=im.FactorScale("images/characters/inui/dog_hungry_happy.png", 0.5)
image mc dog hungry=im.FactorScale("images/characters/inui/dog_hungry_happy.png", 0.5)
image mc dog confused=im.FactorScale("images/characters/inui/dog_confused.png", 0.5)
image mc dog sad=im.FactorScale("images/characters/inui/dog_sad.png", 0.5)
image mc home angry=im.FactorScale("images/characters/inui/home_angry.png", 0.5)
image mc home confused=im.FactorScale("images/characters/inui/home_confused.png", 0.5)
image mc home happy=im.FactorScale("images/characters/inui/home_happy.png", 0.5)
image mc home neutral=im.FactorScale("images/characters/inui/home_neutral.png", 0.5)
image mc home sad=im.FactorScale("images/characters/inui/home_sad.png", 0.5)
image mc home surprised=im.FactorScale("images/characters/inui/home_surprised.png", 0.5)
image mc school angry=im.FactorScale("images/characters/inui/school_angry.png", 0.5)
image mc school confused=im.FactorScale("images/characters/inui/school_confused.png", 0.5)
image mc school happy=im.FactorScale("images/characters/inui/school_happy.png", 0.5)
image mc school neutral=im.FactorScale("images/characters/inui/school_neutral.png", 0.5)
image mc school sad=im.FactorScale("images/characters/inui/school_sad.png", 0.5)
image mc school surprised=im.FactorScale("images/characters/inui/school_surprised.png", 0.5)

#Claudia Catebury
image claudia angry=im.FactorScale("images/characters/claudia_catebury/angry.png", 0.5)
image claudia annoyed=im.FactorScale("images/characters/claudia_catebury/annoyed.png", 0.5)
image claudia happy=im.FactorScale("images/characters/claudia_catebury/happy.png", 0.5)
image claudia neutral=im.FactorScale("images/characters/claudia_catebury/neutral_smug.png", 0.5)
image claudia surprised=im.FactorScale("images/characters/claudia_catebury/surprised.png", 0.5)
#Dimitri Hatter
image dimitri neutral=im.FactorScale("images/characters/Dimitri_Hatter/neutral.png", 0.5)
image dimitri sad disappointed=im.FactorScale("images/characters/Dimitri_Hatter/sad_disappointed.png", 0.5)
image dimitri sad pensive=im.FactorScale("images/characters/Dimitri_Hatter/sad_pensive.png", 0.5)
image dimitri surprised=im.FactorScale("images/characters/Dimitri_Hatter/surprised.png", 0.5)
#Fabien LeBlanc
image fabien neutral=im.FactorScale("images/characters/fabien_leblanc/neutral.png", 0.5)
#Leveret LeBlanc
image leveret annoying=im.FactorScale("images/characters/leveret_leblanc/annoying.png", 0.5)
image leveret happy=im.FactorScale("images/characters/leveret_leblanc/happy.png", 0.5)
image leveret sad=im.FactorScale("images/characters/leveret_leblanc/sad.png", 0.5)
image leveret surprise=im.FactorScale("images/characters/leveret_leblanc/surprise.png", 0.5)
#Mathilda Images
image mathilda= im.FactorScale("images/characters/mathilda/neutral.png", 0.5)
image mathilda happy=im.FactorScale("images/characters/mathilda/happy.png", 0.5)
image mathilda sad pensive=im.FactorScale("images/characters/mathilda/sad_pensive.png", 0.5)
image mathilda sad resigned=im.FactorScale("images/characters/mathilda/sad_resigned.png", 0.5)
image mathilda stern=im.FactorScale("images/characters/mathilda/stern.png", 0.5)
#Mira Shelbrooke
image mira happy=im.FactorScale("images/characters/mira_shelbrooke/happy.png", 0.5)
image mira neutral=im.FactorScale("images/characters/mira_shelbrooke/neutral.png", 0.5)
#Tatianna Rosehart
image tatianna angry=im.FactorScale("images/characters/tatianna_rosehart/angry.png", 0.5)
image tatianna neutral stern=im.FactorScale("images/characters/tatianna_rosehart/neutral_stern.png", 0.5)


#background images start
#TODO: Bring the background up after the transformation CG
image blank = "images/backgrounds/blank.jpg"
image cafeteria= "images/backgrounds/cafeteria.jpg"
image chess club="images/backgrounds/chess_club.jpg"
image garden club="images/backgrounds/garden_club.jpg"
image hallway= "images/backgrounds/hallway.jpg"
image library= "images/backgrounds/library.jpg"
image math classroom= "images/backgrounds/math_classroom.jpg"
image mcs bedroom= "images/backgrounds/mc_bedroom.jpg"
image mathildas house= "images/backgrounds/mysterious_mathilda_s_house.jpg"
image school entrance= "images/backgrounds/school_entrance_.jpg"
image spade dorm hallway= "images/backgrounds/spade_dorm_hallway.jpg"
image spade dorms= "images/backgrounds/spade_dorms.jpg"
image tea club= "images/backgrounds/tea_club.jpg"

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define pov = Character("[povname]", kind=adv, image="mc")                     # The player character
define n = Character("")                                # The narrator
define mathilda = Character("mathilda_name", kind=adv, image="mathilda", dynamic=True)   # Mathilda

define fabien = Character("Fabien LeBlanc", kind=adv, image="fabien")             # Fabien LeBlanc
define tatianna = Character("tatianna_name", kind=adv, image="tatianna", dynamic=True)
define levy = Character("levy_name", kind=adv, image="leveret",dynamic=True)
define mira = Character("mira_name", kind=adv, image="mira", dynamic=True)
define claudia = Character("claudia_name", kind=adv, image="claudia", dynamic=True)
define unknown = Character("???")
define follow1 = Character("Follower 1")
define follow2 = Character("Follower 2")
define girl1 = Character("Girl Student 1")
define girl2 = Character("Girl Student 2")
define girl3 = Character("Girl Student 3")
define girl4 = Character("Girl Student 4")