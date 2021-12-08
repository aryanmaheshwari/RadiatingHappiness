# Episode 4B Jaylin + Jellie
label start_ep4b_jay_j:
    scene room
    Narrator "Once you and Jellie got ready, you two boarded the bus that would take you two to the culinary institute's auditorium. But while on the bus, it seems Jellie wants to ask you something."
    show jellie normal
    Jellie "Hey, um I was wondering uh- you know what nevermind."
    Main "What is it? Stop beating around the bush and just say it"
    Jellie "Well... I was going to ask if you like Jay? like like like"
    menu:
        "Haha no, not at all":
            jump continue_convo_jd

        "Um, maybe? I guess I'm still figuring it out":
            jump continue_convo_jd

label continue_convo_jd:
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
    Jellie "Of course, you were amazing up there! Didn't know you could have such a serious side
But if you'll excuse me I have to go to the bathroom really bad haha"
    hide jellie happy
    show jaylin happy:
        xpos 0.25
    Main "Yeah, I wasn't expecting it at all, do you have any plans to celebrate after this?"
    Jaylin "Oh yeah, about that, I was wondering if you  would like to try the meal I cooked?"
    Jaylin "That's only if you're comfortable with it of course. Ya know what I shouldn't have asked, you've probably already eaten-"
    menu:
        "No! I would love to try what you made! It looked absolutely delicious":
            jump dinner_jaylin
        "Oh... well, thank you for coming anyway! Enjoy the fashion show":
            jump other_plan

label dinner_jaylin:
    Jaylin "Really? Then come on over let me plate it for you!!"
    menu:
        "Wow this is amazing! It's literally melting in my mouth.":
            jump continue_dinner_convo
        "I feel like Remy from Ratatouille!":
            jump continue_dinner_convo

label continue_dinner_convo:
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
    jump end_ep4BJJ

label other_plan:
    show jellie sad
    Jellie "Oh... well, thank you for coming anyway! Enjoy the fashion show "
    hide jellie sad
    Narrator "Jellie decided to stick around the cooking competition to check out the other entries so you decided to just go ahead to Ari's event. Hopefully you won't be too late"
    jump combined_ending4b

label end_ep4BJJ:
    return
