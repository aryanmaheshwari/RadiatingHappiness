# Episode 4B Ari + no Jellie
label start_ep4b_ari_j:
    scene room
    Narrator "Once you and Jellie got ready, you two walked towards the school's Japanese Garden where the event was taking place."
    Narrator "But while walking, it seems Jellie wants to ask you something."
    show jellie normal
    Jellie "Hey, um I was wondering uh- you know what nevermind"
    Main "What is it? Stop beating around the bush and just say it"
    Jellie "Well... I was going to ask if you like Ari? like like like"
    menu:
        "Haha no, not at all":
            jump cont_jellie_convo_ari
        "Um, maybe? I guess I'm still figuring it out":
            jump cont_jellie_convo_ari

label cont_jellie_convo_ari:
    Jellie "Oh okay, my bad I was just wondering since you guys have been talking so much lately"
    show jellie happy:
        xpos 0.25
    Jellie "Don't worry about it, I'm just surprised you'd see us that way, lets just go support him!"
    Narrator "After reaching the garden, you two paid for your tickets and found seats that had a good view of the stage setup."
    Narrator "There's Ari to the right of the stage. It seems he's altering some of the clothes a model is wearing."
    Narrator "Oop he spotted us and is waving now! It's almost as if just seeing us made his aura brighten."
    Jellie "For now, let's let him concentrate on the show. We can talk to him afterwards!"
    Narrator "Watching Ari direct the models to the stage and fix all of the minor mishaps put into perspective another version of him that you had rarely seen."
    Jellie "Wow he's really cool when he's designing"
    Narrator "You could only nod your head as you became entranced with his professional air."
    Narrator "Soon enough the show ended and the announcer began to call out the various designers featured."
    Narrator "When Ari came out, the smile he held showed off a softer side of his that put his usual smirk to shame."
    Narrator "He would definitely have a bright future ahead of him, maybe you could be a part of it."
    show ari happy:
        xpos 0.5
    Ari "hey guys! You guys being here definitely made the experience more enjoyable, thank you for showing. How was it?"
    Jellie "Of course we'd show up! You were amazing back there! The outfits were to die for but if you'll excuse me I have to go to the bathroom really bad haha"
    Main "You truly were impressive, your designs especially blew me away. Do you have any plans to celebrate this successful show?"
    Ari "Actually, I was wondering if you, oh beautiful soul, could accompany me to check out the thrift booths?"
    menu:
        "Aw I'm sorry, I'd love to but I'm going to try to see Jay's cooking competition too so I should leave soon":
            Ari " Hm well, then I won't hold you up. Thank you for coming! Enjoy the cook-off."
            Ari "Jellie decided to stick around the thrift booths to check out the other designers so you decidecd to just go ahead to Jay's event. Hopefully you won't be too late"
            jump combined_end_ari
        "Haha, I would absolutely love to! I'll just text Jellie where we'll be":
            Ari "It's not too far, just to the right of the show. Here we are at my booth :)"
            menu:
                "Wow and this is all recycled material? You've gotta be a genius!":
                    Ari "You know it! While on the subject of um whatever we are on, what are you up to next week?"
                    Main "I'm pretty free, what's up?"
                    Ari "You know Christmas in the Park? Would you like to go there with me next week, as a date?"
                    menu:
                        "OH, um sure?":
                            Ari "Perfect! I'll see you next week then, text me when you get home  ♡"
                            hide ari happy
                            Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath.  One hectic week finished up with an equally hectic day. Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."
                        "Oh, yeah I think I'd really like that :)":
                            Ari "Perfect! I'll see you next week then, text me when you get home  ♡"
                            hide ari happy
                            Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath.  One hectic week finished up with an equally hectic day. Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."
                "This is like Devil wears Prada but not!":
                    Ari "You know it! While on the subject of um whatever we are on, what are you up to next week?"
                    Main "I'm pretty free, what's up?"
                    Ari "You know Christmas in the Park? Would you like to go there with me next week, as a date?"
                    menu:
                        "OH, um sure?":
                            Ari "Perfect! I'll see you next week then, text me when you get home  ♡"
                            hide ari happy
                            Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath.  One hectic week finished up with an equally hectic day. Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."
                        "Oh, yeah I think I'd really like that :)":
                            Ari "Perfect! I'll see you next week then, text me when you get home  ♡"
                            hide ari happy
                            Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath.  One hectic week finished up with an equally hectic day. Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."
