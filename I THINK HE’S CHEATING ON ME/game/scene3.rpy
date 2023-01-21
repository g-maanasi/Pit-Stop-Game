############################################
# Pit Stop #2 Scene
#
# This file encompasses the code and script
# for the Ducee's rest stop scene. The
# choices made by the user can potentially
# affect their final outcome.
############################################

label car_ride2:

    ##########
    # Part 1 #
    ##########

    k "So..."
    k "Did you dream about anything?"
    user_name "Uh... yeah!"
    user_name "I had a dream of you and me together on a cloud and we had a\
    kitten and we were all happy together! ♥"
    k "Sometimes you are really adorable, you know that?"
    user_name "{i}Wonder if he says the same thing to her.{/i}"
    user_name "Hehe..!"
    user_name "{i}This milkshake is cold.{/i}"
    user_name "{i}But I don’t exactly want to move his phone either.{/i}"
    user_name "..."
    user_name "{i}I’ll just put it on the door cup holder.{/i}"

    # ART_FRAME: zoom in on the car cup holder. It is empty other than the fact
    # that there is a fake acrylic nail.

    user_name "..."
    user_name "{i}What the hell is that? Whose the hell is that?{/i}"
    user_name "{i}I’ve never worn acrylics before.{/i}"
    user_name "{i}I can’t take this anymore. I have to say something.{/i}"

    # ART_FRAME: zoom back to normal car pov. Phone in cupholder. Milkshake in cup.

    user_name "Hey, Kevvie?"
    k "Yeah, baby?"
    user_name "Why is there a fake nail in the side cup holder..."
    k "A what?"

    if "Confrontational" in character_choices:
        k "Oh so you think I’m involved with other girls again? Is that it,\
        [user_name]"

        menu:
            "I never said that.":
                user_name "I..."
                user_name "I never said that Kevin."
                k "You didn’t have to."
                k "I’m not stupid. I know that’s what you're implying."
                k "Do you seriously think that I have time to cheat on you?"
                k "I don’t even have time for you, let alone another girl."
                user_name "Then whose nail is this?"
                k "It’s probably one of my coworkers."
                user_name "{i}Whose, Kayla’s?{/i}"
                user_name "{i}I can’t ask him that though.{/i}"
                user_name "..."
                k "I have to drive around my coworkers a lot for meetings."
                k "Don’t worry about it. I promise it’s nothing."
                user_name "Okay."

            "...":
                user_name "..."
                k "You can’t just start these things and say nothing, [user_name]."
                k "I know what you’re implying."
                k "Do you really think I have time to cheat on you?"
                user_name "..."
                k "Okay, stay silent then."
                k "..."
                k "It was probably a coworker’s. I have to drive people around often."
                k "Don’t worry."
                user_name "{i}Whose, Kayla’s?{/i}"
                user_name "{i}I can’t ask him that though.{/i}"
                user_name "Okay."
    else:
        k "A fake nail?"
        k "Huh."
        k "Probably just one of my coworker’s nails."

        menu:
            "Why are you driving your coworkers around?":
                $ character_choices.append("Confrontational 2")
                user_name "Why exactly would you need to drive your coworkers around?"
                k "Woah, woah! No need to get defensive."
                k "Sometimes we have meetings around town and I have to drive\
                them around town."
                k "One of them really likes to get dressed up and has those clanky\
                things on. Definitely just fell off."
                k "Don’t worry about it."
                user_name "Okay!"

            "Oh, okay":
                user_name "{i}His {b}coworker’s{/b}?{/i}"
                user_name "{i}Could be Kayla’s.{/i}"
                user_name "{i}I can’t ask him about that though.{/i}"
                user_name "Oh, okay."
                k "Mhm!"
                k "Probably just fell off when I was driving ‘em to a meeting."
                user_name "..."

    user_name "Let’s talk about something else"

    if "Confrontational" in character_choices or "Confrontational 2" in character_choices:
        k "Then please stop accusing me of things, okay?"
        user_name "Okay."
        k "..."
        k "Okay. We are about an hour into the ride. Two more to go."
    else:
        k "Sure!"
        k "What do ya wanna talk about?"
        user_name "I don't know."
        k "Hmm... we are about an hour into the ride. Two more to go!"

    k "You know what I think we should do?"
    user_name "Hm?"
    k "What if we got some snacks from Ducee’s?"
    user_name "...I think that would be nice."
    k "Aww, c’mon! Cheer up, baby!"
    user_name "..."
    user_name "{i}Maybe it is a good thing to just forget about it.{/i}"
    user_name "Sounds good, Kevvie!"
    k "That's what I like to hear!"
    k "I know that there's one that's about 25 miles from here. Shouldn't\
    take us more than 30 to get there."
    user_name "Okay! ♥"
    k "Hmm..."
    k "In order to burn time, let’s play a game."
    user_name "Like what, Kevvie?"
    k "Oh I don’t know."
    k "Can you think of something?"
    user_name "What about eye-spy?"
    k "Oh man..."
    k "I haven’t played that since I was a kid!"
    k "Let’s do it!"
    user_name "Yay, okay!"
    k "Okay. I'll start first."
    k "Eye Spy with my little eye... something round!"

    menu:
        "Air freshener!":
            user_name "The air freshener!"
            k "Haha, you got it! Went easy on you this time."
        "The snowflakes!":
            user_name "Uhh... the snowflakes!"
            k "Nope! It was the Air freshener! Thought I went easy on you too."
        "The parking sticker!":
            user_name "The parking sticker!"
            k "Nope! It was the Air freshener! Thought I went easy on you too."

    k "Anyways... your turn!"
    user_name "{i}Hmm...{/i}"
    user_name "{i}What should I choose?{/i}"

    menu:
        "Look on the dashboard":
            # ART_FRAME: Zooms in on the dashboard. There's nothing there
            user_name "{i}There’s nothing there at all...{/i}"
            menu:
                "Look down":
                    # ART_FRAME: It zooms in on her feet. She notices that there
                    # is another fake nail on her left foot.

                    user_name "..."

                    # ART_FRAME: There is a close up of her face. She looks disgusted.

    # ART_FRAME: Back to normal car pov.
    user_name "{i}I’ll choose my milkshake.{/i}"
    user_name "Okay, got it!"
    user_name "Eye-Spy with my little eye... something brown!"
    k "Your... milkshake?"
    user_name "Huh? You got it so fast already!"
    k "...Are you serious?"
    user_name "Yeah!"
    k "Haha, nice!"
    k "I’m so smart."
    k "Okay, okay my turn now. Eye-spy with my little eye..."

    jump ducees

