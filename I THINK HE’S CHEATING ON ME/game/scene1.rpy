############################################
# Beginning Scene
#
# This file is used to prompt the user to
# input the character name, and also will
# conduct the blind date scene at the
# restaurant and the characters packing up
# to go on the road trip.
############################################

label start:

    # Character Input; background is intentionally black
    default character_choices = []
    default user_name = Character("[user_input]", color="#ffffff")
    default k = Character("[k]", color="#cc3516")

    $ k = "?????"
    k "Hey, what's your name?"

    python:
        user_input = renpy.input("My name is ...", length=32)
        confirmation = renpy.input("Are you sure with the name [user_input] (y/n)?")

        while confirmation.lower() != "y":
            if confirmation.lower() == "n":
                user_input = renpy.input("My name is ...", length=32)
            confirmation = renpy.input("Are you sure with the name [user_input] (y/n)?")

        if not user_input:
            user_input = "6ix9ine"

    user_name "[user_input], what's yours?"
    k "My name is Kevin Yang, your blind date."
    $ k = "Kevin Yang"

    # Restaurant Scene

    # scene bg room

    # show eileen happy

    jump getting_ready

label getting_ready:

    scene bg black # shows black background

    user_name "..."
    user_name "{i}God where are my pants...{/i}"
    user_name "..."
    user_name "{i}Or should I wear shorts...?{/i}"
    user_name "..."

    # add scene of main_character holding up her pants and shorts

    user_name "{i}Well it's San Antonio so it's bound to be hot as hell...{/i}"
    user_name "{i}But these are Kevin’s favorite pants! ♥{/i}"
    # audio cue

    # new art frame
