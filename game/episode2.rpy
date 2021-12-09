label ep2_1:
    scene room with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day
    Narrator "The first class you'll be taking this semester will be English 1A."

    scene japanese garden with dissolve
    Narrator "In order to get there you simply have to cross the Japanese Garden and take a right or was it a left?"

    show davie sad with easeinright:
        xalign 0.75
    Narrator "Oh no... I think we're lost. "
    Narrator "Maybe we could look around for a map?"

    show davie surprised
    show jaylin happy with easeinleft:
        xalign 0.25
    show davie normal
    Jaylin "Hey there, I couldn't help but notice you looked a bit lost."
    Jaylin "Do you need help finding a class?"

    menu:
        "Oh my that's embarassing, but yeah would you know where Sweeney Hall 207 is?":
<<<<<<< HEAD
            Jaylin "Yeah!! That's actually on the opposite side of campus next to the Willow tree though, you seem to have gotten quite off track."
            jump ask_to_walk

        "Uh......":
            Jaylin "Here, let me see your class schedule"
            Jaylin "Hmm, Sweeney Hall. That's on the opposite side of campus next to the Willow tree..."
            jump ask_to_walk
=======
            jump ep2_2_1

        "Uh......":
            jump ep2_2_2

label ep2_2_1:
    show jaylin happy
    Jaylin "Yeah!! "

    show jaylin normal
    Jaylin "That's actually on the opposite side of campus next to the Willow tree though, you seem to have gotten quite off track."

    jump ep2_3

label ep2_2_2:
    show jaylin happy
    Jaylin "Here, let me see your class schedule"

    show jaylin sad
    Jaylin "Hmm, Sweeney Hall. That's on the opposite side of campus next to the Willow tree..."
>>>>>>> 82de09c74c78dc01ff20fd1ff386056fff0457c2

    jump ep2_3

label ep2_3:
    show jaylin normal
    Jaylin "If you'd like, I could possibly, maybe, not to force you or anything but I could walk you there?"
    
    menu:
        "I would appreciate that, please":
            jump ep2_4_1
        "I think I can figure it out from here but thanks.":
            jump ep2_4_2

<<<<<<< HEAD
label jaylin_rejected:
    show jaylin sad
    Jaylin "Of course!"
    Jaylin "{size=20}I'm so stupid why would [main_sub] want to walk with a weird stranger{/size}"
    Main "Did you say something?"
    Jaylin "Uh I'm promoting the cooking club right now, I was just gonna say you should come check us out sometime! "
    Jaylin "Good luck finding your class, I'll see you around."
    Main "Okay, bye!"
    jump common_ending
=======
label ep2_4_1:

    hide jaylin with easeoutleft
    hide davie with easeoutleft
    scene black with dissolve
>>>>>>> 82de09c74c78dc01ff20fd1ff386056fff0457c2

    Narrator "He begins leading [main] through campus and the two find out they share some common interests like cooking"
    
    scene school with dissolve
    
    show jaylin normal with easeinright:
        xalign 0.25
    show davie normal with easeinright:
        xalign 0.75
    Main "Speaking of cooking, what's up with the frying pan?"

    show davie sad
    show jaylin sad
    Jaylin "Oh! This was given to me by my late father so I carry it everywhere I go..."

    show davie surprised
    show jaylin happy
    Jaylin "Just kidding! I'm promoting the cooking club right now, you should come check us out sometime!"

    menu:
        "haha okay thank you for walking me, bye!":
            show davie normal
            hide jaylin with easeoutleft
            jump ep2_5
        "that's kind of an insensitive joke, thank you for walking me, bye":
            show davie angry
            hide jaylin with easeoutleft
            jump ep2_5

label ep2_4_2:
    show jaylin sad
    Jaylin "Of course!"
    
    Jaylin "{size=20}I'm so stupid why would she want to walk with a weird stranger{/size}{nw}"

    show davie sad
    Main "Did you say something?"

    show davie normal
    show jaylin normal
    Jaylin "Uh I'm promoting the cooking club right now, I was just gonna say you should come check us out sometime! "

    Jaylin "Good luck finding your class, I'll see you around."

    Main "Okay, bye!"
    hide jaylin with easeoutleft
    jump ep2_5

label ep2_5:
    scene black with dissolve

<<<<<<< HEAD
label common_ending:
    hide jaylin happy
=======
>>>>>>> 82de09c74c78dc01ff20fd1ff386056fff0457c2
    Narrator "There may have been some bumps in the road but the day ended without another hitch once [main] found Sweeney Hall. "
    Narrator "Some potential friends were made and overall the day ended well. "

    pause 1.0

    Narrator "Hmm now thinking back to it, [main] never got that student's name. "
    Narrator "Oh well, it seems the new semester will be a good one after all."

    jump ep_3
