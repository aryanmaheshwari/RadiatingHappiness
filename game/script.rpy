# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Headmaster = Character("Headmaster")
define Jellie = Character("Jellie")
define Main = Character("[main]")
define MainPro = Character("[mainpro]")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    Headmaster "Welcome to Cupid University, a campus of acceptance and excitement.
I’m honored that you all have chosen our prestigious school as your college of choice. I hope your first year will treat you well and you will enjoy your time with us. Now, off you go!"


label initialize_main:
    scene bg room
    $ main = renpy.input("Enter your name: ", length=32)
    $ main = main.strip()
    if not main:
         $ main = "You"
    $ mainpro = renpy.input("Enter your pronouns: ", length=32)
    $ mainpro = mainpro.strip()
    if not main:
         $ mainpro = main

    # successful: Headmaster "Your name is [main] and your pronouns are [mainpro]"


label week1:
    scene bg room
    Headmaster "It’s finally move-in day! Although it’ll be hard living far from home, the exciting experiences at the dorm are waiting for you!"
    Headmaster "Your room number is 1111 - Angel numbers!"
    Headmaster "This year you’ll also be rooming with another freshman, it’s time to meet them :)"

# Episode 1: Jellie
label jellie_intro_convo:
    scene bg room # will be dorm room
    show image "anjnormal.png"
    Jellie "Hey my name is Anjelly, but you can call me Jellie. I'm your roomate this year, it’s nice to meet you!"

    menu:
        "Hi! My name is [main].":
            jump haven_city_convo

        "Nice to meet you?":
            jump fumbled


label fumbled:
    show image "anjsurprised.png"
    Jellie "Oh sorry I didn't catch your name."
    Main "Oh my mistake, my name is [main]."
    jump haven_city_convo


label haven_city_convo:
    show image "anjsurprised.png"
    Jellie "Hm that name sounds familiar, are you from Haven City?"
    menu:
        "Maybe...":
            jump past_connection_convo

        "yeah, how'd you know":
            jump past_connection_convo

label past_connection_convo:
    show image "anjhappy.png"
    Jellie "Don't you remember me, we used to hang out all the time! It's me, Jellybean!"
    menu:
        "Uh yeah I remember now...":
            jump jellie_low_connection

        "OMG how did I forget!! How have you been?":
            jump jellie_high_connection

label jellie_low_connection:
    show image "anjsad.png"
    Headmaster "Feeling slightly rejected, Jellie finishes unpacking and goes to bed. The air feels frigid that night with only hopes of a better morning."
    jump end

label jellie_high_connection:
    show image "anjhappy.png"
    Headmaster "Washed over by a wave of nostalgia, [main] and Jellie talk all night long..."
    jump end

label end:
    jump episode2_start
