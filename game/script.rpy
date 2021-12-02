# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Headmaster = Character("Headmaster", color="#ffffff")
define Narrator = Character("Narrator", color="#ffffff")
define Jellie = Character("???", color="#c1a99c")
define Jaylin = Character("???", color="#bfbf90")
define Ari = Character("???", color="#a34635")
define Main = Character("[main]")
define main_sub = ""
define main_obj = ""


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene school
    show davie normal
    # These display lines of dialogue.

    Headmaster "Welcome to Cupid University, a campus of acceptance and excitement."
    Headmaster "I’m honored that you all have chosen our prestigious school as your college of choice. "
    Headmaster "I hope your first year will treat you well and you will enjoy your time with us. Now, off you go!"


label initialize_main:
    scene school
    show davie happy
    $ main = renpy.input("Enter your name: ", length=32)
    $ main = main.strip()
    if not main:
        $ main = "Da Vie"
    if not main:
        $ mainpro = main
    menu:
        "he/him":
            $ main_sub = "he"
            $ main_obj = "him"
        "she/her":
            $ main_sub = "she"
            $ main_obj = "her"
        "they/them":
            $ main_sub = "they"
            $ main_obj = "them"


label week1:
    scene room
    show davie normal
    Narrator "It’s finally move-in day! "
    Narrator "Although it’ll be hard living far from home, the exciting experiences at the dorm are waiting for you!"
    show davie sad
    Narrator "Your room number is 1111 - Angel numbers!"
    show davie happys
    Narrator "This year you’ll also be rooming with another freshman, it’s time to meet them :)"

# Episode 1: Jellie
label jellie_intro_convo:
    scene room # will be dorm room
    show jellie normal
    Jellie "Hey my name is Anjelly, but you can call me Jellie. "
    $ Jellie = Character("Jellie", color="#c1a99c")
    Jellie "I'm your roomate this year, it’s nice to meet you!"

    menu:
        "Hi! My name is [main].":
            jump haven_city_convo

        "Nice to meet you?":
            jump fumbled


label fumbled:
    show jellie surprised
    Jellie "Oh sorry I didn't catch your name."
    Main "Oh my mistake, my name is [main]."
    jump haven_city_convo


label haven_city_convo:
    show jellie surprised
    Jellie "Hm that name sounds familiar, are you from Haven City?"
    menu:
        "Maybe...":
            jump past_connection_convo

        "yeah, how'd you know":
            jump past_connection_convo

label past_connection_convo:
    show jellie happy
    Jellie "Don't you remember me, we used to hang out all the time! It's me, Jellybean!"
    menu:
        "Uh yeah I remember now...":
            jump jellie_low_connection

        "OMG how did I forget!! How have you been?":
            jump jellie_high_connection

label jellie_low_connection:
    show jellie sad
    Narrator "Feeling slightly rejected, Jellie finishes unpacking and goes to bed. "
    Narrator "The air feels frigid that night with only hopes of a better morning."
    jump end

label jellie_high_connection:
    show jellie happy
    Narrator "Washed over by a wave of nostalgia, [main] and Jellie talk all night long..."
    jump end

label end:
    jump episode2_start
