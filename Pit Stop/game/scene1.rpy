############################################
# Beginning Scene
#
# This file is used to prompt the user to
# input the character name, and also will
# conduct the blind date scene at the
# restaurant and the characters packing up
# to go on the road trip
############################################

label start:

    # Character Input; background is intentionally black
    define user_name = Character("[user_input]", color="#ffffff")
    define k = Character("[k]", color="#cc3516")

    $ k = "?????"
    k "Hey, what's your name?"

    python:
        user_input = renpy.input("My name is ...", length=32)
        confirmation = renpy.input("Are you sure with the name [user_input] (y/n)?")

        while confirmation != "y":
            if confirmation == "n":
                user_input = renpy.input("My name is ...", length=32)
            confirmation = renpy.input("Are you sure with the name [user_input] (y/n)?")

        if not user_input:
            user_input = "Monika"

    user_name "[user_input], what's yours?"
    k "My name is Kevin Yang, your blind date."
    $ k = "Kevin Yang"

    # Restaurant Scene

    # scene bg room

    # show eileen happy

    return
