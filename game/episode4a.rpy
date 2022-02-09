###############################################################################
# Episode 4A: Deciding Where to Go
###############################################################################

# Wake up
label ep4a_1:
    scene black with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day
    
    Narrator "The week has flown by with assignments and presentations piled up on your plate. "
    Narrator "Somehow, without even realizing it, it’s now the day of the fashion show and the cooking competition."
    Narrator "After the invitations at the club rush, you had ended up seeing Jay and Ari again."
    Narrator "Surprisingly enough, for two apparent rivals, they were always together whenever you bumped into each other."
    Narrator "Through those walks to classes and lunches in the food court, you became closer to them to the point of considering them to be good friends."
    Narrator "But the day to decide which event to go to has finally come. "
    Narrator "It’s up to you to choose where to go-- will you pick the right one?"
    
    play music "music/Angel Share.mp3"
    scene bg room 
    show jellie happy
    with Fade(1.5, 1.0, 1.0, color="#000") # making this fade longer conveys a new day

    Jellie "Wakie-wakie sleepy head! " with vpunch

    show jellie normal
    Jellie "It’s 2 pm in the afternoon, ya gotta eat something."

    show jellie normal with ease:
        xalign 0.75
    show davie sad with dissolve:
        xalign 0.25
    Main "I’m up, I’ve been awake for hours."
    
    Jellie "What’s got you so miffed?"
    menu:
        "Tell Jellie about your dilemma":
            jump ep4a_2_1

        "Brush it off and get ready for the day":
            jump ep4a_2_2

# Tell Jellie about your dilemma and go to the event(s) with Jellie
label ep4a_2_1:
    Main "So here's the thing, you know how we were invited to the fashion show and cooking competition?"
    Jellie "Uh yeah? Ari and Jay's events?"
    Main "Well they're both today... at the same time... in completely different locations."

    show jellie surprised
    Jellie "Oh... shit. What are you planning to do?"

    show jellie sad
    Main "I mean the only thing I can do is go to one but miss the other, right?"
    Main "What do you think I should do?"

    show jellie normal
    Jellie "Hmm well if it was me, I would just go to whichever I was most interested in. "
    Jellie "Are you sure you wouldn't be able to go to both at some point?"
    
    show davie normal
    Main "Yeah maybe, I'll try to work something out. Thanks for the advice!"
    Jellie "For sure, so which do you think you'll go to?"

    menu:
        "Jay's cooking competition.\n Wanna come with and drool over the food with me?":
            show jellie happy
            Jellie "Yep! I'll come! :)"
            stop music fadeout 1.0
            jump ep4b_jay_1_1
        "Ari's fashion show.\n Wanna come with and check out the thrift shop too?":
            show jellie happy
            Jellie "Yep! I'll come! :)"
            stop music fadeout 1.0
            jump ep4b_ari_1_1

# Brush off the dilemma and go to the event(s) alone
label ep4a_2_2:
    show jellie sad
    Main "It's nothing, don't worry about it. "
    
    show davie normal
    Main "What's your plan for today?"

    show jellie normal
    Jellie "I dunno, I think I'll just go to a cafe and study for a bit, wanna come with?"
    Main "I would, but I've got another event to go to late so I think I'll pass this time. Thank you though!"

    hide jellie with easeoutright
    show davie normal with ease:
        xalign 0.5

    menu:
        "Go to Jay's cooking competition":
            stop music fadeout 1.0
            jump ep4b_jay_1_2

        "Go to Ari's fashion show":
            stop music fadeout 1.0
            jump ep4b_ari_1_2