label ducees:

    ##########
    # Part 2 #
    ##########

    scene black
    # ART_FRAME: Duccee’s interior view

    k "We finally made it."
    k "All that driving is making me damn near delirious."
    user_name "Hehe! Same. Let’s take a break."
    user_name "{i}I need to clear my head.{/i}"
    user_name "I’m gonna go walk around for Lemon Crisps and Ducky Nuggets!"
    k "Come back to the front of the store when you’re done."
    user_name "Okay!"

    # ART_FRAME: Changes to an array of food shelves

    user_name "{i}Found ‘em!{/i}"
    user_name "{i}I still need a break before I get back in that car though.{/i}"
    user_name "{i}I’ll just keep walking around.{/i}"

    # ART_FRAME: Changes to a wall with a corkboard and employee of the month on the wall.
    # ART_FRAME: Zooms in on corkboard.

    user_name "{i}I guess I’ll just stare at these{/i}"

    $ check_promotion_ad = False
    $ check_ads = False

    menu corkboard:
        "Examine the resort promotion." if check_promotion_ad == False:
            user_name "{i}Hey, that’s where we are going!{/i}"
            user_name "{i}Wait... opening next year?{/i}"
            user_name "{i}This is probably wrong.{/i}"
            $ check_promotion_ad = True
            jump corkboard
        "Examine the advertisements." if check_ads == False:
            user_name "{i}Boring.{/i}"
            $ check_ads = True
            jump corkboard
        "Examine the missing posters.":
            # ART_FRAME: Zooms in on MC’s face. She has a terrified look on her face.

            user_name "..."


    # ART_FRAME: Zooms in on the missing poster in the center. It is Kayla.

    user_name "{i}It can’t be.{/i}"
    user_name "{i}It can’t be her.{/i}"
    user_name "{i}Kayla...{/i}"
    user_name "..."
    user_name "..."

    # ART_FRAME: Flash back to the picture of Kayla on his phone when she was
    # looking through it.

    user_name "{i}It’s the same girl that was on his phone...{/i}"
    user_name "..."

    # ART_FRAME: Zooms in on MC’s face. She has a terrified look on her face.
    # THE FRAME IS NOW SHAKING.

    user_name "{i}What do I do{/i}"
    user_name "{i}What do I do{/i}"
    user_name "{i}{b}What did he do?{/b}{/i}"
    user_name "{i}{b}WHAT DO I DO?{/b}{/i}"

    scene black
    menu:
        "KEEP CALM":
            menu:
                "EVERYTHING WILL BE OKAY":
                    menu:
                        "EVERYTHING WILL BE OKAY":
                            menu:
                                "LEAVE NOW":
                                    k "Is everything okay, [user_name]?"
                                "ESCAPE NOW":
                                    k "Is everything okay, [user_name]?"

                        "EVERYTHING WILL NOT BE OKAY":
                            menu:
                                "ESCAPE NOW":
                                    k "Is everything okay, [user_name]?"
                                "EVERYTHING IS FINE":
                                    k "Is everything okay, [user_name]?"

                "YOU NEED TO LEAVE NOW":
                    menu:
                        "WHERE DO I GO":
                            menu:
                                "ESCAPE NOW":
                                    k "Is everything okay, [user_name]?"
                        "WHERE DO I GO":
                            menu:
                                "ESCAPE NOW":
                                    k "Is everything okay, [user_name]?"

        "EVERYTHING WILL BE OKAY":
            menu:
                "EVERYTHING WILL BE OKAY":
                    menu:
                        "YOU NEED TO LEAVE":
                            menu:
                                "YOU’RE OVERTHINKING":
                                    k "Is everything okay, [user_name]?"
                                "ESCAPE NOW":
                                    k "Is everything okay, [user_name]?"

                        "YOU NEED TO LEAVE":
                            menu:
                                "YOU’RE OVERTHINKING":
                                    k "Is everything okay, [user_name]?"
                                "ESCAPE NOW":
                                    k "Is everything okay, [user_name]?"

                "EVERYTHING WILL BE OKAY":
                    menu:
                        "YOU NEED TO LEAVE":
                            menu:
                                "YOU’RE OVERTHINKING":
                                    k "Is everything okay, [user_name]?"
                                "ESCAPE NOW":
                                    k "Is everything okay, [user_name]?"

                        "YOU NEED TO LEAVE":
                            menu:
                                "YOU’RE OVERTHINKING":
                                    k "Is everything okay, [user_name]?"
                                "ESCAPE NOW":
                                    k "Is everything okay, [user_name]?"

    k "I came to find you because you were taking a while."
    user_name "..."
    user_name "{i}I feel paralyzed.{/i}"
    k "[user_name]? You're worrying me. Please talk to me, baby."

    # ART_FRAME: Frame pans to kevin. He looks worried.

    user_name "Yeah! Everything is fine. It just took me a second to find\
    everything, but I found ‘em!"
    k "Are you sure? You look pale."
    user_name "Mhmm! I’m okay, Kevvie."
    user_name "I was just a little fatigued from the drive. I’m ready now, though."
    user_name "Let’s go!"

    # ART_FRAME: Frame pans to kevin. He has a warm smile on his face.

    k "Okay!"

    scene black

    jump after_ducees

