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

    menu escaping_car:

        "Unlock the car door":
            user_name "{i}It’s locked. Heh. That would’ve been too easy.{/i}"

        "Scream for help":
            user_name "{i}There’s a man outside. Maybe he’ll notice.{/i}"

            # ART_FRAME: zoom in on the windshield. You can see a man in the distance.

            user_name "H E E E L  L  L P P P P P P  M E E E E! ! ! ! ! !"

            # ART_FRAME: zoom in on the windshield. You can see a man in the
            # distance. He is now looking up.

            user_name "{i}I think it’s working!{/i}"
            user_name "H E E E L  L  L L L P P P P P P   M E E E E E! ! ! ! ! ! ! ! ! ! ! !"
            user_name "..."

            # ART_FRAME: close up of Kevin's face. He looks scary af.

            k "{b}What do you think you’re doing?{/b}"

            menu:
                "ATTACK":
                    if "Journal" in character_choices:
                        user_name "{i}{b}THE FOUNTAIN PEN...{/b}{/i}"
                    elif "Polaroid" in character_choices:
                        user_name "{i}{b}THE CAMERA...{/b}{/i}"
                    elif "Candy" in character_choices:
                        user_name "{i}{b}THE CANDY CANE...{/b}{/i}"

                    scene black

                    user_name "AHH!"

                    # ART_FRAME: kevin holding MC’s wrist

                    k "Heh."

                    return

                "DO NOTHING":
                    user_name "{i}There’s nothing I can really do.{/i}"
                    user_name "..."
                    k "Man. The one time you talk!"
                    k "But it’s okay. I have duck tape."

                    scene black

                    user_name "{i}Ugh.{/i}"
                    user_name "{i}I can't move... or talk.{/i}"
                    $ character_choices.append("Restrained")

        "Do nothing.":
            user_name "{i}I need to wait.{/i}"
            user_name "..."
            user_name "..."
            user_name "..."

    k "I’m back, baby!"
    k "Brought you some water just in case you needed any."
    user_name "..."
    k "Okkayy!"
    k "We’ve got about twenty minutes until we reach the resort!"
    k "I’m going to try to get there in ten."
    user_name "{i}What is that supposed to mean?{/i}"

    # ART_FRAME: zoom in of the speedometer at like 80 mph

    user_name "{i}Fuck fuck fuck fuck fuck.{/i}"
    user_name "{i}Fuck.{/i}"
    user_name "..."
    user_name "{i}WAIT.{/i}"

    # ART_FRAME: CLOSE UP OF MC’S FACE HORRIFIED
    "..."
    # ART_FRAME: Deer on the road.

    if "Restrained" in character_choices:
        user_name "MMMHHHHHHHHHH!!!!"
    else:
        user_name "KEVIN!"

    k "Hm?"
    k "Oh fuck."

    scene black

    user_name "..."
    user_name "Ugh."
    user_name "{i}My head.{/i}"

    if "Restrained" in character_choices:
        user_name "{i}Hey, my hands are free!{/i}"
        user_name "{i}Now I can take the tape off of my mouth.{/i}"
        user_name "..."

    user_name "{i}I should get up.{/i}"
    user_name "{i}Fuck it hurts.{/i}"
    user_name "{i}Fuck my legs.{/i}"
    user_name "..."
    user_name "{i}Holy shit.{/i}"

    # ART_FRAME: crash site. Deer is messed up too.

    user_name "{i}Kevin...{/i}"

    # ART_FRAME: Close up of kevin. He looks pretty badly injured.

    k "Augh..."
    k "..."
    k "Gugh..."
    k "{b}[user_name]{/b}"
    k "{b}It hurts.{/b}"
    user_name "..."
    user_name "{i}Why does it hurt to see him like this?{/i}"
    user_name "{i}I can’t just leave him here.{/i}"
    user_name "{i}Can I?{/i}"

    menu:
        "KILL HIM.":
            jump kill_path
        "LEAVE HIM.":
            jump escape_path


