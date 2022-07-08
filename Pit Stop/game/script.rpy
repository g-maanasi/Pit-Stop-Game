############################################
# Main Script
#
# This file is used to code the main script
# of the game. Each scene is invoked in this
# file to build the entire game script.
############################################

define e = Character("Eileen")


# The game starts here.

label start:

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
