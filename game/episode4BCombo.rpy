# Episode 4B Combo ending negative
label combined_ending4b:
    show ari sad
    Ari "[main]! Over here! You just missed it, we're starting to close up now :("
    menu:
        "Aw I'm so sorry, I was busy with some other stuff so time flew by too fast":
            jump continue_ari_convo_4b
        "Aw I'm so sorry, I went to Jay's cooking competition too so it slowed me down a bit":
            jump continue_ari_convo_4b

label continue_ari_convo_4b:
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
        "OH, um sure?":
            jump end_ari_convo_4bjj
        "Oh, yeah I think I'd really like that :)":
            jump end_ari_convo_4bjj

label end_ari_convo_4bjj:
    show ari happy
    Ari "Perfect! I'll see you next week then, get home safely  ♡"
    hide ari happy
    Narrator "Back at the dorms after washing up, you finally get a chance to catch your breath."
    Narrator "One hectic week finished up with an equally hectic day."
    Narrator "Who knows, maybe the twinkling christmas decorations will shine a light on any possible feelings you have for Ari."
    return
