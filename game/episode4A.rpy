# Episode 4A
label start_ep4a:
    scene room
    Narrator "The week has flown by with assignments and presentations piled up on your plate. Somehow, without even realizing it, it’s now the day of the fashion show and the cooking competition."
    Narrator "After the invitations at the club rush, you had ended up seeing Jay and Ari again."
    Narrator "Surprisingly enough, for two apparent rivals, they were always together whenever you bumped into each other."
    Narrator "Through those walks to classes and lunches in the food court, you became closer to them to the point of considering them to be good friends.
But the day to decide which event to go to has finally come. It’s up to you to choose where to go-- will you pick the right one?"
    show jellie normal
    Jellie "Wakie-wakie sleepy head! It’s 2 pm in the afternoon, ya gotta eat something."
    Main "I’m up, I’ve been awake for hours"
    Jellie "What’s got you so miffed?"
    menu:
        "Tell Jellie about your dilemma":
            jump get_into_it

        "Brush it off and get ready for the day":
            jump brush_off

label brush_off:
    Main "It's nothing, don't worry about it, whats your plan for today"
    Jellie "I dunno, I think I'll just go to a cafe and study for a bit, wanna come with?"
    Main "I would but I've got another event to go to late so I think I'll pass this time, thank you though!"
    menu:
        "Go to Jay's cooking competition":
            jump start_ep4b_jay_nj

        "Go to Ari's fashion show":
            jump start_ep4b_ari_nj


label get_into_it:
    Main "So here's the thing, you know how we were invited to the fashion show and cooking competition?"
    Jellie "Uh yeah? Ari and Jay's events?"
    Main "Well they're both today...at the same time...in completely different locations"
    Jellie "Oh... shit. What are you planning to do?"
    Main "I mean the only thing I can do is go to one but miss the other right? What do you think I should do?"
    Jellie "Hmm well if it was me, I would just go to whichever I was most interested in. Are you sure you wouldn't be able to go to both at some point"
    Main "Yeah maybe, I'll try to work something out. Thanks for the advice"
    Jellie "For sure, so which do you think you'll go to?"
    menu:
        "I'll go to Jay's cooking competition, wanna come with and drool over the food with me?":
            Jellie "Yep! I'll come :)"
            hide jellie normal
            jump start_ep4b_jay_j
        "I think Ari's fashion show, wanna come with and check out the thrift shop too?":
            Jellie "Yep! I'll come :)"
            hide jellie normal
            jump start_ep4b_ari_j
