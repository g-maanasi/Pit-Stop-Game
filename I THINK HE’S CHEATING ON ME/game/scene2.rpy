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

    # AUDIO CUE: phone alarm
    # ART_FRAME: BLACK_SCREEN

    user_name "{i}...mmmhh{/i}"
    user_name "{i}It’s already 5:30...{/i}"
    user_name "{i}I have to get up, though. Kevin will be here in thirty minutes!{/i}"
    user_name "{i}Let’s see if I have any last minute packing to do.{/i}"

    # ART_FRAME: We are in MC’s room. There is a downward view of her suitcase
    # on the bed. It is open.

    user_name "{i}Looks like I have room for one more thing.{/i}"
    user_name "{i}Well, I have my mini doodle {b}journal{/b} and the best fountain pen\
    ever. It would be nice to have if I get bored.{/i}"
    user_name "{i}I’ve also got a baggie of my {b}favorite candy{/b}! It’s got chocolates\
    and sour strings and candy canes and gummy bears! ♥{/i}"
    user_name "{i}But I'd love to bring my {b}polaroid{/b}. Kev and I could take some\
    really cute pictures!{/i}"
    user_name "..."
    user_name "{i}Ah, I don't know. What should I bring{/i}"

    menu:
        "Journal":
            user_name "{i}Okay... journal it is!{/i}"
            $ character_choices.append("Journal")
        "Polaroid":
            user_name "{i}Okay... polaroid it is!{/i}"
            $ character_choices.append("Polariod")
        "Bag of Candy":
            user_name "{i}Okay... candy it is!{/i}"
            $ character_choices.append("Candy")

    # ART_FRAME: We are in MC’s room. There is a downward view of her suitcase
    # on the bed. The suitcase is now closed.

    user_name "{i}Yay! All done!{/i}"
    user_name "{i}Now time to wait for Kevin. He should be here in around ten minutes.{/i}"
    user_name "{i}Hmm... I feel like watching something.{/i}"

    # ART_FRAME: We can see MC’s phone at a horizontal view. She is watching a
    # video about a monkey.

    user_name "{i}Hehe! It’s too cute.{/i}"

    # ART_FRAME: We can see MC’s phone at a horizontal view. She is watching a\
    #video about a monkey. The monkey moves in the frame.

    user_name "{i}Aww! Haha!{/i}"

    # ART_FRAME: We can see MC’s phone at a horizontal view. She is watching
    # a video about a monkey. The screen goes black to indicate that the video is over.

    user_name "{i}Oh looks like it’s over.{/i}"
    user_name "{i}Shoot, that was a 30 minute video!{/i}"
    user_name "{i}What time is it...{/i}"

    # ART_FRAME: We can see MC’s phone at a vertical view. It is on her home
    # screen and it says that it is 6:25.

    user_name "{i}Huh? Kevin should have been here 20 minutes ago...{/i}"
    user_name "{i}Where is he?{/i}"
    user_name "{i}What if he’s flaking on me again?{/i}"
    user_name "{i}Ah, maybe Jessie is right about him.{/i}"
    user_name "{i}No, no. It’s probably nothing. I’ll just text him.{/i}"

    # ART_FRAME: We can see MC’s phone at a vertical view. It is on her home
    # screen and it says that it is 6:25. There is a text from kevin that says “hey im here”.

    user_name "{i}Oh. Well, nevermind then.{/i}"

    scene black
    # AUDIO CUE: sound of a car engine or sound of a car door closing.
    # ART_FRAME: Kevin’s car. 1999 Chevy Suburban. The car is manual.
    # Back View. Trunk is open. Close up. Kevin and MC can be seen in the frame.

    k "Hey, baby. I missed you so much you don’t even know."
    user_name "I missed you so much too!! I’m so excited!!!"
    user_name "But why were you almost thirty minutes late? Everything okay?"
    k "Oh yeah, sorry about that baby."
    k "Everything’s fine, don't worry. Just woke up a bit late because\
    I was up all night, that’s all."
    k "You all set, babe?"
    user_name "What the heck was he doing all night before a road trip?"
    user_name "..."
    user_name "Mhm! Just gotta put my suitcase in."

    # ART_FRAME: the trunk of his car. She notices a falsie in the corner of the car.

    user_name "Are those... eyelashes?? Or a spider???"
    k "Everything okay?"
    user_name "Uhh... yeah! It’s just a little heavy, but I got it!"
    user_name "Ah, whatever. It’s probably just a bunched up piece of string or something."
    k "Alrighty!"

    # ART_FRAME: returns to the frame before the last

    user_name "..."
    user_name "Umm... Kevvie? Just curious again. Why were you up all night?"
    k "You know, the usual. Work. Why?"
    user_name "Oh, okay! Nothing! Just wanted to know!"
    user_name "{i}Work right before Christmas...{/i}"
    k "Alrighty then."

    # ART_FRAME: Kevin’s car. 1999 Chevy Suburban. Back View. Trunk is open.
    # Close up. Kevin and MC can be seen in the frame. Kevin has a big smile.

    k "Are you really ready for the best road trip of your entire life [user_name]???"
    k "We are about to have the time of our lives!"

    # ART_FRAME: Kevin’s car. 1999 Chevy Suburban. Back View. Trunk is open.
    # Close up. Kevin and MC can be seen in the frame. Kevin and MC have a big smile.

    k "Hehe! Of course! ♥"
    user_name "{i}Maybe I'm just thinking too hard.{/i}"
    k "Hell yeah! Let’s go!"
    user_name "Hehe!"
    user_name "{i}I still don’t think Jessie is up– I'll just text her goodbye.{/i}"

    ##########
    # Part 2 #
    ##########

    scene black
    # ART_FRAME: first POV of the inside of a car from the passenger’s perspective.
    # You can only see Kevin’s hand on the clutch.

    user_name "..."
    k "So baby, what ya been up to?"
    user_name "Oh you know, waiting for you."
    k "Yeah, sorry! I was a teensy bit late."
    user_name "As usual..."
    k "Baby... it was only thirty minutes. I didn’t know you cared so much."
    user_name "..."
    k "Really baby, I’m sorry."
    user_name "{i}I don’t know how to feel.{/i}"

    menu:
        "It's okay.":
            user_name "{i}I guess it’s okay. He said it himself, he was just busy\
            with work. Plus he’s apologizing!{/i}"
            user_name "{i}It’s okay, Kevvie. I understand.{/i}"

            jump nonconfrontational_path

        "You're always late!":
            user_name "{i}No. He needs to hear how I feel.{/i}"
            user_name "{i}You weren’t a {b}teensy{/b} bit late! And anyway I’m\
            not only talking about this time. You haven’t properly spoken to me\
            in what feels like forever.{/i}"
            user_name "You barely return my calls, you’re so dry when you text me,\
            and sometimes you cancel last minute when we make plans."
            user_name "...It feels like you aren’t even there anymore."
            user_name "Like who knows what you’re {b}actually{/b} doing!"
            $ character_choices.append("Confrontational")

            jump confrontational_path

