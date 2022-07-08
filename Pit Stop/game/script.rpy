############################################
# Main Script
#
# This file is used to code the main script
# of the game. Each scene is invoked in this
# file to build the entire game script.
############################################

label start:
    define user_name = Character("[user_input]")
    define k = Character("Kevin Yang")
    python:
        user_input = renpy.input("Hey, what's your name?", length=32)

        if not user_input:
            user_input = "Monika"

    user_name "It's [user_input], what's yours?"
    k "My name is Kevin, your blind date."

    # scene bg room

    # show eileen happy

    return
