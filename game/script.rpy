# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define unknown = Character("???")
define n = Character("")
define unknownWoman = Character("Unknown Woman")
define mathilda = Character("Mathilda")


# The game starts here.

label start:

    ### -------------------- Section 1 -------------------- ###

    # Background: Black Screen
    # Display the background "Room_Blank.jpg" from the images directory
    scene Room_Blank

    # Display the character portrait expression "Actor_Blank_NA.png" from the images directory
    show Actor_Blank_NA

    # Display lines of dialogue.

    unknown "Where am I? I can’t remember what I was doing…"

    n "Your legs wiggle to try to get up, only to splay flat onto the cushion you were laying on."

    unknown "My legs feel weird, like I can’t stand up."

    n "You open your eyes to try and see where you’re at."

    # Background change: Mysterious Room
    scene Room_Mysterious

    unknown "I don’t recognize this room, but it looks nice."

    n "The room has very little light, but what you can see seems well furnished. The pillow you are laying on looks like satin."

    unknown "*Growl*"

    n "That’s definitely your stomach. You successfully get onto all four legs to try and look around for food scraps or a trash can."

    unknown "There’s gotta be a little snack hidden around here…"

    n "You find a basket with what looks like treats! Your tummy growls louder as if begging you to dig in. One bite tells you that it is wrapped in plastic, leaving the snack crushed behind its clear shell."

    unknown "Noooo!"

    n "Your whine sounds out as you drag the plastic wrapped treat out using your paws to try and free your snack."

    unknown "*Squeak*"

    n "Your ears perk as it sounds like a door squeak, followed by footsteps. Someone is coming! You thought at first to be happy someone could open up your treat, only to realize you have no idea if this person is friendly. You grab your snack and sneak under the table to check out who was about to walk into the room."

    unknownWoman "Little doggie, I’m back home!"

    n "A small light comes in as she closes the door behind her. Hopefully you didn’t need that to escape."

    unknownWoman "…"

    unknownWoman "Little doggie?"

    n "Sounds like she’s calling for you."

    # Section 1 Choice 1
    # Offer the player a choice
    menu:
        narrator "What do you do?"

        "Come out from table":

            n "You slowly peek your head out with your snack still hanging from your mouth."

        "Stay underneath":

            n "You stay under the table guarding the snack. She peeks her head underneath, instantly spotting you. Busted."

    unknownWoman "There you are. What’s that you got?"

    n "She takes the treat from you to take a better look at it. She gasps before putting it away and then grabbing the basket and putting it on the table out of reach."

    unknown "*Whine, whine*"

    unknownWoman "Sorry, puppy, you can’t have chocolate. If you’re hungry, I have something that will be much better."

    n "You don’t know what would be better, but you sit patiently as she reaches for something on a high shelf."

    unknownWoman "Here, some yummy and safe dog food."

    n "You see what looks like a couple small sausages. Your mouth waters before you give a quick sniff to check if it’s safe. You then happily tear into your meal."

    unknownWoman "Glad you like it."

    n "You finish your meal with gusto before going to sit back on your pillow. The human had just been watching this whole time. She stares at you with great interest, as if you were the only thing in the room."

    unknownWoman "All done?"

    n "You give a little nod as you lay. Now fed, you thought about why you were here. You know you didn’t have anyone you belonged to. The last thing you remember is digging through trash, actually. You also hadn’t even made a note that you understand this human and she seemed to understand you."

    unknown "Bark!"

    n "No words came out of your mouth, but you were trying to ask why you were here. Not like you had anywhere else to be, but you’d like to know who this person was and what they wanted with you."

    unknownWoman "Settle down, you can’t talk, silly. I can explain as long as you can understand me."

    n "Another nod as you prepared to hear what she had to say."

    unknownWoman "First, I found you and was letting you heal from your accident."

    n "She gestures to your hind leg. It felt funny, but hadn’t noticed anything else wrong with it. That and your head barely lets you see it. You can see something on it that looks like a sock."

    unknownWoman "I’m happy to see you recovering quickly. I think you’ve noticed you’re not an ordinary little dog, are you?"

    n "She has a point. Not most dogs understand humans. Other dogs could learn names or commands, but you knew every word. Even the ones you didn’t want to hear."

    # Section 1 Choice 2
    menu:
        unknownWoman "That’s why I think you’re perfect for my test. Since I’ve been a good host, would you humor me for one little test?"

        "Nod head":

            n "You nod your head. She seems delighted and scoops you up from the pillow in her arms."

        "Give questioning look":

            n "You give her a look to try and portray your uneasy feeling."

            unknownWoman "I promise you won’t be harmed."

            n "You look at your feet mulling it over for a moment before nodding. She scoops you up from the pillow into her arms."

    n "You have a new view of the room from a better vantage point. It looks messy with how many books, crystals, plants, and other things are strewn about. You are soon placed on a chair on the other side of the room."

    unknownWoman "Stay here for one moment. I’ll be right back."

    n "You sit and stay like a good dog. You hope she’ll give you a little pet for being good. Then again, you were unsure about this test. Most things you knew were about sitting, staying, and occasionally, playing dead. Your greedy tummy hoped she’d be back with a box of treats."

    n "It didn’t take long before she appeared back with a small delicate box. Your tail wags in excitement."

    unknownWoman "Don’t get too excited, this isn’t for treats."

    n "Your little head droops and your tail stops as your hopes are crushed. You do get a pat on the head with a scritch behind the ear. Seems like she doesn’t like seeing a pouty face."

    unknownWoman "Alright then, let’s begin shall we?"

    n "She opens the box and the necklace is inside. You give it a sniff before she lifts it to show it off. It hangs from a gold chain down to a big red gem at the end. You know humans love this stuff. Even you can appreciate that it sparkles and looks pretty."

    unknownWoman "Be careful as this necklace is no ordinary necklace. It contains the love, blood, and betrayal of the life before it."

    n "You are not really sure what that means, but the way she stares at the necklace with intensity, you know it must be important."

    unknownWoman "What I plan to do is give this to you. I want to undo what has been done and I think you’ll be able to do it."

    n "You tilt your head. She’s being really vague and also you’re a dog. A smart and adorable dog. But a dog."

    unknownWoman "I know how it sounds, but trust me. I’ve been working on this for a while. At worst, you’re not what I’m looking for and I’m happy to have a new friend. I have a feeling about this though."

    n "You figure that she knows what she’s talking about and at least you’ll give it a try."

    unknownWoman "Alright, I will put this on you. If I’m right something should happen. If not, I’ll take it off and get you a treat."

    n "Your tail wiggles as you try to stay still. You think putting on a necklace shouldn’t hurt so you’re looking forward to an easy treat."

    n "The necklace slips over your head and you feel the weight on your neck. It dangles quite low, almost touching your feet. She backs away, staring at you intently. You close your eyes thinking something should happen. The most you feel is a little itchy."


    
    ### -------------------- Section 2 -------------------- ###
    # Background change: Blank Room
    scene Room_Blank

    unknownWoman "…"

    # Background change: Mysterious Room
    scene Room_Mysterious

    narrator "You open your eyes and nothing has changed, the look on the human’s face is sad. You wish you could change it. The treat no longer sounded nice seeing how it made her so disappointed."

    narrator "That’s when the necklace starts to glow. It freaks you out a little bit. You see a smile start to creep on her face, so maybe that was supposed to happen?"

    unknownWoman "It’s working!"

    narrator "You feel horrible all over. The necklace seems to shrink…or wait, are you growing? You can’t tell as the glow is surrounding your very self. You squeeze your eyes shut trying to endure this and end up curling up. That does last long as you break the chair from your weight leaving you on the floor."

    unknownWoman "Doggie?"

    narrator "She sounds concerned, but you won’t stop holding your legs. Wait holding? You peek an eye open to see the glow is gone and so is all your fur."

    unknown "Gaaah!"

    unknownWoman "Wait, it’s okay! Calm down, I'm here."

    narrator "She grabs you, helping you sit up at least. She then wraps a blanket around your now hairless body."

    # Background change: Transformation CG
    scene CG_Transformation

    unknownWoman "It worked! I know this will be very new, but I promise it will be worth it."

    unknown "What happened? W-what am I saying? Wait, I am saying. I’m talking!"

    unknownWoman "Yes, isn’t it wonderful?"

    narrator "You take a look at your new form. You’re human. A big naked human!"

    unknown "What did you do? Why? W-what do I do?"

    unknownWoman "I know you have a lot of questions, but let’s get you dressed, first."

    narrator "You give a judgemental look before following her lead. Or trying to follow, your new legs are not as well balanced and you’re not sure what to do with your front legs."

    # Background change: Mysterious Room
    scene Room_Mysterious

    narrator "She takes you and dresses you before letting you sit on a chair. She ties up what’s left of your hair into what she called a ‘pony tail’. Speaking of, you don’t have a tail. It made sitting easier, but balancing harder."

    # Section 2 Choice 1 ### TODO ###
    menu:
        unknownWoman "Now, I’m sure you have questions. Go ahead and ask away. I’ll do my best to answer."

        "Who are you?":

        "Why did you change me?":

        "What is up with the necklace?":






    # This ends the game.

    return
