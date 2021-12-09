# Episode 4B Ari + no Jellie
label start_ep4b_ari_nj:
    scene room
    Narrator "Once you finished getting ready, you began your walk towards the school's Japanese Garden where the event was taking place."
    Narrator "It was a short walk but it gave you time to create expectations for the event."
    Narrator "After reaching the garden, you paid for your ticket and found a seat that had a good view of the stage setup."
    Narrator "There's Ari to the right of the stage. It seems he's altering some of the clothes a model is wearing."
    Narrator "Oop he spotted you and is waving now! It's almost as if just seeing us made his aura brighten."
    Narrator "Watching Ari direct the models to the stage and fix all of the minor mishaps put into perspective another version of him that you had rarely seen."
    Narrator "Wow he's really cool when he's designing"
    Narrator "You could only watch in awe as you became entranced with his professional air."
    Narrator "Soon enough the show ended and the announcer began to call out the various designers featured."
    Narrator "When Ari came out, the smile he held showed off a softer side of his that put his usual smirk to shame."
    Narrator "He would definitely have a bright future ahead of him, maybe you could be a part of it."
    show ari happy
    Ari "Hey gorgeous! You coming definitely made the experience much more enjoyable, thank you for showing. How did you like it?"
    Main "You were so impressive, your designs especially blew me away!!"
    Main "Don't tell the others but they were my favorite. Do you have any plans to celebrate this successful show?"
    Ari "Haha actually, I was wondering if you, oh beautiful soul, could accompany me to check out the thrift booths?"
    menu:
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
                        "Oh, yeah I think I'd really like that :)":
                            Ari "Perfect! I'll see you next week then, text me when you get home  ♡"
                            Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
                            Narrator "One hectic week finished up with an equally hectic day."
                            Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."
                            jump start_ari_date
                "This is like Devil wears Prada but not!":
                    Ari "You know it! While on the subject of um whatever we are on, what are you up to next week?"
                    menu:
                        "Wow and this is all recycled material? You've gotta be a genius!":
                            Ari "You know it! While on the subject of um whatever we are on, what are you up to next week?"
                            Main "I'm pretty free, what's up?"
                            Ari "You know Christmas in the Park? Would you like to go there with me next week, as a date?"
                            menu:
                                "OH, um sure?":
                                    Ari "Perfect! I'll see you next week then, text me when you get home  ♡"
                                    hide ari happy
                                "Oh, yeah I think I'd really like that :)":
                                    Ari "Perfect! I'll see you next week then, text me when you get home  ♡"
                                    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
                                    Narrator "One hectic week finished up with an equally hectic day."
                                    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."
                                    jump start_ari_date
                                    hide ari happy
        "Hm well, then I won't hold you up. Thank you for coming! Enjoy the cook-off.":
            hide ari happy
            Narrator "After a short bus ride you were able to make it to Jay's event. Hopefully you aren't too late."
            jump combined_end_ari

label combined_end_ari:
    show jaylin sad
    Jaylin "V! Over here! You just missed it, I got second place :("
    menu:
        "Aw I'm so sorry, I was busy with some other stuff so time flew by too fast":
            jump cont_ari_end
        "Aw I'm so sorry, I went to Ari's fashion show too so it slowed me down a bit":
            jump cont_ari_end

label cont_ari_end:
    show jaylin normal
    Jaylin "Oh.. It's all good, thank you for coming anyway. I'm sorry you weren't able to see the competition."
    Jaylin "What are your plans for later?"
    Main "I'm probably just going to finish up homework and then hit the hay, how about you, how're you going to celebrate your successful win?"
    show jaylin happy
    Jaylin "Hahah, I'm probably going to do the same as you, finish up cleaning and hit the hay"
    Jaylin "I was wondering though, if you had a free schedule next week?"
    Main "Yeah, I'm pretty free, what's up?"
    Jaylin "I was actually also going to ask, would you perhaps want to go to Christmas in the Park with me?"
    Main "Yeah! Jellie was actually talking about it, we were planning on going!"
    Jaylin "Oh I actually meant just us?"
    menu:
        "OH, um sure?":
            Jaylin "Alright! It's a date ♡"
            hide jaylin happy
            Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
            Narrator "One hectic week finished up with an equally hectic day."
            Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on the feelings you hold for Jay."
            jump start_jay_date
        "Oh, yeah I think I'd really like that :)":
            Jaylin "Alright! It's a date ♡"
            hide jaylin happy
            Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
            Narrator "One hectic week finished up with an equally hectic day."
            Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on the feelings you hold for Jay."
            jump start_jay_date
