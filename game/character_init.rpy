#Character Images Start
#MC Images

image mc:
    "images/characters/inui/home_neutral.png"
    zoom 0.5
    
image mc dog:
    "images/characters/inui/dog_neutral.png"
    zoom 0.5

#image mc= im.FactorScale("images/characters/inui/home_neutral.png" zoom 0.0
#image mc dog= im.FactorScale("images/characters/inui/dog_neutral.png" zoom 0.0
image mc dog happy:
    "images/characters/inui/dog_hungry_happy.png"
    zoom 0.5
image mc dog hungry:
    "images/characters/inui/dog_hungry_happy.png"
    zoom 0.5
image mc dog confused:
    "images/characters/inui/dog_confused.png"
    zoom 0.5
image mc dog sad:
    "images/characters/inui/dog_sad.png"
    zoom 0.5
image mc angry:
    "images/characters/inui/home_angry.png"
    zoom 0.5
image mc confused:
    "images/characters/inui/home_confused.png"
    zoom 0.5
image mc happy:
    "images/characters/inui/home_happy.png"
    zoom 0.5
image mc neutral:
    "images/characters/inui/home_neutral.png"
    zoom 0.5
image mc sad:
    "images/characters/inui/home_sad.png"
    zoom 0.5
image mc surprised:
    "images/characters/inui/home_surprised.png"
    zoom 0.5
image mc school angry:
    "images/characters/inui/school_angry.png"
    zoom 0.5
image mc school confused:
    "images/characters/inui/school_confused.png"
    zoom 0.5
image mc school happy:
    "images/characters/inui/school_happy.png"
    zoom 0.5
image mc school neutral:
    "images/characters/inui/school_neutral.png"
    zoom 0.5
image mc school sad:
    "images/characters/inui/school_sad.png"
    zoom 0.5
image mc school surprised:
    "images/characters/inui/school_surprised.png"
    zoom 0.5

#Claudia Catebury
image claudia angry:
    "images/characters/claudia_catebury/angry.png"
    zoom 0.5
image claudia annoyed:
    "images/characters/claudia_catebury/annoyed.png" 
    zoom 0.5
image claudia happy:
    "images/characters/claudia_catebury/happy.png" 
    zoom 0.5
image claudia neutral:
    "images/characters/claudia_catebury/neutral_smug.png" 
    zoom 0.5
image claudia surprised:
    "images/characters/claudia_catebury/surprised.png" 
    zoom 0.5

#Dimitri Hatter
image dimitri neutral:
    "images/characters/Dimitri_Hatter/neutral.png" 
    zoom 0.5
image dimitri sad disappointed:
    "images/characters/Dimitri_Hatter/sad_disappointed.png" 
    zoom 0.5
image dimitri sad pensive:
    "images/characters/Dimitri_Hatter/sad_pensive.png" 
    zoom 0.5
image dimitri surprised:
    "images/characters/Dimitri_Hatter/surprised.png" 
    zoom 0.5

#Fabien LeBlanc
image fabien neutral:
    "images/characters/fabien_leblanc/neutral.png" 
    zoom 0.5

#Leveret LeBlanc
image leveret neutral:
    "images/characters/leveret_leblanc/neutral.png" 
    zoom 0.5
image leveret annoying:
    "images/characters/leveret_leblanc/annoying.png" 
    zoom 0.5
image leveret happy:
    "images/characters/leveret_leblanc/happy.png" 
    zoom 0.5
image leveret sad:
    "images/characters/leveret_leblanc/sad.png" 
    zoom 0.5
image leveret surprised:
    "images/characters/leveret_leblanc/surprise.png" 
    zoom 0.5

#Mathilda Images
image mathilda:
    "images/characters/mathilda/neutral.png" 
    zoom 0.5
image mathilda happy:
    "images/characters/mathilda/happy.png" 
    zoom 0.5
image mathilda sad pensive:
    "images/characters/mathilda/sad_pensive.png" 
    zoom 0.5
image mathilda sad resigned:
    "images/characters/mathilda/sad_resigned.png" 
    zoom 0.5
image mathilda stern:
    "images/characters/mathilda/stern.png" 
    zoom 0.5

#Mira Shelbrooke
image mira happy:
    "images/characters/mira_shelbrooke/happy.png" 
    zoom 0.5
image mira neutral:
    "images/characters/mira_shelbrooke/neutral.png" 
    zoom 0.5

#Tatianna Rosehart
image tatianna angry:
    "images/characters/tatianna_rosehart/angry.png" 
    zoom 0.5
image tatianna neutral stern:
    "images/characters/tatianna_rosehart/neutral_stern.png" 
    zoom 0.5


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

#Bringing in CGs
image transformation cg = "images/cgs/transformation_cg.jpg"
image hug cg = "images/cgs/hug_cg.jpg"
image breakfast cg = "images/cgs/breakfast_cg.jpg"

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