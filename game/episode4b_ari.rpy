###############################################################################
# Episode 4B - Ari's Fashion Show
###############################################################################

###############################################################################
# With Jellie
###############################################################################
label ep4b_ari_1_1:
    scene black with fade

    Narrator "Once you and Jellie got ready, you two walked towards the school's Japanese Garden where the event was taking place."
    Narrator "But while walking, it seems Jellie wants to ask you something."

    play music "music/Carpe Diem.mp3"

    scene bg school with dissolve
    show davie normal with easeinleft:
        xalign 0.75
    show jellie normal with easeinleft:
        xalign 0.25

    show jellie happy
    Jellie "Hey, um I was wondering uh--{nw}" 
    
    show jellie normal
    Jellie "You know what... nevermind."

    show davie sad
    Main "What is it? Stop beating around the bush and just say it."

    show jellie happy
    show davie surprised
    Jellie "Well... I was going to ask if you like Ari? Like {i}like{/i} like?"

    menu:
        "Haha no, not at all.":
            pass
        "Um, maybe? I guess I'm still figuring it out...":
            pass

    show davie normal
    show jellie normal
    Jellie "Oh okay, my bad. I was just wondering since you guys have been talking so much lately."

    show jellie happy:
        xpos 0.25
    Main "Don't worry about it, I'm just surprised you'd see us that way. Let's just go support him!"

    hide davie with easeoutright
    hide jellie with easeoutright

    scene black with fade
    Narrator "After reaching the garden, you two paid for your tickets and found seats that had a good view of the stage setup."
    
    scene bg fashion japanese garden 
    show ari normal:
        xalign 1.0
    with dissolve

    Narrator "There's Ari to the right of the stage. "
    Narrator "It seems he's altering some of the clothes a model is wearing."

    pause 1.0

    show ari surprised

    pause 1.0

    show ari happy
    Narrator "Oop, he spotted us and is waving now!"
    Narrator "It's almost as if just seeing us made his aura brighten."

    Jellie "For now, let's let him concentrate on the show. We can talk to him afterwards!"

    scene black with fade
    Narrator "Watching Ari direct the models to the stage and fix all of the minor mishaps put into perspective another version of him that you had rarely seen."

    pause 1.0

    Jellie "Wow, he's really cool when he's designing!"

    pause 1.0

    Narrator "You could only nod your head as you became entranced with his professional air."
    Narrator "Soon enough, the show ended and the announcer began to call out the various designers featured."
    Narrator "When Ari came out, the smile he held showed off a softer side of his that put his usual smirk to shame."
    Narrator "He would definitely have a bright future ahead of him; maybe you could be a part of it."

    pause 1.0

    scene bg fashion japanese garden
    show ari happy:
        xalign 1.0
    with dissolve

    Ari "Hey guys!"

    show jellie normal with easeinleft:
        xalign 0.5
    show davie normal with easeinleft:
        xalign 0.16

    Ari "You guys being here definitely made the experience more enjoyable, thank you for showing. How was it?"

    show ari normal
    show jellie happy
    Jellie "Of course we'd show up! You were amazing back there! "
    
    show jellie normal
    Jellie "The outfits were to die for, but if you'll excuse me..."
    
    show jellie happy with ease:
        xalign 0
    show davie surprised with ease:
        xalign 0.25
    Jellie "I have to go to the bathroom really bad... haha..."

    hide jellie with easeoutleft

    show davie normal:
        xalign 0.25
    show ari normal:
        xalign 0.75
    with ease

    show davie happy
    Main "You truly were impressive, your designs especially blew me away. "
    Main "Do you have any plans to celebrate this successful show?"

    show ari happy
    Ari "Actually, I was wondering if you, oh beautiful soul, could accompany me to check out the thrift booths?"

    menu:
        "Haha, I would absolutely love to!":
            jump ep4b_ari_2_1

        "Aw I'm sorry, I'd love to but I'm going to try to see Jay's cooking competition too.":
            jump ep4b_ari_2_2

