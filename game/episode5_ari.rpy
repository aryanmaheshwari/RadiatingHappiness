###############################################################################
# Episode 5 - Ari's date
###############################################################################

# Convo with Jellie
label ep5_ari_1:
    scene black with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day
    
    Narrator "*over voicemail*"
    Ari "Hey [main], just calling to remind you of our date tomorrow. I can't wait, I'll see you then!"
    
    scene bg room 
    show jellie normal:
        xalign 0.25
    show davie sad:
        xalign 0.75
    
    Main "Hey Jellie, can I ask you a question?"
    Jellie "Yeah go ahead, what's up?"
    Main "Do you think going on a date with Ari will be weird?"

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
            jump ep5_ari_2_1

        "I think I'm going to try going to the date.":
            jump ep5_ari_2_2

# Declining Ari's date
label ep5_ari_2_1:
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
    scene cg davie x jellie with Fade(1.0, 1.0, 3.0, color="#fff") # Slow transition for dramatic effect

    Narrator "Worried that you were overstepping boundaries you cracked your eyes open only to see Jellie also leaning in too."
    Narrator "With a smile, you closed your eyes and the rest was history. "
    Narrator "Maybe college wasn't too bad after all."

    stop music fadeout 3.0
    scene black with Fade(3.0, 3.0, 3.0, color="#fff") # Slow transition for dramatic effect

    jump fin

# Accepting Ari's date
label ep5_ari_2_2:
    scene black with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day

    Narrator "You decide to reply to Ari through a text with an equally excited response..."
    Narrator "...which soon becomes hearted by the blushing boy."
    Narrator "It's now the day of the fated date! "
    Narrator "You've completed all the chores on your list in preparation for this. You can only hope it goes as well as you want it to. "
    Narrator "Maybe this winter you won't be as alone as before."

    play music "music/Winter Chimes.mp3"
    scene bg xmas 
    show davie normal:
        xalign 0.75
    with dissolve

    Main "Ari told me to meet him by the blue tree so... ah, there he is!"

    show davie happy
    show ari happy with easeinleft:
        xalign 0.25
    Ari "Hey cutie! You wanna walk around and check out the lights for a bit?"

    show davie normal
    Main "Yep, that sounds good to me."

    jump ep5_ari_3

# At date location
label ep5_ari_3:
    scene black with fade

    Narrator "You two took in the lights around you and began to make conversation starting from small talk to the deeper talks about things you hold dear to your heart."
    Narrator "At some point, you tripped and Ari grabbed your hand to steady you. "
    Narrator "He didn’t let go after you were alright, however, and you might have been just fine with that. "

    pause 1.0

    Ari "Alright, Alright, this isn’t all I have planned for our date. "
    Ari "I was going to ask… are you ready for some ice skating!"
    Main "OMG, I love ice skating! "

    menu:
        "I’ll have you know I’m a pro!":
            jump ep5_ari_4_1

        "I’m not that good at it though...":
            jump ep5_ari_4_2

# End of date - Ari falling for DaVie
label ep5_ari_4_1:
    Ari "Ohoho, I'll have to have you help me not fall then. "
    Main "Sounds like a plan!"

    pause 1.0

    Narrator "True to his word, Ari was complete chaos on the ice. "
    Narrator "The amount of time he fell on his butt was hilarious. "

    pause 1.0

    Ari "You're having too much fun with this, do you enjoy having me fall for you that much?"

    pause 1.0

    Narrator "With him, it was easy. The banter flowed between the two and laughter was plenty."
    Narrator "At one point, he began to fall again only for you to steady you in his arms. "
    Narrator "The surrounding scenery seemed to slow and your eyes focused on the warmth in front of you. "

    scene black with dissolve

    stop music fadeout 1.0
    Ari "Can I kiss you?"
    
    play music "music/Heartwarming.mp3" fadein 1.0
    scene cg davie x ari with Fade(1.0, 1.0, 3.0, color="#fff") # Slow transition for dramatic effect

    Narrator "With a silent nod, a pair of lips met one another and the sparks fairytales spoke of finally made sense. "
    Narrator "Winter was not such a cold season after all."
 
    stop music fadeout 3.0
    scene black with Fade(3.0, 3.0, 3.0, color="#fff") # Slow transition for dramatic effect

    jump fin

# End of date - Davie falling for Ari
label ep5_ari_4_2:
    Ari "That's alright, I'll be there to prevent you from falling ;)"
    Main "Okayyy I'll believe you..."

    pause 1.0

    Narrator "True to your word, you were complete chaos on the ice. "
    Narrator "The amount of times you almost fell was hilarious."

    pause 1.0

    Ari "I'm sorry for laughing, I just can't believe you were actually this bad."
    Ari "Do you enjoy falling for me that much?"
    
    pause 1.0

    Narrator "With him, it was easy. The banter flowed between the two and laughter was plenty."
    Narrator "At one point, you began to fall again only for him to steady you in his arms. "
    Narrator "The surrounding scenery seemed to slow and your eyes focused on the warmth in front of you. "

    stop music fadeout 1.0
    scene black with dissolve

    Ari "Can I kiss you?"

    play music "music/Heartwarming.mp3" fadein 1.0
    scene cg davie x ari with Fade(1.0, 1.0, 3.0, color="#fff")  # Slow transition for dramatic effect

    Narrator "With a silent nod, a pair of lips met one another and the sparks fairytales spoke of finally made sense. "
    Narrator "Winter was not such a cold season after all."

    stop music fadeout 3.0
    scene black with Fade(3.0, 3.0, 3.0, color="#fff") # Slow transition for dramatic effect

    jump fin