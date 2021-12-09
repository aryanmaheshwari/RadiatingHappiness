###############################################################################
# Episode 4B - Jay's Cooking Contest
###############################################################################

###############################################################################
# With Jellie
###############################################################################
label ep4b_jay_1_1:
    scene bg room
    Narrator "Once you and Jellie got ready, you two boarded the bus that would take you two to the culinary institute's auditorium. But while on the bus, it seems Jellie wants to ask you something."
    
    show jellie normal
    Jellie "Hey, um I was wondering uh- you know what nevermind."
    Main "What is it? Stop beating around the bush and just say it"
    Jellie "Well... I was going to ask if you like Jay? like like like"
    
    menu:
        "Haha no, not at all":
            pass

        "Um, maybe? I guess I'm still figuring it out...":
            pass

    show jellie normal:
        xpos 0.25
    Jellie "Oh okay, my bad I was just wondering since you guys have been talking so much lately"
    
    show jellie happy
    Main "Don't worry about it, I'm just surprised you'd see us that way, lets just go support him!"
    Narrator "After reaching the auditorium, you two paid for your tickets and found seats that had a good view of the station Jay was assigned to and Oh!"
    Narrator "He spotted you guys and waved. It was a good thing we came so we could see that bright smile."
    Jellie "For now, let's let him concentrate on the competition. We can talk to him afterwards!"
    Narrator "Watching Jay masterfully chop the ingredients up and work precisely to cook them the right amount stirred something awake in you that you were not yet aware of."
    Jellie "Wow he's really cool when he becomes serious"
    Narrator "You could only nod your head as you became entranced with his professional air."
    Narrator "Soon enough the results of the competition came out with Jay being only in second place."
    Narrator "A shame but still pretty high for a junior. He would definitely have a bright future ahead of him, maybe you could be a part of it."
    
    show jaylin happy:
        xpos 0.5
    Jaylin "hey guys! I'm so happy y'all made it, you guys being there really made me feel like I could win :)"
    
    show jellie happy
    Jellie "Of course, you were amazing up there! Didn't know you could have such a serious side"
    Jellie "But if you'll excuse me I have to go to the bathroom really bad haha"

    hide jellie happy
    show jaylin happy:
        xpos 0.25
    Main "Yeah, I wasn't expecting it at all, do you have any plans to celebrate after this?"
    Jaylin "Oh yeah, about that, I was wondering if you  would like to try the meal I cooked?"
    Jaylin "That's only if you're comfortable with it of course. Ya know what I shouldn't have asked, you've probably already eaten-"
    
    menu:
        "No! I would love to try what you made!":
            jump ep4b_jay_2_1
        "Aw I'm sorry, I'd love to but I'm going to try to see Ari's fashion show too.":
            jump ep4b_jay_2_2

# Leads to Jay's date
label ep4b_jay_2_1:
    Main "It looked absolutely delicious!"
    Jaylin "Really? Then come on over let me plate it for you!!"

    menu:
        "Wow this is amazing! It's literally melting in my mouth.":
            pass
        "I feel like Remy from Ratatouille!":
            pass

    show jaylin happy:
        xpos 0.25
    Jaylin "Haha, you flatter me. I was actually also going to ask, would you perhaps want to go to Christmas in the Park with me?"
    Main "Yeah! Jellie was actually talking about it, we were planning on going!"
    Jaylin "Oh I actually meant just us?"
    Main "Just us? um sure!"
    show jaylin happy
    Jaylin "Alright! It's a date ♡"
    hide jaylin happy
    show jellie normal:
        xpos 0.5
    Jellie "Hey, what's up, what'd I miss?"
    show jellie surprised
    Main "Um, I think... Jay and I are going on a date"
    hide jellie surprised
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on the feelings you hold for Jay."
    
    jump ep5_jay_1

# Leads to Ari's event
label ep4b_jay_2_2:
    Main "I should leave soon..."

    show jaylin sad
    Jellie "Oh... well, thank you for coming anyway! Enjoy the fashion show "

    hide jaylin sad
    Narrator "Jellie decided to stick around the cooking competition to check out the other entries so you decided to just go ahead to Ari's event. Hopefully you won't be too late"

    jump ep4b_jay_3