label kill_path:
    user_name "{i}{b}If I don’t, he’ll kill me first.{/b}{/i}"

    if "Candy" in character_choices:
        # ART_FRAME: Her weapon according to what she chose is raised in the drawing.
        ""
    elif "Polaroid" in character_choices:
        # ART_FRAME: Her weapon according to what she chose is raised in the drawing.
        ""
    elif "Journal" in character_choices:
        # ART_FRAME: Her weapon according to what she chose is raised in the drawing.
        ""

    user_name "{i}I have to do it.{/i}"
    user_name "..."

    menu:
        "DO IT.":
            user_name "{i}I CAN'T.{/i}"
            menu:
                "DO IT.":
                    user_name "{i}I CAN'T.{/i}"
                    menu:
                        "DO IT.":
                            user_name "{i}I CAN'T.{/i}"
                            menu:
                                "DO IT.":
                                    user_name "{i}I can.{/i}"
                                "DON'T DO IT.":
                                    user_name "{i}I CAN'T.{/i}"
                                    jump escape_path
                        "DON'T DO IT.":
                            user_name "{i}I shouldn't{/i}"
                            menu:
                                "DO IT":
                                    user_name "{i}I can.{/i}"
                                "DON'T DO IT":
                                    user_name "{i}I CAN'T.{/i}"
                                    jump escape_path

                "DO IT.":
                    user_name "{i}I CAN'T.{/i}"
                    menu:
                        "DO IT.":
                            user_name "{i}I CAN'T.{/i}"
                            menu:
                                "DO IT.":
                                    user_name "{i}I can.{/i}"
                                "DON'T DO IT.":
                                    user_name "{i}I CAN'T.{/i}"
                                    jump escape_path
                        "DON'T DO IT.":
                            user_name "{i}I shouldn't{/i}"
                            menu:
                                "DO IT":
                                    user_name "{i}I can.{/i}"
                                "DON'T DO IT":
                                    user_name "{i}I CAN'T.{/i}"
                                    jump escape_path
        "DON'T DO IT":
            user_name "{i}I shouldn't{/i}"
            menu:
                "DO IT":
                    user_name "{i}I CAN'T.{/i}"
                    menu:
                        "DO IT":
                            user_name "{i}I CAN'T.{/i}"
                            menu:
                                "DO IT":
                                    user_name "{i}I can.{/i}"
                                "DON'T DO IT":
                                    user_name "{i}I CAN'T.{/i}"
                                    jump escape_path
                        "DON'T DO IT.":
                            user_name "{i}I shouldn't{/i}"
                            menu:
                                "DO IT":
                                    user_name "{i}I can.{/i}"
                                "DON'T DO IT":
                                    user_name "{i}I CAN'T.{/i}"
                                    jump escape_path
                "DON'T DO IT":
                    user_name "{i}I shouldn't{/i}"
                    menu:
                        "DON'T DO IT":
                            user_name "{i}I shouldn't{/i}"
                            menu:
                                "DO IT":
                                    user_name "{i}I can.{/i}"
                                "DON'T DO IT":
                                    user_name "{i}I CAN'T.{/i}"
                                    jump escape_path

    scene black
    # ART_FRAME: Kevin is lifeless.

    user_name "{i}Oh my god.{/i}"
    user_name "{i}I did it.{/i}"
    user_name "{i}I did it.{/i}"

    # ART_FRAME: MC crying like crazy

    user_name "{i}I’m so sorry.{/i}"
    user_name "{i}Fuck.{/i}"
    user_name "{i}I’m so sorry Kevin.{/i}"
    user_name "{i}I’m so sorry.{/i}"
    user_name "..."
    user_name "{i}I need to leave.{/i}"
    user_name "{i}I don't know where to go.{/i}"
    user_name "{i}I can't believe I did it.{/i}"
    user_name "{i}I'll just keep walking.{/i}"
    user_name "{i}I'm sorry Kevin.{/i}"
    user_name "{i}I’m so sorry.{/i}"
    user_name "{i}I love you.{/i}"
    user_name "{i}Please forgive me.{/i}"
    user_name "{i}Please forgive me.{/i}"

    # ART_FRAME: Mc looking crazy walking down the road.
    ""

    return

label escape_path:
    user_name "{i}I don’t want to kill him.{/i}"
    user_name "{i}I can’t kill him.{/i}"
    user_name "..."
    user_name "{i}But I can leave him.{/i}"

    # ART_FRAME: MC’s phone calling jessie.

    user_name "..."
    user_name "H-Hello?"
    user_name "Jessie?"
    j "Hey!"
    j "How's everything?"
    user_name "Everything's okay."
    user_name "I was wondering if you could pick me up from the resort? Or call\
    an Uber for me?"
    j "Why? Is everything okay?"
    user_name "Yeah, I'll explain when I get home."
    user_name "..."

    scene black

    user_name "{i}I also called the police right after.{/i}"
    user_name "{i}I didn’t know where to go, so I followed the road down to the resort.{/i}"
    user_name "{i}Just as the ad said, it was still practically a construction site.{/i}"
    user_name "{i}I don’t know what Kevin was planning to do with me.{/i}"
    user_name "{i}I wonder if I didn’t know what happened to Kayla, things would\
    have gone as normal or if he planned something all along.{/i}"
    user_name "{i}It doesn’t matter, though.{/i}"
    user_name "{i}Kevin’s in custody and I’m glad to be at home.{/i}"

    return