label after_ducees:

    ##########
    # Part 3 #
    ##########

    # ART_FRAME: Back to the normal car pov.

    k "Only an hour and a half left!"
    user_name "Oh, finally..."
    user_name "{i}I need to get out of here as fast as possible.{/i}"
    user_name "{i}I need to call the police.{/i}"
    user_name "{i}But there’s no reception.{/i}"
    user_name "..."

    menu:
        "JUMP OUT OF THE CAR":
            user_name "{i}He's driving at 65 mph.{/i}"
            menu:
                "DO IT ANYWAY":
                    # ART_FRAME: Zooms in on the passenger side door.
                    user_name "{i}Please get me out of here.{/i}"
                    user_name "{i}PLEASE{/i}"
                    k "Baby, what are you doing?"

                    scene black

                    user_name "Aghuhhh..."
                    user_name "Arghh."
                    user_name "hnn..."
                    user_name "{i}It hurts...{/i}"
                    user_name "..."
                    user_name "..."
                    user_name "..."
                    "..."

                    return

        "No.":
            menu:
                "DO IT ANYWAY":
                    # ART_FRAME: Zooms in on the passenger side door.
                    user_name "{i}Please get me out of here.{/i}"
                    user_name "{i}PLEASE{/i}"
                    k "Baby, what are you doing?"

                    scene black

                    user_name "Aghuhhh..."
                    user_name "Arghh."
                    user_name "hnn..."
                    user_name "{i}It hurts...{/i}"
                    user_name "..."
                    user_name "..."
                    user_name "..."
                    "..."

                    return

                "NO. BE PATIENT.":
                    jump patience

        "BE PATIENT.":
            jump patience

