label episode2_start:
    scene room
    Headmaster "The first class you'll be taking this semester will be English 1A."
    Headmaster "In order to get there you simply have to cross the Japanese Garden and take a right or was it a left?"
    Headmaster "Oh no... I think we're lost. Maybe we could look around for a map?"

# Episode 2: Jaylin
label jaylin_intro_convo:
    scene room # will be japanese garden
    show jaylin happy
    Jaylin "Hey there, I couldn't help but notice you looked a bit lost."
    Jaylin "Do you need help finding a class?"

    menu:
        "Oh my that's embarassing, but yeah would you know where Sweeney Hall 207 is?":
            jump give_directions

        "Uh......":
            jump jaylin_rejected


label give_directions:
    show jaylin happy
    Jaylin "Yeah!! That's actually on the opposite side of campus next to the Willow tree though, you seem to have gotten quite off track."
    Main "Oh my mistake, my name is [main]."
    jump ask_to_walk

label ask_to_walk:
    show jaylin normal
    Jaylin "If you'd like, I could possibly, maybe, not to force you or anything but I could walk you there?"
    menu:
        "I would appreciate that, please":
            jump jaylin_bonding
        "I think I can figure it out from here but thanks.":
            jump jaylin_rejected

label jaylin_rejected:
    show jaylin sad
    Jaylin "Of course!"
    Jaylin "{size=20}I'm so stupid why would she want to walk with a weird stranger{/size}"
    Main "Did you say something?"
    Jaylin "Uh I'm promoting the cooking club right now, I was just gonna say you should come check us out sometime! "
    Jaylin "Good luck finding your class, I'll see you around."
    Main "Okay, bye!"
    jump common_ending

label jaylin_bonding:
    show jaylin normal
    Headmaster "Jaylin begins leading [main] through campus and the two find out they share some common interests like cooking"
    Main "Speaking of cooking, what's up with the frying pan?"
    jump joke

label joke:
    show jaylin sad
    Jaylin "Oh! This was given to me by my late father so I carry it everywhere I go..."
    show jaylin happy
    Jaylin "Just kidding! I'm promoting the cooking club right now, you should come check us out sometime!"
    menu:
        "haha okay thank you for walking me, bye!":
            jump common_ending
        "that's kind of an insensitive joke, thank you for walking me, bye":
            jump common_ending

label common_ending:
    Headmaster "There may have been some bumps in the road but the day ended without another hitch once [main] found Sweeney Hall. "
    Headmaster "Some potential friends were made and overall the day ended well. "
    Headmaster "Hmm now thinking back to it, [main] never got that student's name. "
    Headmaster "Oh well, it seems the new semester will be a good one after all."
    jump end_episode2

label end_episode2:
    jump episode3_start
