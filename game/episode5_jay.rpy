###############################################################################
# Episode 5 - Jay's Date
###############################################################################

# Convo with Jellie
label ep5_jay_1:
    scene black with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day

    Narrator "*over voicemail*"
    Jaylin "Hey [main], just calling to remind you of our date tomorrow. I can't wait, I'll see you then!"

    scene bg room 
    show jellie normal:
        xalign 0.25
    show davie sad:
        xalign 0.75

    show jellie normal
    Main "Hey Jellie, can I ask you a question?"
    Jellie "Yeah go ahead, what's up?"
    Main "Do you think going on a date with Jay will be weird?"

    show jellie happy
    Jellie "Hmm, depends. Do you think you could see him in a romantic way? "

    show jellie sad
    Jellie "Because if not, maybe it's better to just decline the date and keep your friendship."
    
    show jellie normal
    Jellie "But really, its all about what you are most comfortable with."
    
    show davie normal
    Main "Yeah.. thank you Jellie, that cleared up a lot. "

    menu:
        "I think I'm going to decline the date.":
            jump ep5_jay_2_1

        "I think I'm going to try going to the date.":
            hide jellie normal
            jump ep5_jay_2_2

# Declining Jay's date
label ep5_jay_2_1:

    stop music fadeout 1.0

    scene black with fade

    Narrator "Although the call goes well, there is still a taste of sadness in the air for disappointing a friend and possibly straining your relationship with them."
    Narrator "Perhaps your gloominess was too obvious because soon after Jellie pulled you into a bear hug."
    
    play music "music/Angel Share.mp3"

    scene bg room
    show jellie normal:
        xalign 0.66
    show davie sad:
        xalign 0.75
    with fade

    pause 0.5

    show jellie normal with ease:
        xalign 0.25

    Jellie "Rejecting someone is hard, I'm proud of you for not chickening out. "
    
    show jellie sad
    Jellie "I'm heading home for the break, do you think you'll be okay alone?"
    
    show jellie happy
    show davie surprised
    Jellie "Or actually- do you want to come over?"

    menu:
        "Yeah, I think I'd like that.":
            show davie happy
            Jellie "Yay! Alright, let's start packing then!"

        "Oh no, I couldn't intrude.":
            show davie surprised
            show jellie angry
            Jellie "Nonsense! You're coming with!"

            show jellie happy
            show davie happy
            Jellie "Now start packing! :)"

    stop music fadeout 1.0

    scene black with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day

    Narrator "And with that your winter break began in the comfort of Jellie's family home."
    Narrator "You guys drank hot cocoa, watched stupid romcoms, and cuddled by the fireplace."
    Narrator "The comfort you felt in her arms was everything you'd ever wanted."
    
    scene black with dissolve

    Narrator "Finally, one thing led to another and you found yourself leaning in for a kiss."

    play music "music/Heartwarming.mp3" fadein 1.0
    
    scene cg davie x jellie with Fade(1.0, 1.0, 3.0, color="#fff")  # Slow transition for dramatic effect

    Narrator "Worried that you were overstepping boundaries, you cracked your eyes open only to see Jellie also leaning in too."
    Narrator "With a smile you closed your eyes and the rest was history. "
    Narrator "Maybe college wasn't too bad after all."

    stop music fadeout 3.0
        
    scene black with Fade(3.0, 3.0, 3.0, color="#fff") # Slow transition for dramatic effect

    jump fin

# Accepting Jay's date
label ep5_jay_2_2:
    scene black with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day

    Narrator "You decide to reply to Jay through a text with an equally excited response. Which soon becomes hearted by the blushing boy."
    Narrator "It's now the day of the fated date! "
    Narrator "You've completed all the chores on your list in preparation for this. You can only hope it goes as well as you want it to. "
    Narrator "Maybe this winter you won't be as alone as before."
    
    play music "music/Winter Chimes.mp3"
    scene bg xmas 
    show davie normal:
        xalign 0.75
    with dissolve

    Main "Jay told me to meet him by the Santa so... ah, there he is!"
    
    show davie happy
    show jaylin happy with easeinleft:
        xalign 0.25
    Jaylin "Hey, I hope its not too cold for you! You wanna walk around and check out the lights for a bit?"

    show davie normal
    Main "I'm warm enough, don't worry. I'd love to see the lights with you."

    jump ep5_jay_3

# At date location
label ep5_jay_3:
    scene black with fade

    Narrator "You two took in the lights around you and began to make conversation starting from small talk to the deeper talks about things you hold dear to your heart."
    Narrator "At some point, you tripped and Jay grabbed your hand to steady you. "
    Narrator "He didn’t let go after you were alright, however, and you might have been just fine with that. "

    pause 1.0

    Jaylin "Hmm, your hands seem pretty cold, how about we head into that cafe and order some drinks?"
    menu:
        "Sounds good, my treat!":
            jump ep5_jay_4_1
            
        "Great idea! I could use some warmth.":
            jump ep5_jay_4_2

label ep5_jay_4_1:
    Jaylin "Nooooo! I asked you on the date, I get to pay!"
    Main "Only if you get there first!"
    
    pause 1.0

    Narrator "Racing to get to the cafe, Jay arrives first, holding the door open just in time for the rush of gingerbread scented air wash over the two of you."
    Narrator "The cafe is a quaint little place with soft Christmas music playlist playing in the background. You two settle at one of the tables after ordering."

    jump ep5_jay_5

label ep5_jay_4_2:
    Jaylin "Haha, let's head on in then!"

    pause 1.0

    Narrator "The rush of gingerbread scented air over the two of you washed away the cold from outside in a flash."
    Narrator "The cafe is a quaint little place with soft Christmas music playlist playing in the background. You two settle at one of the tables after ordering."

    jump ep5_jay_5

# End of date
label ep5_jay_5:

    pause 1.0

    Narrator "Unfortunately for you, Jay was able to pay for both drinks by distracting you with a dog in a Santa outfit."
    Narrator "Amused by his refusal to let you buy him anything, you spend the next minutes trying to figure out what he would want as a present."
    Narrator "With you spitting out random guesses that get worse every time and him denying every single one, you two fall into laughter."
    Narrator "After the 10 millionth guess and 10 millionth denial, his pout seems just too cute for you to handle."

    stop music fadeout 1.0
    scene black with dissolve

    Narrator "Before you know it, you find yourself leaning in and meeting his lips with yours."

    play music "music/Heartwarming.mp3" fadein 1.0
    scene cg davie x jaylin with Fade(1.0, 1.0, 3.0, color="#fff")  # Slow transition for dramatic effect

    Narrator "Let it be known that the shock of his crush kissing him jolted him so bad that Jay opened his eyes for the first time, and boy were they beautiful."
    Narrator "You'd have to kiss him more often to see those eyes again. Not that you mind."
    Narrator "Winter was not such a cold season after all."

    stop music fadeout 3.0
    scene black with Fade(3.0, 3.0, 3.0, color="#fff") # Slow transition for dramatic effect

    jump fin