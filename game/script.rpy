
# Declare variables

default menuS2C1Selected = [False, False, False]


# The game starts here.

label start:

    # Initialize variables

    $ mathilda_name = "Unknown Woman"
    $ levy_name = "Bunny Boy"
    $ mira_name = "Cheery Girl"
    $ tatianna_name = "Tall Girl"
    $ claudia_name = "Mischievous Cat"

    python:
        povname = "???"



    ### -------------------- Section 1 -------------------- ###

    # Background: Black Screen
    # Display the background "Room_Blank.jpg" from the images directory
    scene blank
    # Display the character portrait expression "Actor_Blank_NA.png" from the images directory
    #show Actor_Blank_NA

    # Display lines of dialogue.

    pov "Where am I? I can’t remember what I was doing…"

    n "Your legs wiggle to try to get up, only to splay flat onto the cushion you were laying on."

    pov "My legs feel weird, like I can’t stand up."

    n "You open your eyes to try and see where you’re at."

    # Background change: Mysterious Room
    scene mathildas house
    with dissolve

    show mc dog at left
    with dissolve

    pov "I don’t recognize this room, but it looks nice."

    n "The room has very little light, but what you can see seems well furnished. The pillow you are laying on looks like satin."

    pov dog hungry "*Growl*"

    n "That’s definitely your stomach. You successfully get onto all four legs to try and look around for food scraps or a trash can."

    pov "There’s gotta be a little snack hidden around here…"

    n "You find a basket with what looks like treats! Your tummy growls louder as if begging you to dig in. One bite tells you that it is wrapped in plastic, leaving the snack crushed behind its clear shell."

    pov dog sad"Noooo!"

    n "Your whine sounds out as you drag the plastic wrapped treat out using your paws to try and free your snack."

    pov dog -sad "*Squeak*"

    n "Your ears perk as it sounds like a door squeak, followed by footsteps. Someone is coming! You thought at first to be happy someone could open up your treat, only to realize you have no idea if this person is friendly. You grab your snack and sneak under the table to check out who was about to walk into the room."

    hide mc dog
    with dissolve
   

    show mathilda happy at right
    with moveinright
    mathilda "Little doggie, I’m back home!"

    n "A small light comes in as she closes the door behind her. Hopefully you didn’t need that to escape."

    mathilda "…"

    mathilda -happy "Little doggie?"

    n "Sounds like she’s calling for you."

    # Section 1 Choice 1
    # Offer the player a choice
    menu:
        n "What do I do?"

        "Come out from table":

            n "You slowly peek your head out with your snack still hanging from your mouth."

        "Stay underneath":

            n "You stay under the table guarding the snack. She peeks her head underneath, instantly spotting you. Busted."

    show mc dog
    mathilda happy "There you are. What’s that you got?"
    show mathilda stern

    n "She takes the treat from you to take a better look at it. She gasps before putting it away and then grabbing the basket and putting it on the table out of reach."

    pov dog sad "*Whine, whine*"

    mathilda -stern "Sorry, puppy, you can’t have chocolate. If you’re hungry, I have something that will be much better."

    show mc dog

    n "You don’t know what would be better, but you sit patiently as she reaches for something on a high shelf."

    mathilda happy "Here, some yummy and safe dog food."

    show mc dog happy
    n "You see what looks like a couple small sausages. Your mouth waters before you give a quick sniff to check if it’s safe. You then happily tear into your meal."

    mathilda -happy "Glad you like it."

    n "You finish your meal with gusto before going to sit back on your pillow. The human had just been watching this whole time. She stares at you with great interest, as if you were the only thing in the room."

    show mc dog
    
    mathilda "All done?"

    n "You give a little nod as you lay. Now fed, you thought about why you were here. You know you didn’t have anyone you belonged to. The last thing you remember is digging through trash, actually. You also hadn’t even made a note that you understand this human and she seemed to understand you."

    pov "Bark!"

    n "No words came out of your mouth, but you were trying to ask why you were here. Not like you had anywhere else to be, but you’d like to know who this person was and what they wanted with you."

    mathilda "Settle down, you can’t talk, silly. I can explain as long as you can understand me."

    n "Another nod as you prepared to hear what she had to say."

    mathilda "First, I found you and was letting you heal from your accident."

    n "She gestures to your hind leg. It felt funny, but hadn’t noticed anything else wrong with it. That and your head barely lets you see it. You can see something on it that looks like a sock."

    mathilda "I’m happy to see you recovering quickly. I think you’ve noticed you’re not an ordinary little dog, are you?"

    n "She has a point. Not most dogs understand humans. Other dogs could learn names or commands, but you knew every word. Even the ones you didn’t want to hear."

    # Section 1 Choice 2
    menu:
        mathilda "That’s why I think you’re perfect for my test. Since I’ve been a good host, would you humor me for one little test?"

        "Nod head":

            n "You nod your head. She seems delighted and scoops you up from the pillow in her arms."

        "Give questioning look":
            show mc dog confused
            n "You give her a look to try and portray your uneasy feeling."

            mathilda "I promise you won’t be harmed."
            show mc dog
            n "You look at your feet mulling it over for a moment before nodding. She scoops you up from the pillow into her arms."

    n "You have a new view of the room from a better vantage point. It looks messy with how many books, crystals, plants, and other things are strewn about. You are soon placed on a chair on the other side of the room."

    mathilda "Stay here for one moment. I’ll be right back."
    show mc dog hungry
    n "You sit and stay like a good dog. You hope she’ll give you a little pet for being good. Then again, you were unsure about this test. Most things you knew were about sitting, staying, and occasionally, playing dead. Your greedy tummy hoped she’d be back with a box of treats."

    n "It didn’t take long before she appeared back with a small delicate box. Your tail wags in excitement."

    mathilda "Don’t get too excited, this isn’t for treats."
    show mc dog sad
    n "Your little head droops and your tail stops as your hopes are crushed. You do get a pat on the head with a scritch behind the ear. Seems like she doesn’t like seeing a pouty face."
    show mc dog
    mathilda "Alright then, let’s begin shall we?"

    n "She opens the box and the necklace is inside. You give it a sniff before she lifts it to show it off. It hangs from a gold chain down to a big red gem at the end. You know humans love this stuff. Even you can appreciate that it sparkles and looks pretty."

    mathilda stern "Be careful as this necklace is no ordinary necklace. It contains the love, blood, and betrayal of the life before it."

    n "You are not really sure what that means, but the way she stares at the necklace with intensity, you know it must be important."

    mathilda -stern "What I plan to do is give this to you. I want to undo what has been done and I think you’ll be able to do it."

    show mc dog confused
    n "You tilt your head. She’s being really vague and also you’re a dog. A smart and adorable dog. But a dog."

    mathilda "I know how it sounds, but trust me. I’ve been working on this for a while. At worst, you’re not what I’m looking for and I’m happy to have a new friend. I have a feeling about this though."

    show mc dog
    n "You figure that she knows what she’s talking about and at least you’ll give it a try."

    mathilda "Alright, I will put this on you. If I’m right something should happen. If not, I’ll take it off and get you a treat."

    n "Your tail wiggles as you try to stay still. You think putting on a necklace shouldn’t hurt so you’re looking forward to an easy treat."

    n "The necklace slips over your head and you feel the weight on your neck. It dangles quite low, almost touching your feet. She backs away, staring at you intently. You close your eyes thinking something should happen. The most you feel is a little itchy."

    scene blank
    with fade

    
    ### -------------------- Section 2 -------------------- ###
    # Background change: Blank Room

    mathilda "…"

    # Background change: Mysterious Room
    scene mathildas house
    with dissolve

    show mc dog
    with dissolve

    show mathilda at right
    with dissolve

    show mc dog sad
    n "You open your eyes and nothing has changed, the look on the human’s face is sad. You wish you could change it. The treat no longer sounded nice seeing how it made her so disappointed."

    n "That’s when the necklace starts to glow. It freaks you out a little bit. You see a smile start to creep on her face, so maybe that was supposed to happen?"
    show mc dog confused
    mathilda happy "It’s working!"

    scene blank
    with fade
    n "You feel horrible all over. The necklace seems to shrink…or wait, are you growing? You can’t tell as the glow is surrounding your very self. You squeeze your eyes shut trying to endure this and end up curling up. That does last long as you break the chair from your weight leaving you on the floor."

    mathilda "Doggie?"

    n "She sounds concerned, but you won’t stop holding your legs. Wait holding? You peek an eye open to see the glow is gone and so is all your fur."

    scene mathildas house
    with fade

    show mathilda at right
    with dissolve

    show mc at left
    with dissolve

    pov surprised "Gaaah!"

    mathilda "Wait, it’s okay! Calm down, I'm here."

    n "She grabs you, helping you sit up at least. She then wraps a blanket around your now hairless body."

    # Background change: Transformation CG
    scene transformation cg
    with fade

    mathilda "It worked! I know this will be very new, but I promise it will be worth it."

    pov "What happened? W-what am I saying? Wait, I am saying. I’m talking!"

    mathilda "Yes, isn’t it wonderful?"

    n "You take a look at your new form. You’re human. A big naked human!"

    pov "What did you do? Why? W-what do I do?"

    mathilda "I know you have a lot of questions, but let’s get you dressed, first."

    n "You give a judgemental look before following her lead. Or trying to follow, your new legs are not as well balanced and you’re not sure what to do with your front legs."

    # Background change: Mysterious Room
    scene mathildas house
    with dissolve

    show mathilda happy at right
    with dissolve

    show mc at left
    with dissolve
    n "She takes you and dresses you before letting you sit on a chair. She ties up what’s left of your hair into what she called a ‘pony tail’. Speaking of, you don’t have a tail. It made sitting easier, but balancing harder."

    # Section 2 Choice 1
    menu menuS2C1Head:
        mathilda "Now, I’m sure you have questions. Go ahead and ask away. I’ll do my best to answer."

        # Option 0
        "Who are you?" if not menuS2C1Selected[0]:

            $ menuS2C1Selected[0] = True
            pov confused "Who are you?"

            $ mathilda_name = "Mathilda"
            mathilda "Mathilda, I work with magic and potions."

            jump menuS2C1Head

        # Option 1
        "Why did you change me?" if not menuS2C1Selected[1]:

            $ menuS2C1Selected[1] = True
            pov confused "Why did you change me?"

            mathilda "The necklace needed a vessel. It contains a power that could save this world."

            jump menuS2C1Head

        # Option 2
        "What is up with the necklace?" if not menuS2C1Selected[2]:

            $ menuS2C1Selected[2] = True
            pov confused "What is up with the necklace?"
            
            mathilda "The necklace is embedded with power that I cannot possess. It chooses a wearer and they alone can wield the power to save us."

            jump menuS2C1Head

    show mc neutral
    n "Even with my first questions answered, I only have more questions."

    mathilda -happy "If I may ask a question now, who are you?"

    pov sad "Who am I?"

    mathilda "Or at least, what should I call you?"

    pov -sad "Hm…"

    # Prompt the player to type in their name, default is Inui, max length is 32 characters
    python:
        povname = renpy.input("Enter player name", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Inui"

    pov "[povname]."

    mathilda happy "Cute name. I think it suits you."

    n "I’m not sure, now that I think about it. The name felt familiar so I figured it was good enough."

    mathilda -happy "I’m sure this is a lot for one evening. Not to mention you will need to get used to this new body."

    n "I wanted to know more, but I’ll save it for later. In the meantime, I was moved to a bed to rest. My body still tingles all over."

    mathilda "This bell here is if you need me. Ring it if you need help walking, food, anything."

    n "I nodded before going to sleep."

    # Background change: Blank Room
    scene blank

    n "My dreams felt familiar, but I couldn’t recognize anyone. It felt like a memory, but this memory was me as a human. As far as I remember, I had been a dog until this point. I was in a beautiful garden with someone else. It felt nostalgic."

    # Background change: Mysterious Room
    scene mathildas house
    with dissolve

    show mc at left
    with dissolve
    n "The dream ended before the memory got any further. I woke up, instinctively shooting up to try to find the bell. These new paws felt weird. I was able to move them all differently and grab things. I practiced grabbing the blanket then reaching for the bell."

    mathilda "Coming!"

    show mathilda at right
    with easeinright

    n "Soon enough, Mathilda was coming in with a bowl and tray. She set them down before taking the tightly gripped bell in my hand."

    mathilda "Still getting used to everything?"

    n "I nodded."

    mathilda happy "Don’t worry, I will help you learn everything you need."

    n "I was listening, but the smell of the bowl distracted me. Soon enough I grabbed the spoon and took a bite. A little sloppy, but delicious."

    # Background change: Breakfast with Mathilda CG
    scene breakfast cg
    with dissolve

    mathilda "Looks like you’re a quick learner. I was afraid I might have to feed you myself for a while."

    n "I blinked before noticing what I had done. Maybe being a human is easier than being a dog."


    # Time skip fade
    # Background change: Mysterious Room
    scene mathildas house
    with dissolve

    show mc at left
    with dissolve

    show mathilda at right
    with dissolve

    n "Soon enough, I was walking, talking, and acting like a human. Mathilda was patient, but it only took a couple weeks. I figured now I was human, I should ask what she wanted me to do. We were having breakfast and figured it was better now than to keep waiting."

    pov "Hey, can I ask a question?"

    mathilda "Sure, what is it?"

    pov "Now that I’m human, what is it I’m supposed to do?"

    n "She was in the middle of sipping tea before pausing at the question. She set her cup down gently before a sigh."

    mathilda sad resigned "I almost forgot. That’s right. You were such nice company, I forgot that you can’t stay here…"

    pov confused "Why? Where am I going?"

    mathilda stern "It’s time you let you know everything. Settle in, this might take a while."

    n "I felt nervous, but tried to get comfortable."

    mathilda "This world is in trouble. In fact, the reason you were injured is related to this. You were attacked as a small dog and I helped you, of course. But, you were attacked by shadows. They tend only to manifest near and attack humans. Which is why you stood out to me. This necklace can help fight them."

    pov surprised "You want me to fight shadows?"

    mathilda "It’s not that simple. Shadows are caused by the curse over the town. Break the curse, and they will disappear along with freeing everyone."

    pov confused "Curse?"

    mathilda sad pensive "I know very little about the actual curse, but I know it was cast when she disappeared. That necklace brings her spirit back, allowing you the power to fight shadows and break this curse."

    pov -confused "How do I break the curse?"

    mathilda stern "...I don’t know"

    pov angry "What?!"

    mathilda sad pensive "I barely found someone to embody the vessel of Alice, I hadn’t gotten this far before."

    pov confused "Vessel of Alice?"

    mathilda stern "Yes, that’s what I had you transform into. Though, you are now just a normal girl. I believe to turn into its true form, you’d need to call on it."

    pov sad "This is so confusing and complicated."

    mathilda "Believe me, this wasn’t easy to try and learn. Not to mention you’ll soon be moved to the academy."

    pov confused "Academy? You never mentioned that before."

    mathilda "I had to help you just walk first. Yes, you will be attending the academy in order to figure out how to break the curse. If anywhere has the info you need, it would be there. It has the royal library, but you have to be a student or staff member to access it."

    pov "I see."

    mathilda -stern "Thankfully, an important person owes me a favor, thus allowing your enrollment. I sent the letter last week, you’ll be moved there shortly after we receive the acceptance letter."

    pov sad "..."

    # Section 2 Choice 2
    menu:
        mathilda "Something wrong?"

        "Say you’re happy to go to school":

            pov happy"I can’t wait to see the school."

            mathilda "I think you’ll like it. It would be good for you to have friends your age."

            pov "I’ve never been to school, is there anything I would need?"

            mathilda "Nothing the school won’t provide."

            n "She seems to pause, the look on her face a little hard to read."

            mathilda sad pensive "I’ll miss you, [povname]."

            pov sad "I’ll miss you too."

            # Background change: hug with Mathilda CG
            scene hug cg

        "Say you’ll miss her":

            pov "I’ll miss you"

            # Background change: hug with Mathilda CG
            scene hug cg

            mathilda "Oh, I’ll miss you too"

            n "She went over to give me a hug. I knew even if I wasn’t sure about what she wanted, I wanted to do it for her."

    scene blank
    n "We talked some more, the tension in the air now gone. I was just trying to enjoy what time I had left with her before I would have to leave."



    ### -------------------- Section 3 -------------------- ###
    # Time skip fade
    # Background change: School Enterance
    scene school entrance
    with dissolve
        
    n "Soon enough, the letter had arrived and I was walking with a small bag of belongings to my new home."

    show mathilda at right
    with dissolve

    show mc school neutral at left
    with dissolve

    mathilda "Write to me if you can, I want to know if you’re doing okay."

    pov "I will."

    mathilda stern "And keep your necklace on at all times. If it comes off you could transform back. Keep it under her shirt just in case to keep it from being grabbed."

    n "I quickly tucked it under my shirt before giving a thumbs up."
    show mathilda happy at right
    show mc school happy at left

    n "We said our goodbyes at the gates before I was escorted to my dorm."

    # Background change: Spade Dorm Entrance
    scene spade dorms
    with dissolve

    show fabien neutral
    with dissolve

    n "A man was there who walked in front to guide me. He seemed friendly, but I was sort of distracted by his appearance."

    show fabien neutral at right
    with dissolve

    show mc school neutral at left
    with dissolve

    fabien "Nice to meet you, I’m Fabien LeBlanc. You may call me Mr. LeBlanc."
    
    show mc school confused at left

    n "I was staring at his ears. Are those rabbit ears? Isn’t this a human school? He looked like a teacher, so I kept the thought to myself."

    pov school neutral "Nice to meet you. My name is [povname]."

    n "He nodded before heading inside. I followed behind with my small bag."

    # Background change: Spade Dorm Hallway
    scene spade dorm hallway

    show fabien neutral at right
    with dissolve

    show mc school neutral at left
    with dissolve


    fabien "This is your room. This is a Co-Ed dorm, so visiting other dorms is only allowed between Noon and Six. Obviously, curfew at eight. This is your schedule and a map to help you find your way around. The key to your dorm should be inside. Dinner tonight will be at six, don’t be late."

    n "He then turned and left as I took a look at the map. This place was huge, with many hallways and multiple buildings. I just hoped I wouldn’t get lost."

    # Background change: MC Dorm Room
    scene mcs bedroom

    n "I unpacked what little Mathilda was able to give me. I laid on the bed and it was soft enough. I figured I could either wait in my room until dinner or go explore."

    # Section 3 Choice 1
    menu:
        n "What do I do?"

        "Go Explore":
            jump s3c1o0

        "Wait until Dinner":
            jump s3c1o1

label s3c1Tail:
    
    # Background change: Cafeteria
    scene cafeteria
    show mc school neutral
    with dissolve

    n "I was able to navigate on my own to find the cafeteria. It was pretty and, like the rest of the school, huge. I walked up, receiving a hot plate of food. It looked delicious with a big steak, potatoes, and gravy. I had to keep myself from shoving my face to get a bite."
    show mc school happy
    n "I resisted the urge and decided to go take a seat so I didn’t have to wait any longer to eat. I looked around for what looked like a suitable spot. There were two places. One that was near a group of girls and one by itself near a window."

    # Section 3 Choice 2
    menu:
        n "Where do I sit?"

        "Choose seat near group":
            jump s3c2o0
        
        "Choose seat all by itself":
            jump s3c2o1

label s3c2Tail:
        
    # Background change: MC Dorm Room
    scene mcs bedroom
    with dissolve

    show mc school neutral
    with dissolve

    n "Today was a lot and there was more to expect. I just hoped I would have time between classes to try and figure out the whole saving the world thing. I got into my pajamas and tucked myself in. I figured a good night's sleep would help me think of something tomorrow. After all, there’s nothing I could do now. I turned off the light and drifted off to sleep."

    # Background change: Blank Room
    scene blank
    with dissolve
    unknown "I am here to guide you."

    pov "?"

    unknown "Don’t be afraid, [povname]"

    unknown "I know you will do great things. Follow the heart and you will find the way to set everyone free."

    n "I felt like I couldn’t move or speak. It was like being held in a warm dark blanket. Whoever was speaking felt safe even if unfamiliar."

    # Background change: MC Dorm Room
    scene mcs bedroom

    show mc school neutral
    with dissolve

    n "Soon enough I was awake again, awoken by a ringing and shaking of a small clock. I turned it off before getting up. This is where it begins. My new life as [povname] and as Alice."

    # This ends the game.

    return




# Section 3 Choice 1 Option 0
label s3c1o0:

    n "I decided waiting around wasn’t going to help me save the world. I took another look at the map and decided to go see the library. Matilda had said that’s where I would look for information on how to break the curse."

    # Background change: Spade Dorm Hallway
    scene spade dorm hallway

    show mc school confused
    with dissolve

    n "The hallway had been empty just like before making it easy to leave. A place like this I thought would have more security."

    # Background change: School Hallway
    scene hallway

    show mc school neutral

    n "I thankfully was able to find the main building, but was starting to finally notice some people hanging about. Looks like most students were walking about or in class. I was curious what class would be like."

    n "I was almost to the library before someone in one of the many groups of students stopped me."

    show mc school neutral at left
    with dissolve

    show tatianna neutral stern at right
    with dissolve
    tatianna "Where do you think you’re going?"

    pov school confused "I’m going to the library."

    n "I tried walking past, but she held out a long staff-like object to block me."

    tatianna angry "Who do you think you are to just walk past me?! I didn’t give you permission to leave."

    n "Did I break some sort of school rule?"

    pov school angry "I need permission to go to the library?"

    tatianna neutral stern "If you think being a smart ass is going to work, you are very wrong. State your business and don’t try to leave until I tell you."

    pov school surprised "What’s a smart ass?"

    n "She looked more and more angry. This girl seemed like a firework, constantly wanting to go off."

    tatianna angry "One of you, tell me who this is, so I can assign them detention."

    follow1 "I don’t know, I’ve never seen them before."

    follow2 "Me neither."

    tatianna "Then who are you?"

    pov school neutral "I’m [povname], I’m a new student and I would like to go to the library."

    n "Her eyes narrowed. She looked me up and down before rubbing her eyes in irritation."

    $ tatianna_name = "Tatianna Rosehart"
    tatianna neutral stern "I’ll let you slide this time, but from now on when you’re talking to me, don’t leave until I give you permission. Not to mention you should know that I am Tatianna Rosehart, daughter of the king and soon to be Queen. You are expected to respect me from now on, got it?"

    show mc school confused at left
    n "I really didn’t get what she said. I nodded anyway trying to just get to the library. She let me pass shortly afterwards. As I walked by people were peeking out at me from their social groups, but never said anything to me. It reminded me of groups of street dog gangs I’d avoid. This place is really weird."

    # Background change: Library
    scene library
    with dissolve

    show mc school happy at left
    with dissolve

    pov "Finally!"

    n "I made it! Now, what do I do…"
    show mc school surprised at left
    with dissolve

    n "I looked around and peeked at some book titles, but felt already very lost. I did, thankfully, know how to read. The problem is which book would I need to read?"
    show leveret neutral at right
    with dissolve

    levy "Excuse me?"

    show mc school neutral at left
    n "Please don’t yell at me."

    levy "Er, you look a little lost. Can I help?"

    n "Oh thank god."

    pov "Yes, I’m looking for a book."

    levy "What’s the title?"

    pov "I don’t know."

    levy "Er, what is it about then?"

    pov "Got anything that is about breaking curses-?"

    n "Suddenly I was being shushed."

    levy surprised "What are you doing?!"

    show mc school confused at left
    n "I gave him a confused look."

    levy "Why do you need to know about curses?"

    pov school neutral "Uh, I wanted to know more about the curse on this town. That is if you have anything."

    levy neutral "Oh. Be careful when discussing that, okay? I think I know something."
    hide leveret
    with dissolve

    n "He went back into the shelves, finding a big red book before handing it over."

    show leveret neutral at right
    with dissolve
    levy "Here. It’s the town’s history. If there’s anything it would be here."

    pov school happy "Thanks!"

    levy "Any reason why you wanna know about it?"

    pov "Well, I’d like to know how to fix it."

    levy "Haha, if only."

    show mc school confused at left
    n "I just stare at him. Was there a joke?"

    levy sad "You’re serious? I mean good luck, but it’s a little insane to think you can fix this curse. I mean if the King can’t…"

    n "His voice trailed off before he cleared his throat."

    levy happy "Well, enjoy your book"

    pov school neutral "Thank you, uh…"

    $ levy_name = "Leveret LeBlanc"
    levy "Leveret, Leveret LeBlanc. Some people just call me Levy, if that’s easier."

    pov school happy "Thank you, Leveret."

    hide leveret
    with dissolve

    n "He went off somewhere to do whatever he was probably doing before he decided to help me. I decided to open the book and start reading. There were things about Royal families, wars, tea parties, and other things before I got bored. I would have to try and read more later as the giant clock in the courtyard could be heard in the distance. Time for dinner."

    jump s3c1Tail

# Section 3 Choice 1 Option 1
label s3c1o1:
    show mc school neutral
    with dissolve

    n "I decided getting some rest would be fine. Not like I’d miss anything before dinner."

    n "I tried to snooze but, a little later a knock came to my door. I decided to go answer it."

    n "At the door was a short and smiling girl with a gift in her hand. She shoved them into my hands before walking inside."
    show mc school neutral at left
    with dissolve

    show mira happy at right
    with dissolve

    mira "Hello, welcome! You’re the new student, right?"

    pov "Yes, I am. I’m [povname]"

    $ mira_name = "Mira Shelbrooke"
    mira "I’m Mira, Mira Shelbrooke! I’m part of the student council and came to welcome you. The gift is some notebooks and stationary to help you start."

    pov "Thank you, I will probably need those."

    mira happy "Your room looks so nice!"

    pov "Thank you?"

    mira "If you want some stuffed animals to brighten this place up, you can borrow some! Just make sure they’re tucked in for bed, of course."

    pov school confused "Uh, I’ll think about it."

    mira "Well, I’m here if you need any help getting around or anything. I’ll be at the end of the hall in that room on the right. I’ll be off now, have fun moving in!"
    hide mira

    n "She left as quickly as she had come. I took the box and placed it on my bed before opening it. Just pens, pencils, paper, and notebooks. I then set that aside to go and try and nap again. Waking up to the clock striking, soon enough it was dinner time."

    jump s3c1Tail

# Section 3 Choice 2 Option 0
label s3c2o0:
    show mc school neutral at left
    with dissolve

    n "I decided to try and go sit with some of my peers. There was a group of girls all chatting excitedly. I took a seat at the edge of their group and started to eat."

    girl1 "…"

    n "They all looked at me, making me stop eating. I forgot I should introduce myself."

    pov "Hi, I’m [povname]."

    girl1 "Hello"

    n "They seem to be waiting for me to say something else…"

    pov "What are you all talking about?"

    n "They all looked at each other and giggled."

    girl2 "Just the cutest guy in school."

    n "Cutest guy?"

    pov school confused "Who?"

    girl3 "What do you mean who? Dimitri, of course!"

    girl2 "We all like him. I mean, who doesn’t?"

    show mc school angry at left
    n "Maybe I should just start introducing myself as a new student, because I have no idea who they’re talking about."

    pov school neutral "I’ve never seen them, but if you say so."

    girl1 "He’s right there, look."

    n "She pointed on the other side of the room at a tall man in a hat. His hat was very small compared to his head, but it looked nice that way."

    pov school confused "He looks okay."

    girl2 "Just okay?"

    girl3 "Maybe they just have bad taste in men."

    girl4 "Or they like women."

    show mc school surprised at left
    n "What?"

    girl2 "Well if you like girls that’s fine."

    pov "I didn’t say anything about liking anyone-"

    girl3 "Well, if you do, just know we’re like, totally okay with that."

    girl4 "Yeah, we don’t judge."

    pov school confused "Okay, thank you?"
    show mc school neutral at left
    n "They seemed pretty peachy and more friendly. I decided to just listen as they mentioned all the different things they like about Dimitri. Everyone talked about times they almost got to touch his hand or speak, but seemed like no one ever talked to him. It made me think if everyone avoided him this way, it would be lonely."

    jump s3c2Tail

# Section 3 Choice 2 Option 1
label s3c2o1:
    show mc school neutral at left
    with dissolve
    n "I decided to eat alone. I didn’t know anyone yet, so I figured being by myself would be okay. I happily chewed into some potatoes before I noticed someone had snuck up on me. I felt something fluffy touch my back and I flinched turning to see a person standing behind me."

    pov school confused "What are you doing?"
    show mc school angry at left
    with dissolve
    n "My eyes narrowed. They had pointed ears to go with that long tail. Reminded me of a cat. Were those cat ears? Could humans have different ears?"

    show claudia neutral at right
    with dissolve

    claudia "Sorry about that, kitty. I just wanted to introduce myself, but it looks like my tail beat me to it."

    pov school neutral "Who are you?"

    $ claudia_name = "Claudia Catebury"
    claudia happy "They call me many things, but most would say I go by Claudia or Claude. I’m a Catebury, but I don’t care much for the title."

    pov "I’m [povname]. I’m a new student here."

    claudia "I figured as much, which is why I thought I’d come say hello~"

    show mc school confused at left
    n "They seemed friendly, but I felt something odd about them. Not to mention I was distracted by the way their tail flicked back and forth. I missed my tail."

    claudia neutral "No offense, but do you have a dog or something? Your smell reminds me of a dog pound."

    n "I can feel my dog instincts tell me to bite and bark at them, but I’m supposed to be human."

    pov school sad "Uh, I had a dog. Now that I moved here, I don’t get to be with them anymore."

    show claudia surprised at right
    n "I tried to sell my sadness to try and make them not suspect I’m actually a dog. Maybe I should try to use that perfume Mathilda packed more often."

    n "I must have done a good job as their face softened."

    claudia "I’m sorry, I guess I hadn’t considered that. Let me make it up to you."

    n "I cocked my head confused."

    pov school surprised "How?"

    claudia "This!"

    n "They handed me a small charm. It was shaped like a cat."

    claudia "I don’t have anything for dogs, but it’s still a pet right? And it’s a token of my friendship and a good luck charm, if that helps."

    pov school happy "Thank you. It is really cute."

    n "I had no idea what to do with it, but it was nice to have friends. I also might need that good luck."

    claudia "Honestly, I remember being new and figured you could use a leg up. I’m your upperclassman so you should look to me for help. If someone is picking on you, don’t be afraid to call on me, okay?"

    pov school neutral "I will, thank you."

    n "I felt awkward not being able to give anything back. I tried to see what I had on me, but I only had pocket lint."

    claudia happy "I gotta go, but don’t forget. See you around, kitty."
    hide claudia
    with dissolve

    n "They left probably back to their dorm. I decided to put the cham in my pocket and finish eating."

    jump s3c2Tail