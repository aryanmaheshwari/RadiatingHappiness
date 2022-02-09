################################################################################ 
# Episode 3: Meeting Ari at Club Rush
###############################################################################

# Start the day
label ep_3_1:
    scene black with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day
    Narrator "It's finally club rush day! "
    Narrator "Time to check out the various different activities the university offers and maybe meet some interesting people."
    Narrator "Jellie and you have somewhat maintained a good relationship since the first time you guys talked so you two decided to check out the clubs together!"

    # Talk with Jellie about where to go
    scene bg club rush with dissolve
    
    play music "music/Montauk Point.mp3"

    show jellie normal with easeinright:
        xalign 0.25
    show davie normal with easeinright:
        xalign 0.75
    
    Jellie "What kind of clubs did you want to check out first?"

    menu:
        "Maybe the cooking club? For no special reason or anything.":
            show jellie happy
            Jellie "Alright, sounds good to me."
            pass

        "Let's go to the cooking club! I know someone there.":
            show jellie happy
            Jellie "Alright, sounds good to me."
            pass

# Go to the club rush
label ep_3_2:
    hide davie with easeoutright
    hide jellie with easeoutright

    scene black with dissolve
    Narrator "The two of you walk towards the center of the campus where the more well-known clubs are gathering."
    Narrator "Looking around, you finally locate their booth."
    
    scene bg club rush with dissolve
    show davie normal with easeinleft:
        xalign 0.75 
    show jellie normal with easeinleft:
        xalign 0.25

    Narrator "And surprise surprise, there’s the mysterious pan boy too!"
    Narrator "But it seems he’s glaring daggers at a boy from another booth."
    Narrator "That’s weird..."
    Narrator "Ah there we go, he’s noticed you two."

# Jeylin interrupts
label ep_3_3:
    show jaylin happy with easeinright:
        xalign 0.9

    show jellie normal:
        xalign 0.1
    show davie normal:
        xalign 0.5
    with ease

    Jaylin "Hey, I'm so glad you actually came! Who's this?"
    Main "Oh..."

    menu:
        "This is my friend, Jellie.":
            show jellie happy
            pass
        "This is just my roommate, Jellie.":
            show jellie normal
            pass

    show jaylin happy
    Jaylin "Hi, It's nice to meet you, what was your name?"

    show jaylin surprised
    Jaylin "Oh shoot! I never told you my name either."

    show jaylin normal
    Jaylin "Well, no better time than the present."
    $ Jaylin = Character("Jay", color="#bfbf90")
    
    show jaylin happy
    Jaylin "My name is Jay, I'm the president of the cooking club! :D"

# Introduce Ari
label ep_3_4:
    show ari normal with easeinright:
        xalign 1.0

    show jaylin surprised:
        xalign 0.67
    show davie surprised:
        xalign 0.33
    show jellie surprised:
        xalign 0
    with ease

    Ari "You mean the president of the grandpa club."

    show ari happy
    show jaylin angry
    Ari "Hey guys, why don’t you guys come over here?"

    show davie sad
    show jellie sad

    $ Ari = Character("Ari", color="#a34635")
    Ari "Let the handsome Ari, that’s me, tell you about the fashion club instead?"
    Ari "Don’t waste your time with those snickerdoodles."

    menu:
        "Oop that was a little rude.":
            pass
        "Haha, you're too much.":
            pass

    show ari surprised
    show jaylin happy
    show davie surprised
    show jellie surprised

    Jaylin "Yeah right fashion club-- it's more like a blood donation club."

    show jaylin surprised
    show ari happy
    Ari "HEY! Just because you don’t have girls literally having nose bleeds over how hot you are doesn’t mean our club isn’t legit." with vpunch

    show ari surprised
    show jaylin happy
    Jaylin "Did you just call me hot?"

    show jaylin normal
    show davie happy
    show jellie happy
    show ari angry
    Ari "NO I DIDN'T!" with vpunch

    scene black with dissolve

# Jaylin talks about the cooking club after the "fight"
label ep3_5:
    Narrator "As they continue fighting... flirting?..."
    Narrator "...you and Jellie begin to look around at the other clubs."
    Narrator "By the time you two return, they are still at it with their faces only inches apart."

    scene bg club rush
    show jaylin angry:
        xalign 0.67
    show ari angry:
        xalign 1.0
    with dissolve

    show davie normal with easeinleft:
        xalign 0.33
    show jellie normal with easeinleft:
        xalign 0.0

    Jellie "Damn, the tension is through the roof. Kiss already!"
    menu:
        "The flirting is getting out of control.":
            pass
        "Is this how college kids flirt?":
            pass

    show jaylin angry
    AriJay "WE ARE NOT FLIRTING!" with vpunch

    show jaylin sad
    Jaylin "*clears throat*{nw}"

    show jaylin normal
    show ari surprised
    Jaylin "Anyway, ignoring that creature..."

    show jaylin happy
    show ari angry
    Jaylin "The cooking club will be having a tournament amongst our senior and junior members next week, you two should swing by!"

    show jaylin normal
    Jaylin "Yours truly will be one of the competitors! ;) Here’s a flyer."

    menu:
        "I'll definitely attend!":
            show davie happy
            show jaylin happy
            pass
        "I'll see if I can go.":
            show jaylin normal
            pass

# Ari talks about the fashion club
label ep3_6:
    show jaylin normal
    show ari happy
    Ari "In better and more interesting news, the fashion club will be hosting a thrift-inspired show and market!"
    Ari "There’ll be plenty of affordable options for college students with plenty of drip to spare."

    show ari normal
    Ari "You two should definitely swing by ;)"
    Ari "Here’s our Insta with all the info!"

    menu:
        "Ooh I'll make space in my schedule.":
            show ari happy
            pass
        "Hm I'll try to come.":
            show ari normal
            pass

# Back at the dorms
label ep3_7:
    scene bg room with fade

    show jellie normal with easeinright:
        xalign 0.25
    show davie normal with easeinright:
        xalign 0.75

    Jellie "Well, that was quite a ride."
    Main "For real."

    scene black with dissolve

    Narrator "What [main] did not know at this moment however was that upon closer inspection, the time of the competition was the same as that of the market."
    Narrator "[main_sub] would soon have some big decisions to make."
    
    stop music fadeout 1.0

    jump ep4a_1