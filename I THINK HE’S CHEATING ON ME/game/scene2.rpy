############################################
# Pit Stop #1 Scene
#
# This file encompasses the code and script
# for packing up and the diner stop scene.
# The choices made by the user can
# potentially affect their final outcome.
############################################

label diner:

    scene black
    user_name "{i}ugh...I’m too tired for this.{/i}"

    menu sleeping_in:
        "5 more minutes.":
            # add audio code bc there isn't anything to add...

    user_name "...mmmmh.."
    user_name "{i}Oh man...{/i}"
    user_name "{i}What time is it...5:50?????{/i}"
    user_name "{i}Fuck... Kevin will be here in 10 minutes.{/i}"
    user_name "{i}OKAY! Let's see if I have any last minute packing to do.{/i}"
    # new background Scene

    menu packing:
        user_name "{i}Looks like I have room for one more thing. Should I take anything else?{/i}"

        "Journal" if cheating_count > 0:
            $ pen = True
            user_name "{i}I'll bring this just in case I get bored during the car ride...\
            better bring a pen too, can't forget that.{/i}"
        "Sanitary Pads":
            $ pads = True
            user_name "{i}I'll bring this in case I have an emergency{/i}"
        "Candy":
            $ candyCane = True
            user_name "{i}Ohh I need some snacks for the trip!{/i}"

    scene black
    # audio cue
    # kevin car Scene
    k "You all set [user_name]?"
    user_name "Mhmm! Goodbye Jessie! See you in 3 days!"
    j "Bye Love! Be careful now!"
