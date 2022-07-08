############################################
# Main Script
#
# This file is used to code the main script
# of the game. Each scene is invoked in this
# file to build the entire game script.
############################################

label start:
    define user_name = Character("[user_input]")
    python:
        user_input = renpy.input("Hey what's your name", length=32)

        if not user_input:
            user_input = "Monika"

    user_name "It's [user_input], what's yours?"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "hopefully this works"

    e "!"

    # This ends the game.

    return
