############################################
# Pit Stop #1 Scene
#
# This file encompasses the code and script
# for packing up and the diner stop scene.
# The choices made by the user can
# potentially affect their final outcome.
############################################

label car_ride1:

    ##########
    # Part 1 #
    ##########
    scene black
    user_name "{i}ugh...I’m too tired for this.{/i}"

    menu sleeping_in:
        "5 more minutes.":
            # add audio code bc there isn't anything to add...

    user_name "...mmmmh.."
    user_name "{i}Oh man...{/i}"
    user_name "{i}What time is it...5:30?????{/i}"
    user_name "{i}I have to get up, though. Kevin will be here in thirty minutes!{/i}"
    user_name "{i}Let’s see if I have any last minute packing to do.{/i}"
    # new background Scene

    menu packing:
        user_name "{i}Looks like I have room for one more thing.{/i}"
        user_name "{i}Well, I have my mini doodle journal and the best\
        fountain pen ever. It would be nice to have if I get bored.{/i}"
        user_name "{i}I’ve also got a baggie of my favorite candy! It’s got\
        chocolates and sour strings and candy canes and gummy bears! ♥{/i}"
        user_name "{i}But, the smartest thing I could do is to bring some \
        extra pads. Feel like my time of the month is coming soon{/i}"

        "Journal":
            $ character_choices.append("journal")
        "Sanitary Pads":
            $ character_choices.append("pads")
        "Candy":
            $ character_choices.append("candy")

    user_name "{i}Okay the [character_choices[1]] it is!{/i}"
    user_name "{i}Yay! All done! Now time to wait for kevin. He should be here in around ten minutes.{/i}"
    user_name "{i}Hmm.. I feel like watching something.{/i}"
    user_name "{i}Hehe! It’s too cute.{/i}"
    user_name "Aww! Haha!"
    user_name "{i}Oh looks like it’s over.{/i}"
    user_name "{i}Shoot, that was a 30 minute video! What time is it...{/i}"
    user_name "{i}Huh? Kevin should have been here 20 minutes ago... where is he?{/i}"
    user_name "{i}What if he’s flaking on me again?{/i}"
    user_name "{i}Ah, maybe Jessie is right about him.{/i}"
    user_name "{i}No, no. It’s probably nothing. I’ll just text him.{/i}"
    user_name "{i}Oh. Well, nevermind then.{/i}"
    scene black
    k "Hey, baby. I missed you so much you don’t even know."
    user_name "I missed you so much too!! But why were you almost thirty minutes late? Everything okay?"
    k "Oh yeah, sorry about that, baby. Everything’s fine, don't worry. Just woke up a bit late because I was up all night, that’s all."
    k "You all set, babe?"
    user_name "{i}What the heck was he doing all night before a road trip?{/i}"
    user_name "Mhhm! But why were you up all night?"
    k "You know, the usual. Work. Why?"
    user_name "Oh, okay! Nothing! Just wanted to know!"
    user_name "{i}Work again...{/i}"
    k "Alrighty then."
    k "Are you really ready for the best road trip of your entire life [user_name]???"
    k "We are about to have the time of our lives!"
    user_name "Hehe! Of course! ♥"
    user_name "{i}Maybe I'm just thinking too hard.{/i}"
    k "Hell yeah! Let’s go!"
    user_name "Hehe!"
    user_name "{i}I still don’t think Jessie is up– I'll just text her goodbye.{/i}"

    ##########
    # Part 2 #
    ##########
    user_name "..."
    k "So baby, what ya been up to?"
    user_name "Oh you know, waiting for you."
    k "Eh, haha! Sorry I was a bit late."
    user_name "Yeah, as usual"
    k "Baby... it was only thirty minutes. I didn’t know you cared so much. Really, I’m sorry."

    menu pondering:
        user_name "{i}I don’t know how to feel.{/i}"

        "It's okay.":
            # Pondering #1 Route
            user_name "{i}I guess it’s okay. He said it himself, he was just busy\
            with work. Plus he’s apologizing!{/i}"
            user_name "It’s okay, Kevvie. I understand."
            jump pondering1_route
        "You're always late!":
            # Pondering #2 Route
            $ character_choices.append("You're always late!")
            user_name "{i}No. He needs to hear how I feel.{/i}"
            user_name "You weren’t a teensy bit late! And anyway I’m not only\
            talking about this time. You haven’t properly spoken to me in what\
            feels like forever."
            user_name "You barely return my calls, you’re so dry when you text me,\
            and sometimes you cancel last minute when we make plans. "
            user_name "...It feels like you aren’t even there anymore."
            user_name "Like who knows what you’re {b}actually{/b} doing!"

label pondering1_route:
    k "...You do?"
    user_name "Of course! I’m sorry. I’ve just missed you a lot."
    user_name "But I gotta remember you’re just working really hard."
    k "It’s okay, baby. Basically, I’ve got this huge project that I’ve had to\
    make from scratch for an incredibly important client, and they got me working overtime."
    k "Don’t worry, though. I’m just about done with it."
    user_name "{i}Take that, Jessie! I knew that he had some project.{/i}"
    user_name "{i}I really thought he was a darn drug dealer...{/i}"
    user_name "I’m guessing that’s why you stayed up last night? To finish it up?"
    k "...hm? What?"
    user_name "You said earlier that you stayed up all night. Was it because of this project?"
    k "..."
    k "Oh yeah! Yeah, I was working on it. Sorry, my mind is in such a doozy I\
    didn’t understand what you were saying."
    user_name "{i}That was weird. What is there not to understand?{/i}"
    user_name "{i}Whatever. I just want things to go back to the way it was.{/i}"
    user_name "Does that mean that you’ll be free soon?"
    k "Damn right! Then you'll be {b}all mine{/b}, baby."
    user_name "Hehe! ♥"
    k "..."
    user_name "..."
    user_name "{i}Ah, I’m so tired. I honestly didn’t get much sleep last night either.\
    Doesn’t hurt to take a lil nap.{/i}"
