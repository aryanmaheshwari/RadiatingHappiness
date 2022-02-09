# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Headmaster = Character("Headmaster", color="#ffffff")
define Narrator = Character("Narrator", color="#ffffff")

define Jellie = Character("???", color="#c1a99c")
define Jaylin = Character("???", color="#bfbf90")
define Ari = Character("???", color="#a34635")
define Main = Character("[main]")

define AriJay = Character("Jay and Ari", color="#ffffff")

define main_sub = ""
define main_obj = ""


# The game starts here.

label start:

    scene black with fade

    stop music fadeout 1.0

    Headmaster "Welcome to Cupid University, a campus of acceptance and excitement."
    Headmaster "I’m honored that you all have chosen our prestigious school as your college of choice. "
    Headmaster "I hope your first year will treat you well and you will enjoy your time with us. Now, off you go!"

label initialize_main:
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

    jump ep1_1