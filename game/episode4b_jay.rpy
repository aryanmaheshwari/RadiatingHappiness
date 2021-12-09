###############################################################################
# Episode 4B - Jay's Cooking Contest
###############################################################################

###############################################################################
# With Jellie
###############################################################################
label ep4b_jay_1_1:
    scene black with fade

    Narrator "Once you and Jellie got ready, you two boarded the bus that would take you two to the culinary institute's auditorium."
    Narrator "But while on the bus, it seems Jellie wants to ask you something."
    
    pause 1.0

    Jellie "Hey, um I was wondering uh--{nw}"
    Jellie "You know what... nevermind."
    Main "What is it? Stop beating around the bush and just say it!"
    Jellie "Well... I was going to ask if you like Jay? Like {i}like{/i} like?"
    
    menu:
        "Haha no, not at all.":
            pass

        "Um, maybe? I guess I'm still figuring it out...":
            pass

    Jellie "Oh okay, my bad. I was just wondering since you guys have been talking so much lately."
    Main "Don't worry about it, I'm just surprised you'd see us that way, lets just go support him!"

    pause 1.0

    Narrator "After reaching the auditorium, you two paid for your tickets and found seats that had a good view of the station Jay was assigned to-- and oh!"

    scene bg auditorium 
    show jaylin happy:
        xalign 0.0
    with dissolve

    Narrator "He spotted you guys and waved. "
    Narrator "It was a good thing we came so we could see that bright smile."

    Jellie "For now, let's let him concentrate on the competition. We can talk to him afterwards!"
    
    scene black with fade
    Narrator "Watching Jay masterfully chop the ingredients up and work precisely to cook them the right amount stirred something awake in you that you were not yet aware of."

    pause 1.0

    Jellie "Wow, he's really cool when he becomes serious!"

    pause 1.0

    Narrator "You could only nod your head as you became entranced with his professional air."
    Narrator "Soon enough the results of the competition came out with Jay being only in second place."
    Narrator "A shame, but still pretty high for a junior. "
    Narrator "He would definitely have a bright future ahead of him; maybe you could be a part of it."
    
    pause 1.0
    
    scene bg auditorium
    show jaylin happy:
        xalign 0.0
    with dissolve

    Jaylin "Hey guys!"
    
    show jellie normal with easeinright:
        xalign 0.5
    show davie normal with easeinright:
        xalign 0.84

    Jaylin "I'm so happy y'all made it, you guys being there really made me feel like I could win! :)"
    
    show jellie happy
    Jellie "Of course, you were amazing up there! Didn't know you could have such a serious side!"

    show jellie normal
    Jellie "But if you'll excuse me..."

    show jellie happy with ease:
        xalign 1.0
    show davie surprised with ease:
        xalign 0.75
    Jellie "I have to go to the bathroom really bad... haha..."

    hide jellie with easeoutright
    
    show davie normal:
        xalign 0.75
    show jaylin normal:
        xalign 0.25
    with ease

    show davie happy
    Main "Yeah, I wasn't expecting it at all, do you have any plans to celebrate after this?"

    show davie surprised
    show jaylin happy
    Jaylin "Oh yeah, about that, I was wondering if you would like to try the meal I cooked?"

    show jaylin normal
    Jaylin "That's only if you're comfortable with it of course. "

    show jaylin sad
    Jaylin "Ya know what, I shouldn't have asked. You've probably already eaten--"
    
    menu:
        "No! I would love to try what you made!":
            jump ep4b_jay_2_1
        "Aw I'm sorry, I'd love to but I'm going to try to see Ari's fashion show too.":
            jump ep4b_jay_2_2

# Leads to Jay's date
label ep4b_jay_2_1:
    show davie happy
    show jaylin surprised
    Main "It looked absolutely delicious!"

    show jaylin happy
    Jaylin "Really? Then come on over let me plate it for you!!"

    scene black with fade
    menu:
        "Wow, this is amazing! It's literally melting in my mouth.":
            pass
        "I feel like Remy from Ratatouille!":
            pass

    Jaylin "Haha, you flatter me. "

    scene bg auditorium
    show jaylin happy:
        xalign 0.25
    show davie normal:
        xalign 0.75
    with fade

    Jaylin "I was actually also going to ask, would you perhaps want to go to Christmas in the Park with me?"

    show jaylin surprised  
    show davie happy
    Main "Yeah! Jellie was actually talking about it, we were planning on going!"

    show jaylin happy
    show davie surprised
    Jaylin "Oh I actually meant just us?"

    show davie happy
    Main "Just us? Um, sure!"
    Jaylin "Alright! It's a date ♡"

    show jellie normal with easeinright:
        xalign 0.9
        
    show jaylin normal:
        xalign 0.1
    show davie normal:
        xalign 0.5
    with ease

    Jellie "Hey, what's up, what'd I miss?"

    show jaylin happy
    show jellie surprised
    Main "Um, I think... Jay and I are going on a date"

    scene black with fade
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on the feelings you hold for Jay."
    
    jump ep5_jay_1

# Leads to Ari's event
label ep4b_jay_2_2:
    show jaylin sad
    show davie sad
    Main "I should leave soon..."

    show davie normal
    show jaylin normal
    Jaylin "Oh... well, thank you for coming anyway! Enjoy the fashion show! "

    hide jaylin with easeoutleft

    scene black with fade
    Narrator "Jellie decided to stick around the cooking competition to check out the other entries, so you decided to just go ahead to Ari's event. "
    Narrator "Hopefully you won't be too late..."

    jump ep4b_jay_3

