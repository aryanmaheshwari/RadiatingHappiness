# Declining Ari's date
label ep5_anj:
    stop music fadeout 1.0
    scene black with fade

    Narrator "Although the call goes well, there is still a taste of sadness in the air for disappointing a friend and possibly straining your relationship with them."
    
    Narrator "Perhaps your gloominess was too obvious because soon after Jellie pulled you into a bear hug."
    
    play music "music/Angel Share.ogg"
    
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

    # Unlock the CG
    $ persistent.unlocked_gallery_images.append("jellie_kiss")

    play music "music/Heartwarming.ogg" fadein 1.0
    scene cg davie x jellie with Fade(1.0, 1.0, 3.0, color="#fff") # Slow transition for dramatic effect

    Narrator "Worried that you were overstepping boundaries you cracked your eyes open only to see Jellie also leaning in too."
    Narrator "With a smile, you closed your eyes and the rest was history. "
    Narrator "Maybe college wasn't too bad after all."

    stop music fadeout 3.0
    scene black with Fade(3.0, 3.0, 3.0, color="#fff") # Slow transition for dramatic effect

    jump fin