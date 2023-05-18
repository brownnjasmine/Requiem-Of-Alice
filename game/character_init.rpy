#Character Images Start
#MC Images

image mc:
    "images/characters/inui/home_neutral.png"
    
    
image mc dog:
    "images/characters/inui/dog_neutral.png"
    yalign 0.65
    zoom 0.4
    

#image mc= im.FactorScale("images/characters/inui/home_neutral.png" zoom 0.0
#image mc dog= im.FactorScale("images/characters/inui/dog_neutral.png" zoom 0.0
image mc dog happy:
    "images/characters/inui/dog_hungry_happy.png"
    zoom 0.4
    yalign 0.65
    
image mc dog hungry:
    "images/characters/inui/dog_hungry_happy.png"
    zoom 0.4
    yalign 0.65
    
image mc dog confused:
    "images/characters/inui/dog_confused.png"
    zoom 0.4
    yalign 0.65
    
image mc dog sad:
    "images/characters/inui/dog_sad.png"
    zoom 0.4
    yalign 0.65
    
image mc angry:
    "images/characters/inui/home_angry.png"
    
image mc confused:
    "images/characters/inui/home_confused.png"
    
image mc happy:
    "images/characters/inui/home_happy.png"
    
image mc neutral:
    "images/characters/inui/home_neutral.png"
    
image mc sad:
    "images/characters/inui/home_sad.png"
    
image mc surprised:
    "images/characters/inui/home_surprised.png"
    
image mc school angry:
    "images/characters/inui/school_angry.png"
    
image mc school confused:
    "images/characters/inui/school_confused.png"
    
image mc school happy:
    "images/characters/inui/school_happy.png"
    
image mc school neutral:
    "images/characters/inui/school_neutral.png"
    
image mc school sad:
    "images/characters/inui/school_sad.png"
    
image mc school surprised:
    "images/characters/inui/school_surprised.png"
    

#Claudia Catebury
image claudia angry:
    "images/characters/claudia_catebury/angry.png"
    
image claudia annoyed:
    "images/characters/claudia_catebury/annoyed.png" 
    
image claudia happy:
    "images/characters/claudia_catebury/happy.png" 
    
image claudia neutral:
    "images/characters/claudia_catebury/neutral_smug.png" 
    
image claudia surprised:
    "images/characters/claudia_catebury/surprised.png" 
    

#Dimitri Hatter
image dimitri neutral:
    "images/characters/Dimitri_Hatter/neutral.png" 
    
image dimitri sad disappointed:
    "images/characters/Dimitri_Hatter/sad_disappointed.png" 
    
image dimitri sad pensive:
    "images/characters/Dimitri_Hatter/sad_pensive.png" 
    
image dimitri surprised:
    "images/characters/Dimitri_Hatter/surprised.png" 
    

#Fabien LeBlanc
image fabien neutral:
    "images/characters/fabien_leblanc/neutral.png" 
    

#Leveret LeBlanc
image leveret neutral:
    "images/characters/leveret_leblanc/neutral.png" 
    
image leveret annoying:
    "images/characters/leveret_leblanc/annoying.png" 
    
image leveret happy:
    "images/characters/leveret_leblanc/happy.png" 
    
image leveret sad:
    "images/characters/leveret_leblanc/sad.png" 
    
image leveret surprised:
    "images/characters/leveret_leblanc/surprise.png" 
    

#Mathilda Images
image mathilda:
    "images/characters/mathilda/neutral.png" 
    
image mathilda happy:
    "images/characters/mathilda/happy.png" 
    
image mathilda sad pensive:
    "images/characters/mathilda/sad_pensive.png" 
    
image mathilda sad resigned:
    "images/characters/mathilda/sad_resigned.png" 
    
image mathilda stern:
    "images/characters/mathilda/stern.png"
    zoom 0.5
    

#Mira Shelbrooke
image mira happy:
    "images/characters/mira_shelbrooke/happy.png" 
    
image mira neutral:
    "images/characters/mira_shelbrooke/neutral.png" 
    

#Tatianna Rosehart
image tatianna angry:
    "images/characters/tatianna_rosehart/angry.png" 
    
image tatianna neutral stern:
    "images/characters/tatianna_rosehart/neutral_stern.png" 
    


#background images start
#TODO: Bring the background up after the transformation CG
image blank = "images/backgrounds/blank.jpg"
image cafeteria= "images/backgrounds/cafeteria.png"
image chess club="images/backgrounds/chess_club.jpg"
image garden club="images/backgrounds/garden_club.png"
image hallway= "images/backgrounds/school_hallway.png"
image library= "images/backgrounds/library.png"
image math classroom= "images/backgrounds/math_classroom.jpg"
image mcs bedroom= "images/backgrounds/mc_bedroom.png"
image mathildas house= "images/backgrounds/mysterious_mathilda_s_house.png"
image school entrance= "images/backgrounds/school_entrance_day.png"
image spade dorm hallway= "images/backgrounds/spade_dorm_hallway.png"
image spade dorms= "images/backgrounds/spade_dorms_entrance.png"
image tea club= "images/backgrounds/tea_club.jpg"

#Bringing in CGs
image transformation cg = "images/cgs/transformation_cg.png"
image hug cg = "images/cgs/hug_cg.png"
image breakfast cg = "images/cgs/breakfast_cg.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define pov = Character("[povname]", kind=adv, image="mc", namebox_background=Frame("gui/namebox_Heart.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))                     # The player character
define n = Character("", namebox_background=None)                                # The narrator
define mathilda = Character("mathilda_name", kind=adv, image="mathilda", dynamic=True, namebox_background=Frame("gui/namebox_Diamond.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))   # Mathilda

define fabien = Character("Fabien LeBlanc", kind=adv, image="fabien", namebox_background=Frame("gui/namebox_Spade.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))             # Fabien LeBlanc
define tatianna = Character("tatianna_name", kind=adv, image="tatianna", dynamic=True, namebox_background=Frame("gui/namebox_Heart.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define levy = Character("levy_name", kind=adv, image="leveret",dynamic=True, namebox_background=Frame("gui/namebox_Heart.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define mira = Character("mira_name", kind=adv, image="mira", dynamic=True, namebox_background=Frame("gui/namebox_Club.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define claudia = Character("claudia_name", kind=adv, image="claudia", dynamic=True, namebox_background=Frame("gui/namebox_Club.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define unknown = Character("???", namebox_background=Frame("gui/namebox_Diamond.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define follow1 = Character("Follower 1", namebox_background=Frame("gui/namebox_Club.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define follow2 = Character("Follower 2", namebox_background=Frame("gui/namebox_Club.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define girl1 = Character("Girl Student 1", namebox_background=Frame("gui/namebox_Club.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define girl2 = Character("Girl Student 2", namebox_background=Frame("gui/namebox_Club.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define girl3 = Character("Girl Student 3", namebox_background=Frame("gui/namebox_Club.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define girl4 = Character("Girl Student 4", namebox_background=Frame("gui/namebox_Club.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))