###############################################################################
# Without Jellie
###############################################################################
label ep4b_jay_1_2:
    scene black with fade

    Narrator "Once you finished getting ready, you boarded the bus that would take you to the culinary institute's auditorium."
    Narrator "It was a short ride but it gave you time to create expectations for the event."
    Narrator "After reaching the auditorium, you paid for your ticket and found a seat that had a good view of the station Jay was assigned to-- and oh!"

    scene bg auditorium 
    show jaylin happy:
        xalign 0.0
    with dissolve

    Narrator "He spotted you and waved. It was a good thing we came so we could see that bright smile."

    scene black with fade

    Narrator "Watching Jay masterfully chop the ingredients up and work precisely to cook them the right amount stirred something awake in you that you were not yet aware of."
    Narrator "Wow he's really cool when he becomes serious!"
    Narrator "You could only wear a smile as you became entranced with his professional air."
    Narrator "Soon enough the results of the competition came out with Jay being only in second place."
    Narrator "A shame but still pretty high for a junior. "
    Narrator "He would definitely have a bright future ahead of him; maybe you could be a part of it."

    pause 1.0

    scene bg auditorium
    show jaylin happy:
        xalign 0.0
    with dissolve

    Jaylin "Hey [main]! "

    show jaylin happy:
        xalign 0.25
    show davie normal:
        xalign 0.75
    with easeinright
    
    Jaylin "I'm so happy you made it, you being there really made me feel like I could win :)"

    show davie happy
    Main "You were amazing! Even without our support you would do wonderfully, do you have any plans to celebrate after this?"

    show davie surprised
    show jaylin happy
    Jaylin "Oh yeah, about that, I was wondering if you  would like to try the meal I cooked? "
    
    show jaylin normal
    Jaylin "That's only if you're comfortable with it of course. "

    show jaylin sad
    Jaylin "Ya know what, I shouldn't have asked. You've probably already eaten--"

    menu:
        "No! I would love to try what you made!":
            jump ep4b_jay_2_3

        "Aw I'm sorry, I'd love to but I'm going to try to see Ari's fashion show too.":
            jump ep4b_jay_2_4

# Leads to Jay's date
label ep4b_jay_2_3:
    show davie happy
    show jaylin surprised
    Main "It looked absolutely delicious!"
    
    show jaylin happy
    Jaylin "Really? Then come on over let me plate it for you!!"

    scene black with fade
    menu:
        "Wow, this is amazing! It's literally melting in my mouth.":
            pass
        "I feel like Remy from Ratatouille!":
            pass

    Jaylin "Haha, you flatter me. "
    
    scene bg auditorium
    show jaylin happy:
        xalign 0.25
    show davie normal:
        xalign 0.75
    with fade

    Jaylin "I was actually also going to ask, would you perhaps want to go to Christmas in the Park with me?"

    show jaylin surprised  
    show davie happy
    Main "Yeah! Jellie was actually talking about it, we were planning on going!"

    show jaylin happy
    show davie surprised
    Jaylin "Oh I actually meant just us?"
    
    show davie normal
    Main "Just us? Um, sure!"
    Jaylin "Alright! It's a date, I can't wait! ♡"

    show davie surprised
    hide jaylin happy with easeoutleft

    Main "...a date?"

    scene black with fade
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on the feelings you hold for Jay."

    jump ep5_jay_1

# Leads to Ari's event
label ep4b_jay_2_4:
    show jaylin sad
    show davie sad
    Main "I should leave soon..."

    show davie normal
    show jaylin normal
    Jaylin "Oh... well, thank you for coming anyway! Enjoy the fashion show! "

    hide jaylin with easeoutleft
    
    scene black with fade
    Narrator "After a short bus ride and walk you were able to make it to Ari's event."
    Narrator "Hopefully you aren't too late..."

    jump ep4b_jay_3

###############################################################################
# Going to Ari's event after
###############################################################################
# Leads to Ari's date
label ep4b_jay_3:    
    scene bg fashion japanese garden
    show ari happy
    with fade
    Ari "[main]! Over here! "
        
    show davie happy:
        xalign 0.25
    show ari normal:
        xalign 0.75
    with easeinleft

    show ari sad
    show davie surprised
    Ari "You just missed it, we're starting to close up now. :("
    
    show davie sad
    Main "Aw, I'm so sorry..."

    menu:
        "I was busy with some other stuff so time flew by too fast.":
            pass
        "I went to Jay's cooking competition too so it slowed me down a bit.":
            pass

    show ari normal
    Ari "Oh.. It's all good, thank you for coming anyway."

    show ari sad
    Ari "I still wish you were able to see the show."

    show ari normal
    show davie normal
    Ari "What are your plans for later?"
    Main "I'm probably just going to finish up homework and then hit the hay, how about you, how're you going to celebrate your successful show?"

    show ari happy
    Ari "Hahah, I'm probably going to do the same as you, finish up cleaning and hit the hay."
    Ari "I was wondering though, if you had a free schedule next week?"

    show ari normal
    show davie happy
    Main "Yeah, I'm pretty free, what's up?"

    show ari happy
    Ari "You know Christmas in the Park?"
    
    show davie surprised
    Ari "Would you like to go there with me next week, as a date?"

    menu:
        "Oh, um sure?":
            pass
        "Oh, yeah! I think I'd really like that. :)":
            pass

    show davie happy
    Ari "Perfect! I'll see you next week then, get home safely! ♡"

    hide ari with easeoutright
    
    scene black with fade
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."

    jump ep5_ari_1