label patience:
    user_name "{i}I need to distract myself.{/i}"
    user_name "{i}Right now.{/i}"
    user_name "{i}I can’t look suspicious.{/i}"
    user_name "{i}Okay.{/i}"
    user_name "{i}Okay.{/i}"
    user_name "{i}Deep breath in. Deep breath out.{/i}"
    user_name "..."
    user_name "..."

    if "Journal" in character_choices:
        user_name "{i}I just need to get lost in a drawing.{/i}"
        scene black
        user_name "..."

        # ART_FRAME: close up of a drawing in the notebook with the fountain pen.

        user_name "I miss drawing."

    elif "Polaroid" in character_choices:
        user_name "{i}I don’t think I can take any pictures right now, but at\
        least I bought some old polaroids.{/i}"
        scene black
        user_name "..."

        # ART_FRAME: close up of a polaroid with Kevin and the MC.

        user_name "{i}I miss this.{/i}"

    elif "Candy" in character_choices:
        user_name "{i}A couple gummies and a candy cane should do it.{/i}"
        scene black
        # ART_FRAME: zoom in on a bag of candy and a pointy candy cane.

        user_name "Hmm... pointy!"
        user_name "God, I love candy."

    k "Whatcha doing there baby?"
    user_name "Oh..."
    user_name "I'm just distracting myself."

    # ART_FRAME: normal car POV

    user_name "{i}Shit. I shouldn't have said that.{/i}"
    k "You know, I’m trying to distract myself too."
    k "But it’s kinda hard when you’re driving, haha. Don’t want to crash, you know?"
    user_name "{i}Why is he trying to distract himself?{/i}"
    user_name "Why are you trying to distract yourself?"
    k "You know. It’s what I’ve been talking about this whole trip pretty much."
    user_name "Work?"
    k "Yep."
    k "Just thinking about how crazy it was driving me. No pun intended."
    k "Just doing the same routine on autopilot was driving me insane."
    k "But I just remembered what I'm doing it for."
    user_name "What are you doing it for?"
    k "Well... I don't mean to sound cheesy..."
    k "But I'm doing it for you."
    k "For us really."
    k "I just can't wait to become stable. To finish the project and just move\
    on with life. I'm sorry that I haven’t been spending time with you."
    k "Genuinely."
    user_name "..."
    k "I really love you, you know?"
    user_name "{i}Fuck.{/i}"
    user_name "{i}Why does he always do this to me?{/i}"
    user_name "{i}I don’t know how to feel again.{/i}"
    user_name "{i}Fuck.{/i}"
    user_name "{i}I don’t even cuss.{/i}"
    user_name "{i}What’s happening to me?{/i}"
    user_name "{i}...I need to think straight.{/i}"

    menu:
        "I love you too.":
            user_name "{i}It’s the only thing that I can think of in my head.{/i}"
            user_name "I love you, too."

    k "I’m so happy to hear that. I was so afraid that you’ve been mad at me this\
    whole trip. Almost as if your feelings have changed."

    # ART_FRAME: Close up of kevin's hand on MC’s thigh

    k "You know, in an odd way, this new you reminds me of my client."
    user_name "Kayla?"
    k "Yeah. You both are very assertive. Very accusatory. Feisty even."
    k "Well you’re starting to act like how she did."
    user_name "{i}Wait.{/i}"
    user_name "{i}Wait.{/i}"
    user_name "{i}Wait.{/i}"
    user_name "{i}Fuck.{/i}"

    # ART_FRAME: shot of kevin. His hand is still extended to the MC’s thigh.
    # He has an ominous look on his face.

    jump gas_station