label nonconfrontational_path:

    k "...You do?"
    user_name "Of course! I’m sorry. I’ve just missed you a lot."
    user_name "But I gotta remember you’re just working really hard."
    k "It’s okay, baby. Basically, I’ve got this huge project that I’ve had to\
    make from scratch for an incredibly important client, and they got me working overtime."
    k "Don’t worry, though. I’m just about done with it."
    user_name "{i}Take that, Jessie! I knew that he had some project.{/i}"
    user_name "{i}I really thought he was a darn drug dealer...{/i}"
    user_name "I’m guessing that’s why you stayed up last night? To finish it up?"
    k "Hm? What?"
    user_name "You said earlier that you stayed up all night. Was it because of this project?"
    k "..."
    k "Oh yeah! Yeah, I was working on it. Sorry, my mind is in such a\
    doozy I didn’t understand what you were saying."
    user_name "{i}That was weird. What is there not to understand?{/i}"
    user_name "{i}Whatever. I just want things to go back to the way it was.{/i}"
    user_name "Does that mean that you’ll be free soon?"
    k "Damn right!"
    k "Then you'll be {b}all mine{/b}, baby."
    user_name "Hehe! ♥"
    k "..."
    user_name "..."
    user_name "{i}Hehe! ♥{/i}"
    user_name "{i}I honestly didn’t get much sleep last night either.{/i}"
    user_name "{i}Doesn’t hurt to take a lil nap.{/i}"

    jump diner

label confrontational_path:

    k "Okay I know, I know! I’m sorry! That’s why I’m taking you on this damn\
    trip in the first place!"
    user_name "..."
    k "You really don’t seem to understand, [user_name]! I’ve been working so fucking much!"
    k "All day and all night I've been on this damn project! Three god\
    damn weekends in a row I’ve had to talk to my client for hours and hours..."
    k "Unlike you I have a really difficult job and I absolutely do not have time\
    to be sitting around."
    k "And what exactly are you suggesting here? You know EXACTLY what I’m doing,\
    [user_name]!"
    user_name "I..."
    user_name "{i}He’s never been so defensive with me.{/i}"
    user_name "{i}I feel bad.{/i}"
    user_name "{i}I feel so bad.{/i}"
    user_name "{i}I don’t want to talk anymore.{/i}"
    user_name "{i}What’s wrong with me...{/i}"
    user_name "I’m sorry."
    user_name "I’m so sorry."
    user_name "I didn’t mean it like that. I’m sorry."
    k "..."
    k "It’s okay, baby. I didn’t mean to lash out at you either."
    k "Let’s just take it easy, okay?"
    user_name "..."
    k "..."
    user_name "{i}I don’t like this.{/i}"
    user_name "{i}There’s too much tension.{/i}"
    user_name "{i}I hate this.{/i}"
    user_name "{i}I just want this to go away.{/i}"
    user_name "{i}I’ll just sleep. Maybe when I wake up things will be better.{/i}"
    user_name "..."

    jump diner

