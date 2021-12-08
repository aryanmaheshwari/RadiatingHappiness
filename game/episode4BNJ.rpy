# Episode 4B Jaylin + no Jellie
label start_ep4b_jay_nj:
    scene room
    Narrator "Once you finished getting ready, you boarded the bus that would take you to the culinary institute's auditorium."
    Narrator "It was a short ride but it gave you time to create expectations for the event."
    Narrator "After reaching the auditorium, you paid for your ticket and found a seat that had a good view of the station Jay was assigned to and Oh!"
    Narrator "He spotted you and waved. It was a good thing we came so we could see that bright smile."
    Narrator "Watching Jay masterfully chop the ingredients up and work precisely to cook them the right amount stirred something awake in you that you were not yet aware of."
    Narrator "Wow he's really cool when he becomes serious"
    Narrator "You could only wear a smile as you became entranced with his professional air."
    Narrator "Soon enough the results of the competition came out with Jay being only in second place."
    Narrator "A shame but still pretty high for a junior. He would definitely have a bright future ahead of him, maybe you could be a part of it."
    show jaylin happy
    Jaylin "hey [main]! I'm so happy you made it, you being there really made me feel like I could win :)"
    Main "You were amazing! Even without our support you would do wonderfully, do you have any plans to celebrate after this?"
    Jaylin "Oh yeah, about that, I was wondering if you  would like to try the meal I cooked? That's only if you're comfortable with it of course. Ya know what I shouldn't have asked, you've probably already eaten-"
    menu:
        "No! I would love to try what you made! It looked absolutely delicious":
            jump affirm_jaylin
        "Aw I'm sorry, I'd love to but I'm going to try to see Ari's fashion show too so I should leave soon":
            show jaylin sad
            Jaylin "Oh... well, thank you for coming anyway! Enjoy the fashion show "
            hide jaylin sad
            Narrator "After a short bus ride and walk you were able to make it to Ari's event. Hopefully you aren't too late"
            jump combined_ending4b

label affirm_jaylin:
    Jaylin "Really? Then come on over let me plate it for you!!"
    menu:
        "Wow this is amazing! It's literally melting in my mouth.":
            jump ep4bnj_end
        "I feel like Remy from Ratatouille!":
            jump ep4bnj_end

label ep4bnj_end:
    show jaylin happy
    Jaylin "Haha, you flatter me. I was actually also going to ask, would you perhaps want to go to Christmas in the Park with me?"
    Main "Yeah! Jellie was actually talking about it, we were planning on going!"
    Jaylin "Oh I actually meant just us?"
    Main "Just us? um sure!"
    Jaylin "Alright! It's a date, I can't wait! ♡"
    hide jaylin happy
    show da vie happy
    Main "a date?"
    hide da vie happy
    Narrator "With that, one hectic week finished up with an equally hectic day. Who knows, maybe the twinkling christmas decorations will shine a light on the feelings you hold for Jay."
    return