# Leads to Ari's date
label ep4b_ari_2_1:
    Main "I'll just text Jellie where we'll be."
    Ari "It's not too far, just to the right of the show. "

    hide ari with easeoutright
    hide davie with easeoutright

    scene black with fade
    scene bg fashion japanese garden with dissolve

    show ari normal with easeinleft:
        xalign 0.75
    show davie normal with easeinleft:
        xalign 0.25

    Ari "Here we are at my booth! :)"

    menu:
        "Wow and this is all recycled material? You've gotta be a genius!":
            pass

        "This is like Devil wears Prada but not!":
            pass

    show ari happy
    Ari "You know it! "

    show ari normal
    Ari "While on the subject of um... whatever we are on, what are you up to next week?"

    show davie normal
    Main "I'm pretty free, what's up?"
    Ari "You know Christmas in the Park? "

    show davie surprised
    Ari "Would you like to go there with me next week, as a date?"

    menu:
        "Oh, um sure?":
            pass

        "Oh, yeah! I think I'd really like that. :)":
            pass

    show davie happy
    Ari "Perfect! I'll see you next week then, text me when you get home. ♡"
    
    hide ari happy with easeoutright

    scene black with fade
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath. "
    Narrator "One hectic week finished up with an equally hectic day. "
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."
    
    jump ep5_ari_1

# Leads to Jay's event
label ep4b_ari_2_2:
    show ari sad
    show davie sad
    Main "I should leave soon..."
    Ari "Hm well, then I won't hold you up. "

    show davie normal
    show ari normal
    Ari "Thank you for coming! Enjoy the cook-off."

    hide ari with easeoutright

    scene black with fade
    Narrator "Jellie decided to stick around the thrift booths to check out the other designers, so you decidecd to just go ahead to Jay's event. "
    Narrator "Hopefully you won't be too late..."

    jump ep4b_ari_3

###############################################################################
# Without Jellie
###############################################################################
label ep4b_ari_1_2:
    scene black with fade

    Narrator "Once you finished getting ready, you began your walk towards the school's Japanese Garden where the event was taking place."
    Narrator "It was a short walk, but it gave you time to create expectations for the event."
    Narrator "After reaching the garden, you paid for your ticket and found a seat that had a good view of the stage setup."
    
    scene bg fashion japanese garden 
    show ari normal:
        xalign 1.0
    with dissolve

    Narrator "There's Ari to the right of the stage. "
    Narrator "It seems he's altering some of the clothes a model is wearing."

    pause 1.0

    show ari surprised

    pause 1.0

    show ari happy
    Narrator "Oop he spotted you and is waving now! "
    Narrator "It's almost as if just seeing you made his aura brighten."

    scene black with fade
    Narrator "Watching Ari direct the models to the stage and fix all of the minor mishaps put into perspective another version of him that you had rarely seen."

    Narrator "Wow, he's really cool when he's designing."
    Narrator "You could only watch in awe as you became entranced with his professional air."
    Narrator "Soon enough, the show ended and the announcer began to call out the various designers featured."
    Narrator "When Ari came out, the smile he held showed off a softer side of his that put his usual smirk to shame."
    Narrator "He would definitely have a bright future ahead of him; maybe you could be a part of it."
    
    pause 1.0

    scene bg fashion japanese garden
    show ari happy:
        xalign 1.0
    with dissolve

    Ari "Hey gorgeous! "

    show davie normal:
        xalign 0.25
    show ari happy:
        xalign 0.75
    with easeinleft
    
    Ari "You coming definitely made the experience much more enjoyable, thank you for showing. How did you like it?"

    show ari normal
    show davie happy
    Main "You were so impressive, your designs especially blew me away!!"
    Main "Don't tell the others, but they were my favorite. "
    Main "Do you have any plans to celebrate this successful show?"

    show ari happy
    Ari "Haha actually, I was wondering if you, oh beautiful soul, could accompany me to check out the thrift booths?"
    
    menu:
        "Haha, I would absolutely love to!":
            jump ep4b_ari_2_3

        "Aw I'm sorry, I'd love to but I'm going to try to see Jay's cooking competition too.":
            jump ep4b_ari_2_4