###############################################################################
# Without Jellie
###############################################################################
label ep4b_jay_1_2:
    scene bg room
    Narrator "Once you finished getting ready, you boarded the bus that would take you to the culinary institute's auditorium."
    Narrator "It was a short ride but it gave you time to create expectations for the event."
    Narrator "After reaching the auditorium, you paid for your ticket and found a seat that had a good view of the station Jay was assigned to and Oh!"
    Narrator "He spotted you and waved. It was a good thing we came so we could see that bright smile."
    Narrator "Watching Jay masterfully chop the ingredients up and work precisely to cook them the right amount stirred something awake in you that you were not yet aware of."
    Narrator "Wow he's really cool when he becomes serious!"
    Narrator "You could only wear a smile as you became entranced with his professional air."
    Narrator "Soon enough the results of the competition came out with Jay being only in second place."
    Narrator "A shame but still pretty high for a junior. He would definitely have a bright future ahead of him, maybe you could be a part of it."

    show jaylin happy
    Jaylin "Hey [main]! I'm so happy you made it, you being there really made me feel like I could win :)"
    Main "You were amazing! Even without our support you would do wonderfully, do you have any plans to celebrate after this?"
    Jaylin "Oh yeah, about that, I was wondering if you  would like to try the meal I cooked? That's only if you're comfortable with it of course. Ya know what I shouldn't have asked, you've probably already eaten-"

    menu:
        "No! I would love to try what you made! It looked absolutely delicious.":
            jump ep4b_jay_2_3

        "Aw I'm sorry, I'd love to but I'm going to try to see Ari's fashion show too.":
            jump ep4b_jay_2_4

# Leads to Jay's date
label ep4b_jay_2_3:
    Jaylin "Really? Then come on over let me plate it for you!!"

    menu:
        "Wow this is amazing! It's literally melting in my mouth.":
            pass
        "I feel like Remy from Ratatouille!":
            pass

    show jaylin happy:
        xpos 0.25
    Jaylin "Haha, you flatter me. I was actually also going to ask, would you perhaps want to go to Christmas in the Park with me?"
    Main "Yeah! Jellie was actually talking about it, we were planning on going!"
    Jaylin "Oh I actually meant just us?"
    Main "Just us? um sure!"

    show jaylin happy
    Jaylin "Alright! It's a date ♡"

    hide jaylin happy
    show jellie normal:
        xpos 0.5
    Jellie "Hey, what's up, what'd I miss?"

    show jellie surprised
    Main "Um, I think... Jay and I are going on a date"

    hide jellie surprised
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on the feelings you hold for Jay."

    jump ep5_jay_1

# Leads to Ari's event
label ep4b_jay_2_4:
    Main "I should leave soon..."
    Jaylin "Oh... well, thank you for coming anyway! Enjoy the fashion show"
    Narrator "After a short bus ride and walk you were able to make it to Ari's event."
    Narrator "Hopefully you aren't too late."

    jump ep4b_jay_3

###############################################################################
# Going to Ari's event after
###############################################################################
# Leads to Ari's date
label ep4b_jay_3:
    show ari sad
    Ari "[main]! Over here! You just missed it, we're starting to close up now :("
    Main "Aw I'm so sorry..."

    menu:
        "I was busy with some other stuff so time flew by too fast":
            pass
        "I went to Jay's cooking competition too so it slowed me down a bit":
            pass

    show ari sad
    Ari "Oh.. It's all good, thank you for coming anyway. I still wish you were able to see the show. What are your plans for later?"
    Main "I'm probably just going to finish up homework and then hit the hay, how about you, how're you going to celebrate your successful show?"

    show ari normal
    Ari "Hahah, I'm probably going to do the same as you, finish up cleaning and hit the hay"
    Ari "I was wondering though, if you had a free schedule next week?"
    Main "Yeah, I'm pretty free, what's up?"

    show ari happy
    Ari "You know Christmas in the Park?"
    Ari "Would you like to go there with me next week, as a date?"

    menu:
        "Oh, um sure?":
            pass
        "Oh, yeah I think I'd really like that :)":
            pass

    show ari happy
    Ari "Perfect! I'll see you next week then, get home safely  ♡"

    hide ari happy
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."

    jump ep5_ari_1