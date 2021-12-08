
label ep1_1:
    scene room with Fade(1.5, 1.0, 1.0, color="#fff") # making this fade white gives a cool effect
    show davie normal with easeinleft
    Narrator "It’s finally move-in day "
    show davie sad
    Narrator "Although it’ll be hard living far from home, the exciting experiences at the dorm are waiting for you!"
    show davie happy
    Narrator "Your room number is 1111 - Angel numbers!"
    Narrator "This year you’ll also be rooming with another freshman, it’s time to meet them :)"
    hide davie with easeoutright

    # Episode 1: Jellie
    scene room with fade # will be dorm room
    show davie normal with easeinleft:
        xalign 0.75
    show jellie normal with easeinleft:
        xalign 0.25
    Jellie "Hey my name is Anjelly, but you can call me Jellie."
    $ Jellie = Character("Jellie", color="#c1a99c")
    Jellie "I'm your roomate this year, it’s nice to meet you!"

    menu:
        "Hi! My name is [main].":
            jump ep1_2_1

        "Nice to meet you?":
            jump ep1_2_2

label ep1_2_1:
    jump ep1_3

label ep1_2_2:
    show jellie surprised
    Jellie "Oh sorry I didn't catch your name."
    Main "Oh my mistake, my name is [main]."

label ep1_3:
    show jellie surprised
    Jellie "Hm that name sounds familiar, are you from Haven City?"
    menu:
        "Maybe...":
            pass

        "yeah, how'd you know":
            pass

    show jellie happy
    Jellie "Don't you remember me, we used to hang out all the time! It's me, Jellybean!"
    menu:
        "Uh yeah I remember now...":
            jump ep1_4_1

        "OMG how did I forget!! How have you been?":
            jump ep1_4_2

label ep1_4_1:
    show davie sad
    show jellie sad
    Narrator "Feeling slightly rejected, Jellie finishes unpacking and goes to bed. "

    scene black with dissolve
    Narrator "The air feels frigid that night with only hopes of a better morning."
    jump ep1_5

label ep1_4_2:

    show jellie happy
    show davie happy
    Narrator "Washed over by a wave of nostalgia, [main] and Jellie talk all night long..."
    jump ep1_5

label ep1_5:
    jump ep2_1