label diner:

    scene black
    # ART_FRAME: Back to car POV. his phone is in the cupholder

    user_name "{i}Mmm...{/i}"
    user_name "{i}That was a nice dream...{/i}"
    user_name "..."
    user_name "{i}Where’s Kevin?{/i}"

    # ART_FRAME: pans towards the driver’s seat. It is empty.

    user_name "{i}Where even are we?{/i}"

    # ART_FRAME: zooms in on the diner.

    user_name "...oh."
    user_name "{i}I think I'll just wait for him.{/i}"

    # ART_FRAME: back to og car POV. The phone is in the cupholder.

    user_name "{i}Hm...?{/i}"
    user_name "{i}Huh. He left his phone here.{/i}"
    user_name "{i}Hehe, I'm gonna clog up his camera roll!{/i}"

    # ART_FRAME: Kevin's phone POV. she unlocks it. There are a lot of notifications
    # on iMessage and in his calls.

    user_name "{i}...{/i}"
    user_name "{i}Lots of calls and texts.{/i}"
    user_name "{i}...Looks like someone’s popular.{/i}"
    user_name "{i}Wonder who they are.{/i}"

    default phone_choices = []
    menu:
        set phone_choices

        "Let’s check the calls.":
            # ART_FRAME: Kevin's phone POV. on the phone app. There are missed calls
            # from Client on two separate days coming to a total of 12 missed calls.
            # 3 missed calls the first day. Kevin picked up once. The next day the
            # client called 9 times.

            user_name "{i}What kind of client needs to spam call 12 times...{/i}"
            user_name "{i}He did say that they were “important”{/i}"
            user_name "{i}Interesting. The latest calls were two days ago.{/i}"

        "Let’s check the messages.":

            user_name "{i}Wonder who sent these 43 messages...{/i}"

            # ART_FRAME: Kevin's phone POV. on the messages menu.

            user_name "{i}Client?{/i}"
            user_name "{i}I’m gonna scroll up a bit too.{/i}"

            # ART_FRAME: Kevin's phone POV. on the actual messages app.

            user_name "{i}Kayla, huh.{/i}"
            user_name "{i}Why doesn’t he just use her actual name instead of “client”.{/i}"
            user_name "..."

    user_name "{i}Is {b}she{/b} what he has been doing for weeks?{/i}"

    menu:
        "You’re overreacting.":
            user_name "{i}No. That’s actually ridiculous. I need to stop overreacting.{/i}"
            user_name "{i}This is all driving me insane.{/i}"
            user_name "{i}But what about the missed messages and calls?{/i}"

            menu:
                "There has to be something going on.":
                    user_name "{i}I don’t know why...{/i}"
                    user_name "{i}It just doesn’t feel right.{/i}"
                    user_name "{i}Something isn’t right.{/i}"

        "Why else would he hide her name?":
            user_name "{i}Why else would he change her name?{/i}"
            user_name "{i}Why was she trying to tell him?{/i}"
            user_name "{i}Why were there so many missed calls?{/i}"
            user_name "{i}What is he hiding?{/i}"
            user_name "{i}This is driving me insane.{/i}"

    user_name "..."
    user_name "{i}Frick!{/i}"
    user_name "{i}Kevin is coming back.{/i}"

    # ART_FRAME: Back to original car POV. His phone is in the cupholder.

    user_name "{i}...Hi Kevvie!!{/i}"

    # ART_FRAME: Back to original car POV. His hand is on the clutch. His phone
    # is in the cupholder.

    k "Hey, baby! I see that you’re finally up!"
    k "Sorry you were probably confused when you woke up. I just went to the bathroom."
    k "Andddd I brought you this!"

    # ART_FRAME: He is holding out a milkshake.

    user_name "Umm... thank you so much!!"
    k "Mhmm!"
    k "Ah, so that’s where my phone went too! Thought I lost that thing."
    k "Okay, on we go!"
    user_name "..."
    k "Everything okay? You seem a little shaken up. Haha, get it? Shaken up!"
    user_name "Haha... yeah!"
    user_name "I just woke up so I'm just a little disoriented is all!"
    k "Aw, okay! Hopefully the shake will sweeten up your mood! Haha!"
    user_name "{b}Yeah...{/b}"

    jump car_ride2
