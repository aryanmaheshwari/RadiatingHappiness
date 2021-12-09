label start_jay_date:
    scene room
    Narrator "*over voicemail*"
    Jay "Hey [main], just calling to remind you of our date tomorrow. I can't wait, I'll see you then!"
    show jellie normal
    Main "Hey Jellie, can I ask you a question?"
    Jellie "Yeah go ahead, whats up"
    Main "Do you think going on a date with Jay will be weird?"
    Jellie "Hmm, depends. Do you think you could see him in a romantic way? Because if not maybe its better to just decline the date and keep your friendship."
    Jellie "But really, its all about what you are most comfortable with."
    menu:
        "Yeah.. thank you Jellie, that cleared up a lot. I think I'm going to decline the date.":
            hide jellie normal
            Narrator "Although the call goes well, there is still a taste of sadness in the air for disappointing a friend and possibly straining your relationship with them."
            Narrator "Perhaps your gloominess was too obvious because soon after Jellie pulled you into a bear hug."
            show jellie normal
            Jellie "Rejecting someone is hard, I'm proud of you for not chickening out. I'm heading home for the break, do you think you'll be okay alone?"
            Jellie "Or actually- do you want to come over?"
            menu:
                "Yeah, I think I'd like that.":
                    Jellie "Yay! Alright lets start packing then!"
                    Narrator "And with that your winter break began in the comfort of Jellie's family home."
                    Narrator "You guys drank hot cocoa, watched stupid romcoms, and cuddled by the fireplace."
                    Narrator "The comfort you felt in her arms was everything you'd ever wanted."
                    Narrator "Finally, one thing led to another and you found yourself leaning in for a kiss."
                    Narrator "Worried that you were overstepping, you cracked your eyes open only to see Jellie also leaning in too."
                    Narrator "With a smile you closed your eyes and the rest was history. Maybe college wasn't too bad after all."
                    jump fin
                "Oh no, I couldn't intrude.":
                    Jellie "Nonsense! You're coming with! Now start packing :)"
                    Jellie "Yay! Alright lets start packing then!"
                    Narrator "And with that your winter break began in the comfort of Jellie's family home."
                    Narrator "You guys drank hot cocoa, watched stupid romcoms, and cuddled by the fireplace."
                    Narrator "The comfort you felt in her arms was everything you'd ever wanted."
                    Narrator "Finally, one thing led to another and you found yourself leaning in for a kiss."
                    Narrator "Worried that you were overstepping boundaries, you cracked your eyes open only to see Jellie also leaning in too."
                    Narrator "With a smile you closed your eyes and the rest was history. Maybe college wasn't too bad after all."
                    jump fin
        "Yeah.. thank you Jellie, that cleared up a lot. I think I'm going to try going to the date.":
            hide jellie normal
            jump continue_date_Jay
label continue_date_Jay:
    Narrator "You decide to reply to Jay through a text with an equally excited response. Which soon becomes hearted by the blushing boy."
    Narrator "It's now the day of the fated date! You've completed all the chores on your list in preparation for this. You can only hope it goes as well as you want it to. Maybe this winter you won't be as alone as before."
    Main "Jay told me to meet him by the Santa so... Ah there he is!"
    show jay normal
    Jay "Hey, I hope its not too cold for you! You wanna walk around and check out the lights for a bit?"
    Main "I'm warm enough don't worry, I'd love to see the lights with you"
    Narrator "You two took in the lights around you and began to make conversation starting from small talk to the deeper talks about things you hold dear to your heart."
    Narrator "At some point, you tripped and Jay grabbed your hand to steady you. He didn’t let go after you were alright, however, and you might have been just fine with that. "
    Jay "Hmm, your hands seem pretty cold, how about we head into that cafe and order some drinks?"
    menu:
        "Sounds good, my treat!":
            show jay happy
            Jay "Nooooo I asked you on the date, I get to pay"
            Main "Only if you get there first!"
            Narrator "Racing to get to the cafe, Jay arrives first, holding the door open just in time for the rush of gingerbread scented air wash over the two of you"
            Narrator "The cafe is a quaint little place with soft Christmas music playlist playing in the background. You two settle at one of the tables after ordering."
            jump common_end_Jay_date
        "Great idea! I could use some warmth":
            show jay happy
            Jay "Haha lets head on in then"
            Main "The rush of gingerbread scented air over the two of you washed away the cold from outside in a flash."
            Narrator "The cafe is a quaint little place with soft Christmas music playlist playing in the background. You two settle at one of the tables after ordering."
            jump common_end_Jay_date

label common_end_Jay_date:
    hide jay happy
    Narrator "Unfortunately to you, Z was able to pay for both drinks by distracting you with a dog in a santa outfit"
    Narrator "Amused by his refusal to let you buy him anything you spend the next minutes trying to figure out what he would want as a present."
    Narrator "With you spitting out random guesses that get worse every time and him denying every single one, you two fall into laughter."
    Narrator "After the 10 millionth guess and 10 millionth denial, his pout seems just too cute for you too handle."
    Narrator "Before you know it you find yourself leaning in and meeting his lips with yours."
    Narrator "Let it be known that the shock of his crush kissing him jolted him so bad that Jay opened his eyes for the first time and boy were they beautiful."
    Narrator "You'd have to kiss him more often to see those eyes again. Not that you mind"
    Narrator "After all, winter is not such a cold season."
    jump fin

label fin:
    return
