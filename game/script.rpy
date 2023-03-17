# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define unknownPlayer = Character("???")
define narrator = Character("Narrator")
define unknownWoman = Character("Unknown Woman")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room
    scene room_blank

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy
    show actor_blank_na

    # These display lines of dialogue.

    unknownPlayer "Where am I? I can’t remember what I was doing…"

    narrator "Your legs wiggle to try to get up, only to splay flat onto the cushion you were laying on."

    unknownPlayer "My legs feel weird, like I can’t stand up."

    narrator "You open your eyes to try and see where you’re at."

    # This ends the game.

    return
