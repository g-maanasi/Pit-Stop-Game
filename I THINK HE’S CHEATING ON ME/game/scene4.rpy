############################################
# Pit Stop #3 Scene
#
# This file encompasses the code and script
# for the gas station rest stop scene. The
# choices made by the user can potentially
# affect their final outcome.
############################################

label gas_station:

    ##########
    # Part 1 #
    ##########

    k "Why do you look so scared?"
    user_name "..."
    k "Please, talk to me."
    user_name ""
    k "Oh please. I’m not going to hurt you."
    k "I could never hurt you."
    user_name ""
    k "I’m guessing you want to ask me what happened, right?"
    user_name ""
    k ".........."
    k "I don’t really want to talk about it if that’s okay."
    user_name "{i}I can barely think straight.{/i}"
    user_name "{i}Nothing will come out.{/i}"
    user_name "{i}Please don’t hurt me.{/i}"
    user_name ""
    user_name "I’m glad you get me."
    user_name "Anyways. We aren’t too far now."

    ##########
    # Part 2 #
    ##########

    # ART_FRAME: back to usual car pov.

    k "Ah, we need gas."
    user_name "..."
    user_name "{i}He left the car.{/i}"
    user_name "{i}I don't see him by the gas pump.{/i}"
    user_name "Now is my chance to escape."

    menu:
        "Unlock the car door":
            user_name "{i}It’s locked. Heh. That would’ve been too easy.{/i}"

        "Scream for help":
            user_name "{i}There’s a man outside. Maybe he’ll notice.{/i}"