# Leads to Ari's date
label ep4b_ari_2_3:
    Main "I'll just text Jellie where we'll be."
    Ari "It's not too far, just to the right of the show. "
    
    hide ari with easeoutright
    hide davie with easeoutright
    
    scene black with fade
    scene bg fashion japanese garden with dissolve

    show ari normal with easeinleft:
        xalign 0.75
    show davie normal with easeinleft:
        xalign 0.25

    Ari "Here we are at my booth! :)"
    menu:
        "Wow and this is all recycled material? You've gotta be a genius!":
            pass

        "This is like Devil wears Prada but not!":
            pass

    show ari happy
    Ari "You know it! "
    
    show ari normal
    Ari "While on the subject of um... whatever we are on, what are you up to next week?"
    
    show davie normal
    Main "I'm pretty free, what's up?"
    Ari "You know Christmas in the Park?"
    
    show davie surprised

    Ari "Would you like to go there with me next week, as a date?"
    
    menu:
        "Oh, um sure?":
            pass

        "Oh, yeah! I think I'd really like that. :)":
            pass

    show davie happy
    Ari "Perfect! I'll see you next week then, text me when you get home. ♡"
    
    hide ari with easeoutright

    scene black with fade
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."

    stop music fadeout 1.0

    jump ep5_ari_1

# Leads to Jay's event
label ep4b_ari_2_4:
    show ari sad
    show davie sad
    Main "I should leave soon..."
    Ari "Hm well, then I won't hold you up. "
    
    show davie normal
    show ari normal
    Ari "Thank you for coming! Enjoy the cook-off."

    hide ari with easeoutright

    scene black with fade
    Narrator "After a short bus ride you were able to make it to Jay's event. "
    Narrator "Hopefully you aren't too late..."
    
    stop music fadeout 1.0

    jump ep4b_ari_3

###############################################################################
# Going to Jay's event after
###############################################################################
# Leads to Jay's date
label ep4b_ari_3:
    scene bg auditorium
    show jaylin happy
    with fade
    Jaylin "[main]! Over here! "

    show davie happy:
        xalign 0.75
    show jaylin normal:
        xalign 0.25
    with easeinright

    show jaylin sad
    show davie surprised
    Jaylin "You just missed it, I got second place :("

    show davie sad
    Main "Aw, I'm so sorry..."

    menu:
        "I was busy with some other stuff so time flew by too fast.":
            pass
        "I went to Ari's fashion show too so it slowed me down a bit.":
            pass

    show jaylin normal
    Jaylin "Oh.. It's all good, thank you for coming anyway. "

    show jaylin sad
    Jaylin "I'm sorry you weren't able to see the competition."

    show jaylin normal
    show davie normal
    Jaylin "What are your plans for later?"
    Main "I'm probably just going to finish up homework and then hit the hay, how about you, how're you going to celebrate your successful win?"

    show jaylin happy
    Jaylin "Hahah, I'm probably going to do the same as you, finish up cleaning and hit the hay."
    Jaylin "I was wondering though, if you had a free schedule next week?"

    show jaylin normal
    show davie happy
    Main "Yeah, I'm pretty free, what's up?"
    
    show jaylin happy
    show davie normal
    Jaylin "I was actually also going to ask, would you perhaps want to go to Christmas in the Park with me?"

    show jaylin surprised  
    show davie happy
    Main "Yeah! Jellie was actually talking about it, we were planning on going!"

    show jaylin happy
    show davie surprised
    Jaylin "Oh I actually meant just us?"

    menu:
        "Oh, um sure?":
            pass
        "Oh, yeah I think I'd really like that :)":
            pass

    show davie normal
    Jaylin "Alright! It's a date! ♡"

    scene black with fade
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on the feelings you hold for Jay."

    jump ep5_jay_1