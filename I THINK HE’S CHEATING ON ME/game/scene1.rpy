############################################
# Beginning Scene [Exposition]
#
# This file is used to prompt the user to
# input the character name, and also will
# conduct the blind date scene at the
# restaurant. Some of the options the player
# will choice might affect the choices
# that'll show up in the future.
############################################

label start:

    # Character Input; background is intentionally black
    $ character_choices = []
    default user_name = Character("[user_name]", who_color="#ffffff")
    default k = Character("Kevin Yang", who_color="#cc3516")
    define j = Character("Jessie", who_color="#6930b0")

    scene black # shows black background
    "..."
    "{i}God, where is my pink beanie...{/i}"
    "{i}Or should I wear my black one...?{/i}"
    "..."
    "{i}Found them!{/i}"
    # add scene of main_character holding up her pants and shorts
    "{i}Well, pink is my favorite color.. so I should probably go with that...{/i}"
    "{i}But black is Kevin’s favorite!  ♥{/i}"

    # audio cue
    # new art frame (new scene)
    "Hm?"
    # new art frame (new scene)
    # new art frame (new scene)
    # new art frame (new scene)
    "Oh hey Jessie!"
    # new art frame (new scene)
    j "Hey love. Whatcha up to?"
    "Just packin’ for tomorrow! Can’t decide what beanie to bring though."
    j "Hm? What do you mean?"
    # new art frame (new scene)
    "Well you see...pink is my favorite color, so the obvious choice would be\
    to bring my pink beanie. Plus it has this super cute yā kitty patch on the\
    bottom that would go with almost all of the outfits that I have planned."
    "But you know on the other hand, Kevin loves the color black. But I don't \
    think the black one is as cute. I mean it has nothing on it other than the \
    Mike logo and i'm not even a huge fan of mike. I like adid--"
    # new art frame (new scene)
    j "Girl, Please. No way you’re gonna let your boyfriend stop you from bringing your favorite beanie of all things."
    j "Who cares what Kevin thinks!"
    "{b}I{/b} do! I want to look good for him!"
    j "..."
    j "I think you should take the pink one. You said it yourself. It’s {b}your{/b} favorite one."
    "But..."
    j "Here’s an idea, take both. You can decide for yourself when you get there.\
    It shouldn’t take up any luggage space and better yet Kevin can help you choose if you so please."
    "Oh yeah. That’s actually a good idea. {i}Why didn’t I just think of that...{/i}"

    # new art frame (new scene)
    j "Anyway, where are you guys going again?"
    "I forgot the name, but it's some ski resort in Aspen!"
    j "Oh man, that’s like a 3 hour drive from here."
    "Yep!"
    # new art frame (new scene)
    "EEEE I’m honestly so excited Jessie!!! I haven’t gotten to spend time with \
    Kevin like this in so long because of his job. It’s so time consuming and he’s been so tired lately"
    j "Or so he says."
    # new art frame (new scene)
    "What is that supposed to mean?"
    j "I don’t know love. Do you really think he’s that busy doing work? Like\
    do you know anyone else that works until 1 am everyday at the office including\
    the damn weekends?"
    j "Not to mention he has been flaking on you last minute lately and barely answers your texts anymore"
    "Well he is a whole software engineer. Seems like some intense position. He’s probably just coding some huge project!"
    j "Something still feels off. Like he could definitely be doing something else..."
    "...He’s just a hard worker."
    j "Okay, okay, fine. Sorry. I didn’t mean to make assumptions. I just want \
    to make sure that he’s not messing with you or something."
    "Hey. He’s so much better than you think, you know? It’s only been like this for a couple weeks."
    j "..."
    "I know it’s a little weird that he’s kinda off the grid right now. \
    But I know he would never lie to me."

    # new art frame (new scene) [first date]
    "{i}Kevin... It has only been around 3 months, but he’s genuinely \
    one of the sweetest people I have ever met.{/i}"
    "...and funny too"
    # new art frame (new scene) [first date]

    # user input
    k "So beautiful, how do you pronounce your name?"

    python:
        user_name = renpy.input("My name is ...", length=32)
        user_name.strip()

        if not user_name:
            user_name = "6ix9ine"

    menu user_input:
        k "[user_name]?"

        "Mhm!":
            k "Sounds beautiful. What does it mean?"
        "No, no, actually it's...":
            $ user_name = renpy.input("No, no, actually it's...", length=32)
            $ user_name.strip()
            jump user_input


    $ name_meaning = renpy.input("{i}[user_name] means...{/i}")
    $ name_meaning.strip()
    k "[name_meaning] huh?"
    k "That's so cool!"
    k "Kevin means uhh..."
    k "Sexy and Handsome!"
    user_name "Is that so..."
    # new emotion from kevin
    k "No really, that’s what it means!"
    user_name "..."
    k "...hey [user_name]! Check this out!"
    # new art frame (new scene) [first date]
    user_name "{i}Or maybe he’s just stupid. But I love him anyways.{/i}"
    # new art frame (new scene) [first date]
    user_name "..."
    # new art frame (new scene) [first date]
    k "What the hell-"
    # new art frame (new scene) [first date]
    user_name "Hehe! ♥"

    # new art frame (new scene)
    user_name "I mean he’s taking me on this whole trip just to apologize to me!"
    j "I guess. Just be careful, love."
    j "..."
    j "I’ll leave you to it. See ya in the morning."
    # new art frame (new scene)
    user_name "'night Jessie!"
    j "Goodnight."

    user_name "..."
    user_name "{i}Man, what’s her deal? She hasn’t even properly met him yet and\
    she’s acting like he’s some weird sneaky b-word.{/i}"
    user_name "{i}She’s the weird sneaky b-word here!{/i}"
    user_name "...{i}Or maybe she’s right. What if he is doing something weird?{/i}"
    user_name "{i}...Nah, he wouldn’t lie to me.{/i}"
    user_name "..."

    # overthinking options
    menu overthinking:
        user_name "{i}Jessie is never wrong though! What if he really is up to \
        something weird? What if he’s selling drugs or something?{/i}"

        "Nah. You’re overthinking it.":
            user_name "No.. that makes no sense. He wouldn’t do that. She doesn’t know him like I do."
        "He has to be.":
            $ character_choices.append("overthinking option 2")
            user_name "I mean why else would he stay out so late right? He’s \
            probably talking to all of his other clients. Not his project clients \
            but his drug clients. Or both."
            user_name "Maybe that’s why his snap score increases at night even \
            when he leaves me on delivered!"

    # overthinking continued
    menu overthinking_cont:
        user_name "{i}Or what if he’s just saying he’s working all the time so \
        he doesn’t have to talk to me?{/i}"

        "You're wrong." if "overthinking option 2" in character_choices:
            user_name "{i}That’s stupid to think. I’m his girlfriend for god’s \
            sake.{/i}"
            user_name "{i}He loves me... right?{/i}"
            "..."
            user_name "{i}Of course he does. He tells me so everyday. This trip \
            is just more proof of that fact.{/i}"

        "You're wrong." if "overthinking option 2" not in character_choices:
            user_name "{i}That’s stupid to think. I’m his girlfriend for god’s \
            sake.{/i}"
            user_name "{i}He loves me... right?{/i}"
            "..."
            user_name "{i}What if he doesn’t.{/i}"
            user_name "..."
            user_name "I don't know... I don't know."
            "..."

        "Of course he’d avoid you.":
            user_name "{i}He’s definitely avoiding me.{/i}"
            user_name "{i}He’s probably bored of me.{/i}"
            user_name "{i}He’s probably talking to someone else.{/i}"
            "..."


    user_name "What if he’s cheating on me?"
    user_name "..."
    user_name "I don’t want to think about that."
    "............................................."
    user_name "{i}I’m done packing anyways.{/i}"
    user_name "{i}I’ll just go to bed.{/i}"

    scene black
    user_name "{i}Ahh! I'm so tired{/i}"
    user_name "{i}Need to check my phone though.{/i}"
    # new art frame (phone scene)
    user_name "{i}Kevin!!!♥♥♥{/i}"

    # texting Kevin
    menu texting_options:
        user_name "{i}EEE What should I tell him!{/i}"
        "I love you!":
            # scene bg
        "Sounds good!":
            # scene bg

    user_name "{i}Huh. He said “gn” instead of “goodnight”.{/i}"
    user_name "{i}Is he mad about something? What if he’s mad at me???{/i}"
    user_name "{i}Okay, I'm seriously overreacting. I’m sleeping.{/i}"
    scene black

    jump diner
