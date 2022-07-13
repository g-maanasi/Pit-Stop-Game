############################################
# Beginning Scene
#
# This file is used to prompt the user to
# input the character name, and also will
# conduct the blind date scene at the
# restaurant and the characters packing up
# to go on the road trip.
############################################

label start:

    # Character Input; background is intentionally black
    default character_choices = []
    default user_name = Character("[user_name]", who_color="#ffffff")
    default k = Character("Kevin Yang", who_color="#cc3516")
    define j = Character("Jessie", who_color="#6930b0")

    scene black # shows black background
    "..."
    "{i}God where are my pants...{/i}"
    "..."
    "{i}Or should I wear shorts...?{/i}"
    "..."
    # add scene of main_character holding up her pants and shorts
    "{i}Well it's San Antonio so it's bound to be hot as hell...{/i}"
    "{i}But these are Kevin’s favorite pants! ♥{/i}"

    # audio cue
    # new art frame (new scene)
    "Hm?"
    # new art frame (new scene)
    # new art frame (new scene)
    # new art frame (new scene)
    "Oh hey Jessie!"
    # new art frame (new scene)
    j "Hey love. Whatcha up to?"
    "Just packin’ for tomorrow! Can’t decide what pants to bring though."
    j "Hm? What do you mean?"
    # new art frame (new scene)
    "Well.. it’s gonna be hot as balls outside so I should definitely \
    wear shorts or else i’m probably gonna eventually get sick but like I don’t \
    want my thighs to chafe and I know Kevin really loves these pants and I want \
    to make sure he’s extra happy so maybe if I wear the pants it’ll be a better choice."
    "But at the same time I should be more focused on my own comfort \
    or else I may act uncomfortable and that’ll probably be even worse than \
    wearing the pants. But at the same time—"
    # new art frame (new scene)
    j "Girl. Please for the love of god stop overthinking it."
    j "Who cares what Kevin thinks!"
    "{b}I{/b} do! I want to look good for him!"
    j "..."
    j "Just take the shorts. You said it yourself. It’s definitely going to be \
    at least 100 degrees out there. And it will probably feel like 150…"
    "..."
    j "Here’s an idea, take both. You can decide for yourself when you get there. \
    Better yet Kevin can help you choose if you so please."
    "Oh yeah. That’s actually a good idea. {i}Why didn’t I just think of that...{/i}"

    # new art frame (new scene)
    j "Anyway, where are you guys going again?"
    "I forget the name but it’s some resort in San Antonio!"
    # new art frame (new scene)
    "EEEE I’m so excited Jessie!!! I haven’t gotten to spend time with \
    Kevin like this in so long because of his job."
    j "Or so he says."
    # new art frame (new scene)
    "What is that supposed to mean?"
    j "I don’t know love. Do you know anyone else around town who works until \
    1 am everyday including the damn weekends?"
    j "Not to mention he flakes on you last minute and barely answers your texts anymore."
    "Well he is some software-engineer-programmer guy. He’s probably just coding some huge project."
    j "Something still feels off."
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
        redo_name = True

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
    user_name "{i}What the hell is her deal? She hasn’t even met him yet and \
    she’s acting like he’s a bitch or something.{/i}"
    user_name "{i}She’s really the bitch here.{/i}"
    user_name "...{i}Or maybe she’s right.{/i}"
    user_name "{i}...No. He wouldn’t lie to me.{/i}"
    user_name "..."

    # overthinking options
    menu overthinking:
        user_name "{i}Jessie is never wrong though! What if he really is up to \
        something weird? What if he’s selling drugs or something?{/i}"

        "Nah. You’re overthinking it.":
            $ character_choices.append("overthinking option 1")
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
            $ character_choices.append("overthinking_cont option 1.1")
            user_name "{i}That’s stupid to think. I’m his girlfriend for god’s \
            sake.{/i}"
            user_name "{i}He loves me... right?{/i}"
            "..."
            user_name "{i}Of course he does. He tells me so everyday. This trip \
            is just more proof of that fact.{/i}"

        "You're wrong." if "overthinking option 2" not in character_choices:
            $ character_choices.append("overthinking_cont option 1.2")
            user_name "{i}That’s stupid to think. I’m his girlfriend for god’s \
            sake.{/i}"
            user_name "{i}He loves me... right?{/i}"
            "..."
            user_name "{i}What if he doesn’t.{/i}"
            user_name "..."
            user_name "I don't know... I don't know."
            "..."

        "Of course he’d avoid you.":
            $ character_choices.append("overthinking_cont option 2")
            user_name "{i}He’s definitely avoiding me.{/i}"
            user_name "{i}He’s probably bored of me.{/i}"
            user_name "{i}He’s probably talking to someone else.{/i}"
            "..."

        "What if he’s cheating on me?":
            $ character_choices.append("overthinking_cont option 3")
            user_name "..."
            user_name "I don’t want to think about that."

    "............................................."
    user_name "{i}I’m done packing anyways.{/i}"
    user_name "{i}I’ll just go to bed.{/i}"
