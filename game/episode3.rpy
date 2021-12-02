label episode3_start:
    scene room
    Narrator "It's finally club rush day! "
    Narrator "Time to check out the various different activities the university offers and maybe meet some interesting people."
    Narrator "Jellie and you have somewhat maintained a good relationship since the first time you guys talked so you two decided to check out the clubs together! Enjoy my dear!"

# Episode 3: Ari
label ari_intro_convo:
    scene room # will be club rush
    show jellie happy:
        xpos 0
    Jellie "What kind of clubs did you want to check out first?"

    menu:
        "Maybe the cooking club? for no special reason or anything":
            Jellie "alright, sounds good to me"
            jump narration1

        "Let's go to the cooking club! I know someone there":
            Jellie "alright, sounds good to me"
            jump narration1


label narration1:
    show jellie happy
    Narrator "The two of you walk towards the center of the campus where the more well-known clubs are gathering."
    Narrator "Looking around, you finally locate their booth. And surprise surprise, there’s the mysterious pan boy too!"
    Narrator "But it seems he’s glaring daggers at a boy from another booth."
    Narrator "That’s weird…"
    Narrator "Ah there we go, he’s noticed you two."
    jump interrupt_jaylin

label interrupt_jaylin:
    show jaylin happy:
        xpos 0.25
    Jaylin "Hey, I'm so glad you actually came! Who's this?"
    menu:
        "Oh, this is my friend, Jellie":
            jump jaylin_talking
        "Oh, this is just my roommate, Jellie":
            jump jaylin_talking

label jaylin_talking:
    show jaylin happy
    Jaylin "Hi, It's nice to meet you, what was your name?"
    Jaylin "Oh shoot! I never told you my name either."
    Jaylin "Well, no better time than the present."
    $ Jaylin = Character("Jay", color="#a34635")
    Jaylin "My name is Jay, I'm the president of the cooking club :D"

label introduce_aryan:
    show ari happy:
        xpos 0.5
    Ari "You mean the president of the grandpa club."
    Ari "Hey guys, why don’t you guys come over here and let the handsome?"
    $ Ari = Character("Ari", color="#a34635")
    Ari "Ari, that’s me, tell you about the fashion club instead?"
    Ari "Don’t waste your time with those snickerdoodles."
    menu:
        "Oop that was a little rude":
            jump fashion_club_transition
        "Haha, you're too much":
            jump fashion_club_transition

label fashion_club_transition:
    show jaylin happy
    Jaylin "Yeah right fashion club-- it's more like a blood donation club"
    show ari happy
    Ari "HEY just because you don’t have girls literally having nose bleeds over how hot you are doesn’t mean our club isn’t legit."
    Jaylin "Did you just call me hot?"
    Ari "NO I DIDN'T"
    Narrator "As they continue fighting/flirting? Jellie and you begin to look around at the other clubs."
    Narrator "By the time you two return, they are still at it with their faces only inches apart."
    Jellie "Damn the tension is through the roof, kiss already"
    menu:
        "The flirting is getting out of control":
            jump fighting
        "Is this how college kids flirt?":
            jump fighting

label fighting:
    show jaylin angry
    Jaylin "WE ARE NOT FLIRTING"
    show ari normal
    Ari "*clears his throat* Anyway, ignoring that creature,  the cooking club will be having a tournament amongst our senior and junior members next week, you two should swing by!"
    show ari happy
    Ari "Your's truly will be one of the competitors ;) Here’s a flyer"
    menu:
        "I'll definitely attend!":
            jump ari_respond
        "I'll see if I can go":
            jump ari_respond

label ari_respond:
    show ari normal
    Ari "In better and more interesting news, the fashion club will be hosting a thrift-inspired show and market!"
    Ari "There’ll be plenty of affordable options for college students with plenty of drip to spare."
    Ari "You two should definitely swing by ;) Here’s our Insta with all the info!"
    menu:
        "Ooh I'll make space in my schedule":
            jump end_ep3
        "Hm I'll try to come":
            jump end_ep3

label end_ep3:
    scene room
    show jellie normal
    Jellie "Well that was quite a ride"
    Main "For real"
    Narrator "What [main] did not know at this moment however was that upon closer inspection, the time of the competition was the same as that of the market. [main_sub] would soon have some big decisions to make. "
    return
