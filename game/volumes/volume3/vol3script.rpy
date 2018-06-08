





define sky = Character("SKYLLA", color='#FFFFFF', image="skylla", window_background="gui/textbox_bronze.png", who_outlines=[ (4, "#bb6405") ],)
define bro = Character("BRONYA", color='#FFFFFF', image="bronya", window_background="gui/textbox_jade.png", who_outlines=[ (4, "#0aa85b") ],)

image bronya angry = "volumes/volume3/images/bronya_angry.png"
image bronya duty = "volumes/volume3/images/bronya_duty.png"
image bronya happy = "volumes/volume3/images/bronya_happy.png"
image bronya mom = "volumes/volume3/images/bronya_motherly.png"
image bronya panic = "volumes/volume3/images/bronya_panic.png"
image bronya talk = "volumes/volume3/images/bronya_talk.png"
image bronya um = "volumes/volume3/images/bronya_umm.png"
image bronya worried = "volumes/volume3/images/bronya_worried.png"

image skylla anger = "volumes/volume3/images/skylla_anger.png"
image skylla concern = "volumes/volume3/images/skylla_concern.png"
image skylla depressed = "volumes/volume3/images/skylla_depressed.png"
image skylla distress = "volumes/volume3/images/skylla_distress.png"
image skylla happy = "volumes/volume3/images/skylla_happy.png"
image skylla kickass = "volumes/volume3/images/skylla_kickass.png"
image skylla numb = "volumes/volume3/images/skylla_numb.png"
image skylla numb2 = "volumes/volume3/images/skylla_numb2.png"
image skylla stand = "volumes/volume3/images/skylla_stand.png"
image skylla talk = "volumes/volume3/images/skylla_talk.png"
image skylla upset = "volumes/volume3/images/skylla_upset.png"

image lady = Image("volumes/volume3/images/lady.png")

image gameover skylla1 = "volumes/volume3/images/skylla_lose1.png"
image gameover skylla2 = "volumes/volume3/images/skylla_lose2.png"
image gameover bronya1 = "volumes/volume3/images/bronya_lose1.png"
image gameover bronya2 = "volumes/volume3/images/bronya_lose2.png"

image win skylla = "volumes/volume3/images/skylla_victory.png"
image win bronya = "volumes/volume3/images/bronya_victory.png"

image sun 1 = "volumes/volume3/images/sun.png"
image sun 2 = "volumes/volume3/images/sun2.png"

image bison = Image("volumes/volume3/images/bisonlusus.png", ypos = 738)
image bgbison = "volumes/volume3/images/bgbison.png"

image sunclassic:

    "volumes/volume3/images/sunbase.png"
    pause 0.75
    "volumes/volume3/images/sunhalfleft.png"
    pause 0.75
    "volumes/volume3/images/sunleft.png"
    pause 0.75
    "volumes/volume3/images/sunhalfleft.png"
    pause 0.75
    "volumes/volume3/images/sunbase.png"
    pause 0.75
    "volumes/volume3/images/sunhalfright.png"
    pause 0.75
    "volumes/volume3/images/sunright.png"
    pause 0.75
    "volumes/volume3/images/sunhalfright.png"
    pause 0.75
    "volumes/volume3/images/sunbase.png"
    repeat

image burnsight = "volumes/volume3/images/burnsight.png"

image bg skyllahive = Image("volumes/volume3/images/skylla_hive.png", ypos=730)
image bg desert = Image("volumes/volume3/images/desert.png", ypos=730)
image bg desert night = Image("volumes/volume3/images/desertnight.png", ypos=730)

image bg cave = Image("volumes/volume3/images/bronya_cave.png", ypos=730)
image bg nursery = Image("volumes/volume3/images/bronya_nursery.png", ypos=730)
image bg2 cave = Image("volumes/volume3/images/bronya_cave.png", ypos=730)

transform bisonmad:

    xpos 85 ypos 425
    pause 0.1
    xpos 83
    pause 0.1
    repeat

transform bisonshake:

    xalign 0.49
    pause 0.1
    xalign 0.51
    pause 0.1
    repeat

transform bisonstomp:

    ypos 738
    easeout 0.16 ypos 712
    easeout_back 0.10 ypos 738

    pause 1.2
    repeat

transform bisonrun:

    xpos -1400
    linear 1 xpos 1400
    pause 7.5
    linear 1 xpos -1400
    pause 8.5
    repeat

transform popup:

    alpha 0.0 ypos 45

    parallel:
        linear 0.2 alpha 1.0
    parallel:

        linear 0.8 ypos 30

    linear 0.4 ypos 35 alpha 0.0

transform pullback:

    xpos 620
    ease_back 0.65 xpos 360
    pause 1.2
    block:


        parallel:
            easein_elastic 0.75 xpos 650
            pause 0.05
            easein_back 1.0 xpos 360
            pause 0.68
            repeat
        parallel:

            linear 0.05 ypos 722
            linear 0.05 ypos 720
            repeat

transform calming:

    parallel:
        easein 0.2 xpos 360

        easein_elastic 0.9 xpos 705
        pause 0.5
        easein_back 1.4 xpos 360
    parallel:

        linear 0.12 ypos 722
        linear 0.12 ypos 720
        repeat (16)
    block:

        linear 0.25 ypos 722
        linear 0.25 ypos 720
        repeat (4)
    block:

        linear 0.5 ypos 722
        linear 0.5 ypos 720
        repeat (2)

transform returntocenter:

    xpos 360
    linear 0.5 xpos 635

transform shake:

    xalign 0.5
    linear 0.15 xalign -0.01
    linear 0.15 xalign 1.01
    repeat (2)

transform slowfadeout:

    alpha 1.0
    pause 6.5
    easein 25 alpha 0

transform flipped:
    xzoom -1.0

transform skyllapunch:
    xpos -200 ypos -250 rotate 0
    pause 1.1
    linear 0.1 xpos -125 ypos -50 rotate 0
    ease_back 0.25 xpos -300 ypos -200 rotate 20
    pause 0.5
    ease_back 0.35 xpos -350 ypos -50 rotate -35
    linear 0.1 xpos -75 ypos -225 rotate -25
    block:

        pause 0.4
        easeout 0.4 xpos -250 ypos -175 rotate -25
        pause 0.3
        linear 0.1 xpos -40 ypos -225 rotate -10
        pause 0.25
        easeout 0.55 xpos -100 ypos -150 rotate -15
        pause 0.3
        linear 0.16 xpos 450 ypos -225 rotate -5
        pause 0.25
        easeout 0.6 xpos 0 ypos -150 rotate -10
        pause 0.35
        linear 0.2 xpos 1100 ypos -225 rotate 0





label volumethree:

    $ renpy.block_rollback()

    $ main_menu = False

    show expression "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)

    op "Putting one foot in front of the other, you continue on through this strange alien world."

    op "Just when you think stuff is beginning to make sense it all slips through your fingers and becomes even stranger and more alien."

    op "There does, however, seem to be one thing that remains constant through all planets and walks of life."

    op "That thing is\n {size=80}{=friend}FRIENDSHIP.{/=friend}{/size}"

    op "You are on the prowl for more."

    op "It would have perhaps been wise to stay with one of your wonderful new friends until you are fully healed..."

    op "But as Martha Stewart said, “Visitors, like fish, begin to smell after three days.”"

    op "You are almost positive Martha Stewart said that."

    op "Nevertheless, you soldier on in your endless quest for companionship."

    op "Where will your travels take you next?"

    call screen troll_select3 with Dissolve(1.0)

    with Pause(0.25)

    return

label skylla:

    $ renpy.block_rollback()

    scene black with Dissolve(1.0)

    scene bg desert with dissolve

    $ quick_menu = True

    "As dawn approaches, you find yourself heading out of the big city and into the rustic outskirts."

    play music "volumes/volume3/music/skyllatheme.mp3" loop

    show sun 2 with Dissolve(1)

    "Man. The sun sure is bright on this planet. It’s rising over the crest of the distant hills--a huge, fiery ball. The later it gets the bigger and bigger it grows, way bigger than you’ve ever seen the sun on earth."

    "What’s that smell? Could it be your flesh beginning to sizzle? Fantastic! You love the country."

    "No wonder the nightlife seems so active on Alternia. They are all nocturnal to avoid brutal, daily roasting."

    "You reach into your pocket for your cool new shades, but you appear to have left them at your friend’s house. Fuck."

    "You gotta get yourself together. The recent physical trauma and extensive blood loss has you a little fuzzy. You weren’t built for this wilderness survival shit."

    "You’re starting to wish you’d just stolen a fucking Lamborghini or something, instead of a spaceship."

    "This seriously isn’t looking good. The city is too far away now for you to turn back, so you have no choice but to keep walking."

    "Maybe you can find a cave or a hole in the ground. Maybe you can just cover yourself with grass."

    "You wish that someone had mentioned the death sun in between offering you alien meat products and calling you their muse."

    "Off to your left in the distance you catch sight of what might be the shimmer of sunlight on glass. A window? A solar panel? You could seriously clean up with renewable energy on this planet."

    "Should you change your trajectory and go toward the shimmer? It might just be a mirage."

    menu:
        "Should you change your trajectory and go toward the shimmer? It might just be a mirage."
        "[pick] Go toward the shimmer.":



            "You turn your aching, stinging meatsack toward the distant promising sparkle of safety and succor."

            "You focus on just staying upright. One step at a time. Just keep swimming, or whatever. God. This sun, though. You need SPF 5 million for this nonsense."

            "But then, almost like it has picked itself up to come scuttling to meet you, you suddenly find yourself in front of a long, low structure."

            "You let out a yelp of anguish, pounding on the door. At least, you hope it’s the door."

            show skylla concern behind sun with moveinbottom

            sky "What in the world?"

            show bg skyllahive with dissolve

            show sun 1 with dissolve

            "The door opens and you fall inside with one of the most pathetic whimpers of your career."

            hide sun with dissolve

            "Blessed darkness closes in on you. From right beside you comes a snuffling yip, like some joker is making fun of your dire situation. Something warm and wet glides up your stinging cheek."

            sky concern "Hold on, Ladyy!"

            sky "Give ‘em some room."

            "A pair of hands help you sit up, gently. Your eyes haven’t adjusted enough to make out more than a couple shapes, one upright and one lower to the ground."

            sky "What were yyou doin’ out there?"

            sky talk "Can yyou stand?"

            "Strong arms pull you to your feet. You wonder if everyone on this planet is strong or if you are just extremely flimsy. They guide you to a chair at the end of a long table."

            "Stutteringly, you begin to explain yourself--that you are an injured, exhausted traveler who is ravenous for pals."

            sky "Well bless yyour heart,"

            sky stand "But hold on a tick."

            sky "Dinner’s about to burn."

            "Now that your rescuer mentions it, you do smell something. It smells... amazing."

            sky talk "Funnyy yyou should just blunder in here like that."

            sky stand "I was just sayyin’ wasn’t I, Ladyy?"

            sky "It’s been so long since we had anyy sort’a guests who weren’t imperial drones or out to rob us."

            "You rub at your watering, slowly-clearing eyes, and when you look back up your rescuer finally comes into focus."

            "She’s tall--taller than anyone else you’ve met here, you think. Also, maybe a little older? Not that you’re an expert in troll physiology, she just has an air of knowledgeable competence. She’s wearing a fringed jacket and holding up a plate."

            sky talk "There yyou go."

            sky "Yyour oculars feelin’ anyy better?"

            show skylla happy at nod

            sky "Byy the byy myy name’s Skyylla! Pleasure to meet yyou!"

            sky talk "And this here’s Ladyy."

            show lady at right with moveinbottom

            "She looks down, and at first you think she means the table. But then you look under the table at the giant monster dog looking up at you. You jolt so hard you almost fly backward out of your goddamn chair."

            show skylla concern at bounce

            sky "Whoa there!"

            sky "No need for theatrics."

            "It looks a little like one of those lassie dogs with the pointed noses, except enormous and pure white. Its barks practically shake the whole house."

            sky talk "Heyy there, Ladyy."

            sky "No need to be rude."

            sky "Theyy’ve clearlyy had one hell of a time and theyy don’t look dangerous."

            sky stand "Just reallyy peculiar!"

            show skylla stand at nod

            sky "Sides, if theyy tryy anyything yyou and me can take ‘em."

            "Skylla puts her hands on her hips, staring you down with thunderous yellow eyes."

            sky "Right?"

            sky "No funnyy business, yya hear?"

            "You swallow and nod, trying to look unthreatening and obliging. Ready for anything. For instance... friendship. You are so ready for that."

            "Skylla sets down the plate she’s holding."

            sky talk "Here, have a grubcake."

            sky "There’s plentyy."

            "That sounds gross as hell, but what’s sitting on the plate looks and smells exactly like a normal pancake, golden-brown and crispy at the edges."

            sky "There’s boiled tree blood too, if yyou like."

            sky "Also churned dairy product."

            "She puts down a carafe of syrup and a dish of butter. Man, everything here has really weird names. Skylla pours out a cup of some very familiar-smelling liquid. Brown bean juice, you guess."

            "Skylla raises an eyebrow."

            sky "Um."
            sky "No..."
            sky stand "That’s just coffee."

            "She sits down next to you."

            sky "Yyou’re lucky yyou were onlyy out in the light at dawn."

            sky "Nobody wants to be out in direct Alternian sunlight besides jadebloods."

            sky "And no offense but yyou certainlyy ain’t anyy jadeblood that I’ve ever seen."

            sky talk "At first I thought yyou were some sort of mutated lusus ‘cause yyou don’t have horns and yyou were gruntin’ and yippin’ up a storm back there."

            sky "But yyou’re an alien, right?"

            sky concern "Don’t worryy."

            sky "I won’t call the drones."

            sky talk "I’d best get used to bein’ around aliens, anyywayy."

            sky "Seeing as how I’m gonna be seein’ a whole mess of yy’all come next sweep."

            "She laughs nervously."

            "You aren’t sure what she’s talking about. Do you even need to specify that anymore? It’s just natural law at this point. Gravity, the conservation of energy, and you don’t know what the fuck is going on."

            sky "Ladyy, would you mind drawing a bath for our guest?"

            sky stand "No offense, but yyou smell like yyou could use one."

            "You can’t argue with that. You offer her a cautious smile. God, she seems so nice and caring, but you’ve been burned before. And cut. And generally kicked around by fate."

            "It’s a tough world out there. But you want to trust Skylla."

            "Ladyy takes a bucket in her muzzle and runs out into the yard, getting up on her hind legs and batting at the door latch to open it. It’s adorable."

            hide lady with moveoutright

            show sun 1 with dissolve

            pause(0.25)

            hide sun with dissolve

            "The sun is high enough now that the whole landscape outside is washed in white."

            "... Oh god, the dog!"

            sky talk "Oh, it’s sweet of yyou to worryy."

            sky stand "Lusii are fine go’in outside for a little while in the daylight--their coats reflect light, or somethin’ to that effect."

            sky talk "I don’t reallyy know how it works."

            sky "I ain’t exactlyy known for my scientific acumen."

            "You tell her that she seems pretty smart from where you’re standing."

            "As cynical as you are becoming, you just can’t help trying to be her friend. She’s so nice and, wow, really pretty."

            "Not that that’s a requirement for friendship, but your retinas would have to be way more scalded than they are not to notice that."

            sky stand "That’s nice of yyou to say."
            sky "But it wouldn’t even reallyy matter if I was a bonafide genius."
            sky numb2 "Someone of myy caste could never hope to rise up in the ranks."
            sky talk "Best I can hope for is haulin’ crates on some cargo vessel."

            "Ranks? Cargo vessel? You swallow your bite of grubcake, ready to ask her if she is thinking about joining the military, but just then a swell of noise erupts from outside the house."

            show skylla concern at bounce with hpunch

            "Shouts, crashes, and Ladyy’s frantic barks. Skylla gasps and launches herself out of her chair, knocking over the carafe of syrup. It oozes across the tabletop in a sticky wave."

            sky "Oh no!"
            sky anger "Not now!"

            "What the hell is going on?"

            sky "Bandits!"
            sky "Goddamn lusus thieves!"

            show sun 1 with dissolve

            "You don’t get the chance to ask anything else before Skylla careens toward the door, throwing up an arm as blazing white light pours in."

            "Oh, god. She’s going to go outside and burn up. She isn’t thinking straight. You’ve got to do something!"

            menu:
                "Oh, god. She’s going to go outside and burn up. She isn’t thinking straight. You’ve got to do something!"
                "[pick] Stop her!":



                    "Skylla is bigger than you, and she has the strength of both desperation and a superior genome, so you don’t feel great about your chances."

                    "But you have to try. Skylla is too upset to be careful. You have to stop her from hurting herself."

                    "You stumbled into her house all gross and pathetic and alien and she didn’t turn you away. She gave you pancakes, for chrissake."

                    "Grubcakes. Whatever."

                    "And it isn’t just the sun--from the number of voices, there’s got to be twenty people out there. She doesn’t stand a chance."

                    show skylla anger at pullback

                    "You run up behind her and hook your arms under hers, hauling her back by the armpits. She struggles, jabbing her elbow into your aching ribs."

                    sky "Let me go!"
                    sky "Yyou don’t understand, theyy’ll take her!"
                    sky distress "Ladyy!"

                    "You hold grimly on, going limp and using gravity and your own dead weight to pull her down to the floor."

                    "Through wheezing breaths you tell her she can’t go out there, didn’t she just tell you that you’d never have survived if it had been later than dawn?"

                    "You probably aren’t making much sense, but you keep up a stream of worthless bullshit until something catches."

                    show skylla distress at calming

                    "Would your lusus really want this for you, Skylla? Would Ladyy really want you to sacrifice yourself for her?"

                    "Skylla goes rigid, and then all the fight just drains out of her like blood down a drain. She sags back into your arms."

                    show skylla numb at default with move

                    "The two of you watch Ladyy thrashing in a huge black net as several of the figures haul her away."

                    "The sun is too bright to see them clearly, but they appear to be herding more white creatures out of a paddock and into a collection of vehicles."

                    show skylla numb at lowered

                    sky "The herd..."

                    "She says it so quietly you feel it more than hear it."

                    "You continue to watch as Ladyy is packed into one of the vehicles and they drive away, kicking up clouds of dust that glimmer in the brutal sun."

                    sky "Yyou can let me go now."
                    sky upset "I’m not going to throw myyself out into the dayylight like a romance novel heroine."

                    "You realize just how tight you’re holding on to her and loosen your arms, pulling away and sitting up."

                    show skylla depressed at shake

                    "Skylla’s cheeks are wet with tears, but she quickly shakes her hair into her face to hide it. That makes your heart hurt."

                    "You want to tell her that everything is going to be okay, but you make it a point not to lie to your friends. You have absolutely no idea how it’s going to be."

                    hide skylla depressed with Dissolve(0.75)

                    "And before you can say anything at all, she gets up and disappears through a door and further into the house."

                    menu:
                        "[pick] Give her some space.":


                            "You decide to mind your own business. Well, you do try the door, but it’s locked."

                    hide sun with dissolve

                    "Best to keep occupied, and do what you can for her. First, you shut the door, to keep that sweltering heat and blinding light out."

                    "Then, you tidy up the kitchen a little. Everything here is oddly textured and colored, the shapes unusually organic. Some of it is worryingly scuttly and alive. You do your best."

                    "You mop up the syrup and straighten the chairs."

                    "You’re just trying to figure out how to get the sink to spit out some water onto the dirty dishes, when Skylla comes back out. Her eyes are dry and her hair is combed back out of her face."

                    show skylla numb with dissolve

                    sky "Don’t you worryy about that."
                    sky "Yyou’re gonna break somethin’."

                    "She plays with one of her beaded bracelets with nervous little fidgets of her fingers."

                    sky "I could never have taken those fellas by myyself."
                    sky "Especiallyy not in broad dayylight."
                    sky "I wanna thank yyou for steppin’ in and stoppin’ me."
                    sky upset "I was overwrought."

                    show skylla numb

                    "You nod, accepting her thanks. She doesn’t seem overwrought anymore. Just numb."

                    "Wow, this is actually a legitimately terrible situation. Not even in a dumb, zany way like all the other horseshit that has happened to you recently."

                    "You wonder who those guys even were."

                    sky "Lusus thieves."
                    sky "Theyy’ve come before, but alwayys at night and never in such large numbers."
                    sky "So Ladyy and me could alwayys take ‘em."
                    sky "I never expected anyythin’ like this."

                    show skylla upset at bounce

                    sky "For them to come out in force like this in the middle of the dayy!"

                    show skylla at lowered

                    "She sits down at the table, putting her elbow in a patch of syrup you missed."

                    "You offer her the dishcloth, and notice several little discolored patches on her arm. It looks like she got burned just from having her arm out the door for like a minute and a half."

                    "You’re really glad you didn’t let her go out there."

                    "You’ve endured a lot of heinous shit on your short span on this planet--injuries, and lots of added insults to those injuries. But the time you spend with Skylla waiting for the sun to go down is some of the worst and most hopeless."

                    "You don’t know what to say to help her--you aren’t actually her friend. You aren’t even the same species."

                    "The troll/lusus relationship is a little confusing, but they seem to be some combination of caretaker and pet. More symbiotic than parent and child."

                    show bg desert night
                    show skylla at default
                    with fade

                    "Finally, it gets late enough to venture outside and you follow Skylla out to the empty paddock. There’s nothing out here but a broken fence and trampled ground."

                    sky upset "Lots of kids lose their lusii..."
                    sky "It’s just a part of life."
                    sky numb "I would have been heading into the ordeals next sweep anyyway."
                    sky "I would never have seen her again."
                    sky upset "But at least I would have gotten the chance to say goodbyye, yyou know?"

                    "It’s kind of a bummer how resigned everyone on this planet seems to terrible things happening. Then again, you guess that’s sort of true on your planet too. Existence: just a goddamn mess."

                    "You try to give her the most understanding look you can. Just a really good and supportive friend face. You’re killing it."

                    "But Skylla isn’t paying attention to your glowing facade. She’s reaching into her jacket and pulling out her phone."

                    sky numb "What the hell..."
                    sky "Myy palmhusk is blowin' up."

                    show skylla upset at bounce

                    sky "Oh god."

                    "Skylla drops her phone in the dirt and claps a hand over her mouth. Her eyes sparkle with tears."

                    "You pick it up. It’s kind of squishy and squirms in your hand a little, which you don’t love. You also don’t love what’s on the screen."

                    "It’s a troll in a mask, holding a gun on Ladyy, who is still in that net, baring her teeth. The gun looks fake--kind of like a nerf gun."

                    "... You bet it’s not a nerf gun."

                    "The photo is accompanied by more of that spiky text that you can’t read."

                    "Hey, how can you understand the Alternian spoken language but not the written? You decide not to think about it too hard. Waste of time."

                    sky numb "Theyy sent a ransom demand."
                    sky "Theyy sayy that if I can’t pay theyy’ll sell her."
                    sky "Troll lusii are valued for their strength all over the galaxyy."
                    sky "The heiress knows about the black market but she doesn’t do anyything about it--she just takes a cut."

                    "You ask her how much the ransom demand is for, as if you have a penny to your name."

                    "She tells you a number that sounds stupidly large, even without knowing the exchange rate to Earth Money."

                    sky upset "Theyy’re just mockin’ me."
                    sky "Theyy know a bronzeblood can’t afford this."
                    sky depressed "Theyy just want to force me to fail her one more time."

                    "Her voice breaks on a sob. You reach over and put your hand on her arm. She looks at you with big watery eyes, and you brace for her to fall into your arms sobbing. You’re actually kind of hoping for it."

                    "Not that you’re the type to want to profit off another’s pain, but you’re pretty sure that offering comfort in a time of crisis is a first class ticket to Friendsville."

                    show skylla upset with vpunch

                    "Instead Skylla gives you a hard shove backward."

                    "You take two stumbling steps and fall on your ass. Something squishes underneath you. A cowpat, or something alive? You aren’t sure which you’d prefer, honestly."

                    sky numb "Sorryy."
                    sky "I didn’t actuallyy push yyou that hard."
                    sky "Yyour species just seems prettyy flimsyy."
                    sky upset "I don’t want syympathyy right now."
                    sky depressed "...especiallyy not from yyou."

                    "She stands framed between the two moons, some trick of perspective making her look just as distant. And just as sad. Not that moons are inherently sad."

                    "Whatever. That’s not the issue right now."

                    "Had Skylla been lying to you before when she said she doesn’t blame you? She’d even thanked you for stopping her from killing herself!"

                    sky numb "Naw, I don’t blame yyou."
                    sky "I just... can’t stand the sight of yyou."
                    sky depressed "Lookin’ at yyou just reminds me of losin’ Ladyy and I don’t think that’ll ever change."
                    sky "Sorryy."
                    sky upset "I reallyy was hopin’ we could be friends--it’s been a reallyy long time since I’ve seen anyybodyy out here that goes on two legs ‘stead of four."
                    sky "But I just don’t think it’s gonna work out."
                    sky numb "...if yyou start walkin’ now yyou can probablyy make it to the cityy before sunrise."
                    sky "Or there’s a jadeblood colonyy nearbyy if yyou want to inflict yyour personal brand of assistance on them."
                    sky upset "Byye."

                    show skylla depressed

                    "You leave with your proverbial tail between your legs, and the last glimpse you get of Skylla she’s standing next to the empty paddock, staring at the ground."

                    hide skylla with Dissolve(1.0)

                    call ending ("gameover skylla2", False, True) from _call_ending_8

                    return
                "[pick] Help her!":


                    "What the hell. You’ve already experienced the Alternian sun. It sucked a whole lot. Maybe now will suck less, because of how bad it sucked then. Just... a sliding scale of suckage."

                    hide skylla with moveoutright

                    if persistent.flash:
                        show sun 2
                        show bg desert behind sun
                        with Fade(0.25, 0.2, 0.25, color="#fff")
                    else:
                        show sun 2
                        show bg desert behind sun
                        with Fade(0.25, 0.6, 0.25, color="#fff")

                    "Skylla plunges out into the daylight in the direction of the commotion, and like a big dumb asshole you barrel out into the blazing hellscape after her."

                    "Surprise! It still sucks. You’ve had sunburns before, but this is ridiculous."

                    "This is a fucking monster of a gas giant pointing and laughing at the tiny speck of humanity you represent, trembling before the void."

                    "It’s a pure assault on all your senses. The light is almost as bad as the heat, and you put up your arms to block the glare, following the dust Skylla kicks up behind her."

                    "You doubt your eyes will actually ever adjust to this fuckery, but you can see a little better than before."

                    "There are about a dozen of them--all of them trolls, all wearing dark, padded outfits that cover their faces. They look halfway between hazmat suits and swat uniforms."

                    "All of them have big, fake-looking guns that probably aren’t fake."

                    if persistent.flash:

                        with Fade(0.20, 0.05, 0.20, color="#ffcc00")

                    "In fact, one of them shoots a laser at your face. You duck, and it leaves a blazing heat trail across your cheek."

                    "But as all of you is currently burning, it doesn’t really break your stride."

                    show skylla anger behind sun
                    with moveinleft
                    with hpunch

                    "Skylla throws herself into the fray, letting out a warcry accompanied by the sound of a fist hitting flesh."

                    hide skylla anger with moveoutright

                    "It’s twelve against two. Which, if you remember your fractions right, is not unlike six against one."

                    show skylla anger behind sun at flipped
                    with moveinright
                    with hpunch

                    "But these guys had probably not been expecting a frontal assault, and they had definitely not been expecting a Skylla, who is frankly fucking terrifying."

                    "She shoves three trolls down like dominoes, grabbing up a discarded gun and shooting all three while they’re on the ground."

                    if persistent.flash:

                        with Fade(0.14, 0.02, 0.14, color="#ffcc00")
                        with Fade(0.14, 0.02, 0.14, color="#ffcc00")
                        with Fade(0.14, 0.02, 0.14, color="#ffcc00")

                    "You have never been in a fight before. A fucking all-out brawl. It’s scary. But now that you are in the thick of it, also kind of awesome?"

                    hide skylla anger with moveoutleft

                    "Sure, your skin is burning and you could be killed at any moment, but that’s just how it goes on this planet."

                    "You just gotta get into the swing of things. Take no prisoners. Kill or be killed! Hell yeah!"

                    with vpunch

                    show skylla kickass behind sun
                    with moveinleft
                    with hpunch

                    "You pop one of the bandit trolls in the face. Fuck. That probably hurt your fist more than it hurt the troll, but it does throw them off balance for long enough for Skylla to smash the butt of her gun into the side of their head."

                    sky "Yyee haw!"
                    sky "Hell yyeah!"

                    "She gives you a wild grin. The two of you are beaming at each other while a hostile alien sun tries to boil away the liquid from your eyeballs and a bunch of bandits try to dognap a giant monster. You love this girl."

                    show skylla behind sun at flipped
                    hide skylla with moveoutleft

                    "In a friendship way."

                    "But still! You love her! You make an awesome team!"

                    show skylla kickass behind sun at skyllapunch with moveinleft

                    "Another troll comes up behind Skylla and she smashes an elbow into their throat, grabbing them by the front of their uniform and supplexing them onto the dusty ground."

                    with hpunch

                    "She wails on them with her bare hands."

                    with hpunch

                    "God."

                    hide skylla with moveoutright

                    "She’s really hot."

                    show skylla anger behind sun at flipped
                    with moveinright
                    with hpunch

                    sky "Get Ladyy!"

                    hide skylla with moveoutleft

                    "Oh, right."

                    "You stumble over to where the lusus is thrashing inside a big black net. You don’t have any way to cut her free, but she’s already doing great on her own, biting through the fibers with her big sharp teeth."

                    show lady behind sun with moveinbottom

                    show lady at bounce

                    "You hold the net still for her to finish the job, then pull it off her so she can join the fray."

                    hide lady with moveoutright

                    with hpunch

                    with vpunch

                    with hpunch

                    "It’s over fast after that. How did they even get Ladyy into the net in the first place? She’s so giant and quick, grabbing trolls in her jaws and shaking them like chew toys."

                    "The remaining five who are still standing jump into their weird little dune buggies and make tracks. Emphasis on the “bug”. They look like scuttling little beetles."

                    show skylla kickass behind sun with moveinleft

                    "Skylla chases after them for a few hundred yards, throwing the gun after them and shouting obscenities."

                    show skylla happy at bounce

                    sky "And stayy awayy, yya hear!!"

                    show skylla happy at bounce

                    sky "Tell the rest of ‘em whyy yyou don’t ever fuck with a rustyy’s ranch!"

                    "She stands silhouetted against the blazing sun, the dust trails vanishing into the distance. You are awash in heady victory, giggling like a lunatic, before the adrenaline kind of drains out of you all at once."

                    "You are violently reminded of your fucked up ribs and recent blood loss."

                    "The Alternian sun beats down, and your arms are already covered in raised patches of red skin. This is a sunburn turned up to eleven."

                    sky concern "Whoa there, are yyou..."
                    sky "Are yyou okayy?"

                    "Skylla is swaying too. A spray of olive-green blood covers her cheek. At least the rainbow blood on this planet means you can be sure it isn’t hers. But she still looks rough. Kind of how you feel."

                    show skylla concern at bounce

                    sky "Ladyy!"
                    sky "C’mere girl!"

                    show lady behind sun at right with moveinright

                    "Wow. You’re just... you’re gonna sit down. Maybe just take a little break. The pale landscape swoops, going even paler."

                    sky "No, yyou can’t rest here!"
                    sky "Yyou’ll die, dumbass!"
                    sky happy "I’m not lettin’ anyything happen to myy new best friend."

                    show skylla happy at bounce

                    sky "Get up!"

                    "New best friend? Holy shit. That makes you so happy. You absolutely can’t die here. Not when you’ve just made such an amazing friend."

                    show skylla concern

                    "Somehow, the two of you manage to drag each other across the yard and toward the house. Hive. You’re gonna get this lingo down if it kills you."

                    show lady at nod

                    "Whenever you feel yourself about to fall forward, you lean on Skylla. When you start to fall back, Ladyy is there to brace herself against the back of your knees. She’s such a good lusus."

                    "You wonder if she’ll be your friend too. Her muzzle is dripping with a soup of multicolored alien blood."

                    show blackcover at slowfadeout with dissolve
                    show burnsight behind blackcover
                    show bg skyllahive
                    hide sun

                    "When you get back into the darkness of the hive, you can’t see shit."

                    sky talk "Dang, yyour species reallyy ain’t suited for this kinda environment, huh."
                    sky "Yyou can’t even see in the dark."

                    "In demonstration you walk right into the table. You’ve about had it with tables. You are sworn enemies at this point."

                    sky concern "Please don’t knock down myy nutrition platform."
                    sky stand "I built it myyself."

                    "She sounds exhausted but giddy. Dang, you really did that thing, didn’t you?"

                    "You kind of want to go in for the hug, but that sunburn is really something. It feels like tiny needles piercing your arms and cheeks. The back of your neck is a colony of fire ants."

                    sky concern "Oh, yyeah."
                    sky "Feels real bad, don’t it?"
                    sky talk "C’mon, there’s onlyy one cure for sunrash."

                    "Skylla takes your hand. Gosh. This is next level friendship stuff."

                    hide lady with dissolve

                    "She leads you through her hive, and who knows if you are ever going to get all of your vision back. Maybe you are just blind for life."

                    "You’ll have to get a cane and a whimsical aesthetic, and learn to navigate the world by smell alone."

                    "No, that would be stupid."

                    sky "Here we go."
                    sky "My ‘coop isn’t huge but yyou’re kinda scrawny."

                    show skylla stand at bounce
                    sky "What are yyou waitin’ for?"
                    sky "Take yyour clothes off."

                    "Man. The sun must have fucked with more than just your eyes, because you could have sworn Skylla just told you to take your clothes off."

                    sky talk "Yyou are seriouslyy not gettin’ into myy recuperacoon in those filthyy rags."
                    sky "I’m not even sure what those clothes were supposed to be originallyy."

                    "Yeah, you aren’t so sure about your look either. Another new friend of yours told you it was rad, but you were both a little high at the time."

                    "You might be a little high right now. You wonder if sunstroke causes auditory hallucinations. Also, you don’t know what a recuperacoon is."

                    sky concern "Hmm?"
                    sky "Reallyy?"
                    sky "Then what the heck do yyou sleep in on yyour planet?"

                    show skylla at lowered

                    "You hear rustling, followed by the sound of clothes hitting the floor, and then a weird {i}gloop gloop{/i}, like someone getting into a bathtub only... thicker."

                    sky stand "If a troll didn’t have sopor, well..."
                    sky concern "I don’t rightlyy know what would happen."
                    sky stand "But I reckon it wouldn’t be great."
                    sky "It can speed the healin’ process for burns and small wounds."
                    sky "I’m not sure what it’s gonna do to your weird alien anatomyy, but I don’t see as how it’s gonna make it anyy worse."

                    "You tell Skylla that in your experience, things can always get worse. Especially from her perspective right now, since she’s about to see you naked. Nothing like a little self-deprecating humor as an A+ cover for crippling insecurity."

                    show skylla talk

                    "Skylla laughs."

                    sky "C’mon now."
                    sky "I’m sure yyou’re a perfectlyy healthyy example of yyour species."
                    sky stand "Just get in alreadyy!"
                    sky concern "I promise this isn’t anyy sort of pale solicitation."
                    sky "Or flushed, for that matter."
                    sky talk "I know it’s awkward but... I only got the one ‘coop."

                    "Right, okay. Yeah. You can totally do this. You can make this not weird."

                    "Of course, you trip taking off your goddamn pants and Skylla starts laughing all over again."

                    "Not in a mean way. More in a chill, {i}please join me in my slime bathtub, old chum{/i} way."

                    "In a non-awkward way."

                    "In a... FRIEND WAY."

                    call ending ("win skylla", True, False) from _call_ending_9

                    return
        "[pick] Forget it.":


            stop music fadeout 1.0
            play sound "volumes/volume3/music/fire2.mp3"

            show sunclassic with Dissolve(1.2)

            "Honestly you could probably see this one coming."

            stop sound fadeout 1.0

            call ending ("gameover skylla1", False, False) from _call_ending_10

            return

label bronya:

    $ renpy.block_rollback()

    scene black with Dissolve(1.0)

    scene bg cave with dissolve

    $ quick_menu = True

    "You've been travelling through a cave network for a while now."

    "The rigid stone is a welcome respite from the eerily organic infrastructure you've been encountering, but it is also proving an unwelcome respite from friendmaking."

    "Maybe it was too much to hope for, that this cavern would be home to another potential new buddy."

    "Maybe leaving the big city behind was a horrible mistake."

    "Just maybe, these dark, cold tunnels are completely devoid of oh hang on there's a bunch of buildings in the distance."

    play music "volumes/volume3/music/bronyatheme.mp3" loop

    show bronya um with moveinbottom

    bro "Oh, hello."
    bro "I thought you were one of my girls, but you don’t look like a jadeblood. Or anything else, actually. How strange."

    "You convey your usual spiel regarding your circumstances: you are lost, and lonely, and your ribs are still broken you think?"

    "Honestly, the ribs are fine. You could just use another friend or two."

    bro "I see. My first responsibility is to my jades and the Mother Grub, so I can’t make any promises of friendship just yet. But you do look like you need someone to take care of you."

    show bronya happy at bounce
    bro "vV Here in the brooding caverns we follow a few simple rules! Vv"

    bro um "1. Don’t invite drama from up top down below.{p}2. Protect the Mother Grub.{p}3. We have no hierarchy, but do what I say."

    show bronya happy at bounce

    bro happy "vV Let’s do everything we can to keep up our current record of dozens of sweeps without any jades\nbeing culled! Vv"

    "You’re not sure what half of those words mean, but you nod your head."

    bro talk "Good. I’ll take you to our hive."

    show bronya happy at bounce

    bro "vV Follow me! Vv"

    show bronya talk

    "You follow her into her hive, which looks like a school or some kind of dormitory, with multiple rooms and multiple floors."

    bro "Usually more of my jades are around. I suppose that everyone is out watching the Imperial Drones arrive with the filial pails."

    show bronya happy at bounce

    bro "vV Girls! We have a visitor to our caverns! Vv"
    bro um "1. Do not be alarmed by their bizarre appearance, they seem to be harmless and quite weak.{p}2. Do not give them more injuries than they already have."

    show bronya happy at bounce

    bro "vV Our visitor deserves a warm jadeblood welcome! Vv"

    "She claps her hands. No one else is around, but you stand to attention and give her the thumbs up to show that you read her loud and clear."

    show bronya talk

    "You noticed that she called you ‘visitor’ and not ‘friend,’ but that’s okay. You can do whatever it takes until you’re upgraded from ‘visitor’ to ‘friend,’ or at least ‘charity case.’"

    show bg nursery with wipeup

    "You follow her upstairs and she stops at a big room on the second floor. When you step into it you have to clap your hand over your mouth to keep from gagging at the revolting sight."

    "There are big, baby-sized larvae-looking things all over the floor, squirming around and crying and inch-worming out of kiddie pools of green slime. What the hell?"

    bro mom "This is our nursery. Most of these wigglers are sick or injured, so we look after them in here until they’re well enough to go back out to the caverns and spin their cocoons."

    show bronya worried

    "She looks shifty all of a sudden, giving you some side-eye like she’s sizing you up. You try to look very non-threatening and also 100 percent trustworthy."

    bro "We keep this nursery on the down-low. It’s not against any laws, but it’s something of a break with tradition to save any of the grubs instead of just letting them die."
    bro mom "To tell you the truth, I’m not sure why we do it. I guess it just feels right to me to take care of them, the same way I take care of my jades."

    "A nursery, huh? You look around again with this new information. You guess you can sorta see how the wigglers look like babies."

    "You can’t believe that one of these things could grow up into anything that looks like Bronya, but this is an alien planet, so who knows."

    show bronya talk

    "She takes you over to a shelf that seems to hold medical supplies. You’re not sure what can be done for your broken ribs, but maybe she has some kind of alien technology that can help."

    "But when she starts going through the cabinet, you don’t see anything that looks high-tech like the thing that fixed your arm."

    bro um "Uh... I guess that most of what we have is stuff for the wigglers. And I’m not familiar enough with your bizarre anatomy to know if it will help."

    show bronya happy at bounce

    bro "vV But if you’re not completely sure how to do something, it’s best to try anyway! Vv"
    bro "1. Even if you fail, everyone else can still learn from your mistake.{p}2. Maybe you won’t fail. You never know!"

    "You’re not so sure about applying this ethos to your broken ribs. But she looks so determined. It might be rude to say no."

    menu:
        "You’re not so sure about applying this ethos to your broken ribs. But she looks so determined. It might be rude to say no."
        "[pick] Go for it. My ribs are already broken, so where’s the harm!":



            bro um "Okay, come here. Lift up your shirt so I can get to your injured bellowsac enclosures. Yes like that, turn the part that’s all bloody and horrifying towards me."

            "She has something that looks like some kind of... ointment?"

            "It’s a shade of bright green similar to the slime beds you see around the nursery, and it also seems to be glowing. Seems like there’s nothing wrong about applying it to your skin."

            "But despite your optimism, the second Bronya rubs some of it on your broken skin, you feel a searing hot pain like you just got doused with poison."

            show bronya worried with hpunch

            "You flinch back instinctively. Your momentum carries you too far, and as you step back you trip on something behind your feet."

            "You cartwheel your arms, but it’s no use. You’re going down, you’re yelling timber."

            show bronya panic with vpunch

            "You feel something soft and squishy break your fall, and you hear a terrible squelching noise and some kind of animal squeal."

            "You have fallen right onto one of the wigglers. You roll off of it, but there’s no use: it’s squished flat, and you’re covered in olive fluid that you think might be its blood."

            "You look up to see Bronya’s horrified face, and know that there is no hope for friendship in those vengeful eyes."

            bro angry "vV You might want to run, before I throw you out this window and break the rest of your bones! Vv"

            call ending ("gameover bronya1", False, True) from _call_ending_11

            return
        "[pick] Thanks but no thanks. I’ll heal on my own just fine.":


            bro um "Oh. Well, if you’re sure."
            bro talk "I’m worried about you though. You seem like you need help, and I wish I could help you more."
            bro "If I can’t take care of someone, I’m not sure how we can ever truly be friends. "

            "You try to cheer her up, pointing out that friendship is a two-way street, after all. She doesn’t have to concern herself with your mutilated frame. How can you help her instead?"

            bro um "Well... sure, there are things around here that I could use some assistance with."
            bro "However, don’t take this the wrong way, but we’ve only just met. I don’t know that I can trust you to be as responsible as I am."

            show bronya happy at bounce

            bro "vV It’s not easy to be the one in charge! You have to be: 1. Conscientious, 2. Considerate, and 3. Competent, at all times! Vv"

            "You try to think of times in your life when you’ve been conscientious, considerate, or competent. You’re drawing a bit of a blank, but hey, new planet, new you. You assure her that you have what it takes."

            bro talk "I guess if you want to prove that you can be responsible, I can let you help me out today."

            show bronya happy at bounce

            bro "vV It’s a good time for a visit to the Mother Grub! Vv"

            show bronya talk

            "You’re careful to step around all the little guys on the floor as you head out of the nursery."

            show bg cave with wipedown

            "She takes you back outside, and these caverns are even bigger than you first realized. They’re also dark, and cold, and gloomy, and you can’t see anywhere that might lead up to the planet’s surface."

            "Does she really just live down here all the time?"

            "To make some conversation during this cold hike in a damp cave, you mention that living underground like this seems kind of depressing."

            "You realize too late that this wasn’t very tactful, but she doesn’t get angry at your conversational gambit of insulting her home."

            bro "Oh no, it’s very peaceful down here. Well, in comparison to anywhere else."
            bro mom "I quite enjoy it."
            bro "The brooding caverns are a place for life and birth, not death!"
            bro um "That’s pretty uncommon on Alternia."

            show bronya talk

            "You’re still not sure what she means by ‘brooding caverns,’ but you guess it has something to do with the wigglers in her nursery."

            "Before you can ask, you reach the top of a ridge and get a new, wider view of the rest of this cavern."

            "It’s enormous, probably the size of a small city. All over the cave floor, you see more wigglers crawling everywhere. Cocoons line the cave walls and the larger stalactites, with some young trolls crawling out of them."

            "Walking, flying, and crawling among the wigglers and young trolls are a variety of white monsters, of all kinds and shapes and sizes."

            "In the center of the cavern, there is... You don’t even know how to describe it."

            "It looks like a huge many-legged queen bug of some kind, with a goat-shaped skull and horns coming out of her head."

            "Her bulbous sphincter ripples as she lays a continuous stream of hundreds of eggs, from which you assume the gray wigglers will hatch."

            "And marching through all this, you see several hulking bipedal creatures, each carrying two buckets either to or away from the Mother Grub."

            "They look armed and they move like regimented troops, soldiers of some kind. You are instinctively terrified of them."

            bro "This is where the magic happens. And by that I mean the continuation of our species."

            show bronya happy at bounce

            bro "vV Jadebloods like myself are entrusted with looking after this process, which is of course a very special job! Vv"
            bro "1. The Imperial Drones carry filial pails of genetic material to the Mother Grub for her slurry.{p}2. She lays eggs that hatch new grub broods."
            bro "3. After the wigglers emerge from their cocoons, the new trolls will go through the trials, and the ones that make it will be selected by a lusus to help care for them."
            bro "4. Together the young trolls and their lusii go up to the surface together, where the trolls will grow up, or get culled, or whatever."

            show bronya worried

            "As Bronya explains troll reproduction to you, one of the Imperial Drones veers sharply to the left and in the process, tramples over a few wigglers and young trolls."

            "The Drone continues on, but several of the lusii cry out, crowding around their dead or injured charges."

            show bgbison behind bronya at bisonmad with dissolve

            show bg2 cave behind bg

            "One of them, a gigantic beast that resembles a bison, bellows and rears up on its hind legs, hitting one of the other lusii with its front hoof."

            bro "Oh geez. Not again."
            bro um "This kind of damage control is a lot of what we have to deal with. Whenever a lusus goes rogue out of grief or confusion, there’s the potential for it to lash out at other lusii, the wigglers, or the Mother Grub herself."

            show bronya duty at bounce

            bro "vV We Jadebloods cannot let that happen! Vv"

            show bronya worried

            "She looks so concerned, a marked contrast to how confident she’s seemed before now."

            "You offered to help her out earlier, and it seems like now’s your chance. Someone has to stop that rogue lusus, and that someone could be... you?"

            menu:
                "You offered to help her out earlier, and it seems like now’s your chance. Someone has to stop that rogue lusus, and that someone could be... you?"
                "Fight the monster. Save the day. You’ve got this.":



                    "The bison lusus seems to be causing quite a ruckus. Other lusii have now gotten riled up too, with some of them trying to gather wigglers to keep them out of harm’s way and others just getting hyped to thrash."

                    "It seems like it could turn into a monster stampede, and they’re close to the Mother Grub’s big soft vulnerable abdomen. Not great!"

                    "Fighting a monster single-handed seems like a daunting first step in a friendship, but you did tell her you could be responsible."

                    "You square your shoulders and tell Bronya that she has nothing to worry about."

                    "You’re going to stop that lusus, calm down all the other lusii, and protect the Mother Grub, all without breaking a sweat and hopefully without breaking any more bones either."

                    bro um "Whoa there. I was going to suggest that I go after it while you stay here."
                    bro "You seem kind of weak and fragile. Even apart from your injuries, I mean."
                    bro worried "I don’t want you to get hurt worse, and I’m not sure I trust anyone other than myself to take the lead on this."

                    "That wasn’t quite the reaction you were hoping for. Normally, you would be all about sitting back and letting her protect you, because well--protective and responsible is a good look on her."

                    "But desperate times call for desperate measures, and you don’t know how else you’re going to prove yourself worthy to be her friend."

                    "You do your best to project an air of confidence, or at least competence."

                    "You assure her that this is no sweat for you. You take down raging bison back on your home planet all the time! You’re known for it, actually!"

                    bro um "Well... if you say that this isn’t your first ungulate-roping gallop exhibition, I’ll believe you."
                    bro "I’ll hang back to let you give it a shot."

                    show bronya happy at bounce

                    bro "vV But if it gets too overwhelming in there, I’m right here! Vv"
                    bro um "1. Caring for the Mother Grub is my responsibility as a jadeblood.{p}2. I’d never abandon a friend to deal with a mess on their own. If we end up being friends, that is."

                    "Oh hell yes. Now you have reason to hope."

                    hide bronya with moveoutleft

                    hide bgbison with dissolve
                    pause(0.3)
                    show bison with dissolve

                    show bison at bisonshake

                    "You approach the rampaging bison with caution. Do all bison have horns like that? Maybe they do--you’re no bison expert. But you’re pretty sure they don’t all have teeth that nasty."

                    "Bison on Earth mostly eat grass, don’t they? This guy doesn’t look like a herbivore."

                    "At first you try to calm the lusus down by talking to it, but your soothing words have no effect. In fact, you might have just made it even angrier by suggesting that it pause and take some deep breaths in reaction to its trampled charge."

                    "You’re not even sure it can understand human speech, come to think of it."

                    "You circle around it, wishing that you had some kind of lasso or something. Maybe you can herd it away from the Mother Grub."

                    "You look around to see if any of these other lusii look vaguely like Earth shepherd dogs, but no dice."

                    "You hesitate too long and the lusus turns away, its furious eyes falling on the Mother Grub."

                    show bison at bisonstomp

                    "It stamps its hooves, snorts air out of its nostrils and screams in a way that sounds a lot more hellish than you imagine normal bison are capable of."

                    "It’s obviously about to charge, and you can only think of one thing to do."

                    with hpunch

                    "In desperation, you leap forward and tackle it football-style, doing everything you can with your flimsy human body to drag it onto its side."

                    with vpunch

                    "It half-works: you plow into the lusus and stop it in its tracks, but it topples over onto a nest of wigglers, taking you down with it."

                    show blackcover with dissolve

                    "Wigglers and young trolls go bouncing everywhere, squealing in distress, and their lusii descend upon you in a rage."

                    "Everything is chaos for a while. You’re trapped beneath the bison lusus, which is very worrying for all your body parts and you think you might feel something important rupturing inside you."

                    "But hey, on the bright side this crushing mass is protecting you from all the other pissed-off lusii trying to attack you."

                    "Just as your whole breathing situation is starting to get dicey, you hear a commotion and what sounds possibly the trouncing of some of the smaller lusii that were trying to get to you."

                    "The crowd of beasts around you scatters, and then you hear her."

                    bro "Oof. I’m having a hard time getting this thing off of you. And he’s still very angry, he keeps trying to kick me."
                    bro "Where’s a bronzeblood when you need one..."

                    "You don’t know what that means, but you’re very grateful that she’s here to help you. You try to communicate this, but it comes out garbled from all the blood in your mouth."

                    bro "Maybe don’t try to speak. Or move. Or help."

                    "You experience a sinking feeling that could be related to your diminishing odds of impressing Bronya and becoming her friend, or it could be the compression of all your internal organs."

                    "Either way, it’s tough to feel optimistic right now."

                    "But before you can give in to complete despair, you hear other voices."

                    "Your view is blocked by the mass of bison flesh on top of you, but could it be? Are these other people here to save you?"

                    bro "Finally! I was wondering where you all had gotten off to."
                    bro "vV Let’s all work together girls! Vv"
                    bro "1. You two grab his horns to keep the head still and keep it from biting anyone.{p}2. The rest of you, come around with me to its backside so we can push it without getting kicked."

                    "You hear some grunting and muttering and the bison starts making noises that sound more confused and less furious."

                    "The pressure and pain on your chest briefly spike in intensity as the thing’s weight shifts, and then they must succeed in dragging it off you because suddenly you can breathe again."

                    hide blackcover
                    hide bison
                    show bg cave at shaking
                    show bronya um
                    with dissolve

                    "But the crisis is not yet over. While you’re still testing the use of your lungs and blinking up at the cavern ceiling, you hear a new cacophony of enraged monster noises."

                    bro worried "Uh-oh. The other lusii are still agitated."

                    show bronya duty at bounce

                    bro "vV Get down there and try to calm them down! Protect the Mother Grub! Vv"

                    "You try to lift yourself to see what’s going on, but putting any weight on your arms makes you feel like maybe all your bones got turned to confetti. Painful, painful confetti."

                    show bronya mom

                    "You feel strong hands propping you up gently, and now your head is in Bronya’s lap."

                    "You try to focus more on how this is a nice place for your head to be and less on the pain."

                    bro worried "This is not good. I don’t know if my jades can reach the stampede in time and the Mother Grub could get injured. Not to mention all these wigglers in danger!"
                    bro "Oh no..."

                    "You didn’t think this situation could get any worse, but now you see that several of the Imperial Drones that had been about to leave the cavern are turning back, drawn by all the noise and chaos."

                    "But maybe this could be a good thing? Maybe they can instill some order?"

                    bro panic "Fuck! They’re going to kill everyone!"

                    show bronya duty

                    with vpunch

                    "She scrambles to her feet, in the process letting your head whack down on the cave floor."

                    if persistent.flash:

                        with Fade(0.14, 0.02, 0.14, color="#ffcc00")
                        with Fade(0.14, 0.02, 0.14, color="#ffcc00")

                    "Your vision swims, but you can still make out the Drones firing indiscriminately: at the lusii, at the grubs and wigglers, and at the jadebloods."

                    if persistent.flash:

                        with Fade(0.14, 0.02, 0.14, color="#ffcc00")

                    with vpunch

                    "One laser beam skims the side of the Mother Grub’s massive midsection and her scream is so loud that the ceiling shakes and a few stalactites shake loose, falling on drones and lusii and wigglers alike."

                    show bronya panic at bounce

                    if persistent.flash:

                        with Fade(0.14, 0.02, 0.14, color="#ffcc00")

                    with hpunch

                    "It’s a total catastrophe. A whole rainbow’s worth of troll, wiggler and lusus blood is splattering the cavern walls."

                    with vpunch

                    "Bronya seems paralyzed by the chaos, looking from her jades to the Mother Grub to the imperilled wigglers like she’s not sure who to help first."

                    show bronya at lowered

                    bro "I can’t believe it. This is the worst disaster we’ve ever had down here!"
                    bro worried "And all because I thought I could sit back and let someone else be responsible for once..."
                    bro "If I were a less secure person, I could let this moment plant a seed of self-doubt in my mind about my ability to take care of others and do my job well."
                    bro angry "Or I could chalk it up to you being really fucking stupid."

                    "You shrink under the weight of her glare. She’s green in the face from how angry she is."

                    "You swallow and manage to spit out enough blood to ask a question that you already know is hopeless: does this mean you can’t be friends?"

                    bro "Are you serious right now?"

                    show bronya duty at bounce

                    bro "vV I do NOT make friends with anyone who recklessly endangers the trolls and wigglers under my care! Vv"

                    call ending ("gameover bronya2", False, True) from _call_ending_13

                    return
                "Be a weeny.":


                    "You definitely do not like the idea of wading into a monster fight, not even to save the progenitor of your new friend’s species."

                    "In fact, you don’t like that Bronya is so focused on protecting all these helpless toddlers and distressed animals instead of taking care of you."

                    "You stammer out that you don’t think you can take on any kind of monster right now. In fact, you just felt another stab of pain in your ribs. You might be blacking out..."

                    show bronya worried

                    "Bronya’s concerned face turns in your direction as you start to swoon. She catches you before you hit the ground, and your heart flutters."

                    "You look up at her serious face and she looks like such a mom, but also such a friend, like some sort of combination of these two concepts."

                    bro "Yikes, you don’t look so good."
                    bro um "I can’t leave you alone, not when you’re in such bad shape. Hmm."
                    bro "Maybe I could carry you on my back while I try to stop the rampaging lusus?"

                    "Your heart flutters turn to pinpricks of alarm. That sounds dangerous, mainly for you."

                    "You try to think of what you can say to dissuade her. Something other than ‘I think you should ignore the helpless babies and mother in danger behind you in favor of continuing to hold me in your strong arms.’"

                    "But before you can speak, you hear a commotion behind her. She turns to look over her shoulder, and her face sags with relief."

                    bro mom "Yes! The other jades are here!"
                    bro "They should know what to do. We’ve taken care of crises like this before. Of course, usually I’m there to help..."

                    hide bgbison with dissolve

                    "If you crane your neck, you can just glimpse a crowd of trolls corralling the rogue lusus away from the Mother Grub, while other trolls calm the remaining lusii and swoop up any wigglers in harm’s way."

                    bro talk "It looks like I needn’t have worried. They’re more than capable of stepping in while I’m otherwise occupied."

                    show bronya mom at nod

                    bro "I’m so proud!"

                    "You take this opportunity to compliment her on what a good leader she must be, to have trained the others so well. Super smooth."

                    "She beams at you and sets you down carefully on the cavern floor, kneeling at your side."

                    bro talk "This could have gone quite badly. I’m glad I didn’t make the wrong choice when I stayed to help you instead of rushing off."

                    show bronya happy at bounce

                    bro "vV It just goes to show, sometimes the best thing you can do for the group is take care of the weakest person in it! Vv"

                    show bronya talk

                    "You kind of want to object to being called the weakest person, but you did just fake a fainting spell for attention, so maybe now isn’t the best time. Instead, you thank her sincerely for sticking by your side."

                    "The two of you watch together as order is gradually restored to the chaos below, and even with your injuries, you feel close to content and quite hopeful about how this relationship is progressing."

                    "You notice that at your side, several wigglers are blindly squirming around, confused and crying. There are some young trolls here, too, looking around all lost and bereft."

                    "You’re not sure if their lusii ran off with the others that got involved in the fracas, or if these little guys are orphans now."

                    "Now that you’re seeing them out in the natural cavern light, the wigglers look less like maggots to you. In fact, they’re even kind of cute. You can see why Bronya would want to take care of them."

                    "One of the smallest wigglers closest to you has somehow flipped himself over onto his back and seems unable to right himself, his little legs waving in the air while he cries."

                    "Trying to be careful with your ribs, you reach out to scoop him up and cradle him to your chest, rocking him back and forth until his cries quiet down."

                    bro mom "Wow, you have a very strong nurturing instinct. I think he likes you."
                    bro "You almost look like you could be his lusus. Or a jadeblood."

                    "You are pleased that she approves of your caretaking display."

                    "The wiggler’s cough breaks through your haze of smug satisfaction, and when you look down you realize that he seems to be having some trouble breathing. You point this out to Bronya."

                    bro talk "Good observation. You really are a natural at taking care of other creatures, aren’t you?"
                    bro mom "Some people find that nurturing ability to be very attractive in a potential friend."
                    bro um "But as for the wiggler, this is definitely not a good sign. I’m surprised none of these drones have noticed that he’s sick."
                    bro worried "If we leave him here, he’ll be culled for sure."

                    "Bronya takes the wiggler from you, and you’re more than happy to hand him over considering that you have no idea what to do with a sick baby that’s not your species."

                    "Also, your broken ribs make holding a baby kind of painful, and Bronya holds the wiggler carefully but with perfect ease. Just like you hope she’ll cradle your new friendship in its infancy."

                    show bronya mom

                    show bg nursery with wipeup

                    "Once Bronya feels assured that her jades have the situation at the brooding caverns under control, you both take the wiggler back to the jadeblood nursery."

                    "You hover around uselessly while Bronya sets up some kind of crib filled with green slime."

                    "You’re a little concerned when she takes the wiggler and submerges him under the slime, because like... he was already having trouble breathing? Surely drowning in slime won’t help?"

                    bro "The sopor should help strengthen his bellowsacs and soothe his sorrow chute."
                    bro talk "When he gets healthy again, I’ll take him back to the cavern and set him free to make his cocoon and pupate."
                    bro worried "But he’s so small... it’s unlikely that she’ll survive the trials, or be selected by a lusus..."

                    "You hate to see Bronya looking sad. You try to be sympathetic, mentioning your astute observation that this whole system set up with the wigglers and the trials and the culling seems pretty brutal."

                    show bronya panic at bounce

                    bro "What? Oh, no. I would never suggest..."
                    bro worried "This is just the way the world works. And it’s fine. It’s fine!"
                    bro "The trials are how young trolls prove that they’re strong enough to survive. It’s only right for the weak to be culled."

                    show bronya happy at bounce

                    bro "vV It’s the purpose of jadebloods to ensure the continuation of our species! And consequently, the hemospectrum! Vv"
                    bro worried "1. We are not revolutionaries.{p}2. We’re meant to do our jobs, and keep our heads down, and keep things running smoothly."
                    bro "3. I would never presume to question the basic tenets of Alternian society. That would bring negative attention from the highbloods, and I just want to keep my jades safe."

                    "You look around at the nursery, and all these injured or underdeveloped wigglers that Bronya was apparently supposed to let die."

                    "You think it might not be true that she doesn’t question the way her world works. She’s looking at you like she’s scared you’ll call her on it and expose her altruistic tendencies."

                    "You try to salvage this conversation thread. Did you say that culling wigglers sounded brutal? You meant... neutral!"

                    "Yes, you feel 100 percent neutral on this topic, neither committed to the culling side of things nor eager to take up arms in revolution."

                    bro um "Ah yes. Neutral is how I feel about it as well. What a good word to describe exactly how I feel about all controversial political subjects."
                    bro worried "Did I mention that keeping this nursery isn’t technically illegal? Because it isn’t. Technically."

                    show bronya happy at bounce

                    bro "vV There is no reason for any of Trizza’s drones to come investigating our hive! And if any drones do come knocking, we have nothing to hide. No borderline-revolutionary ideas will be tolerated within these walls! Vv"

                    show bronya worried

                    "Bronya laughs nervously and looks around the room, like she’s making sure that any Imperial Drones hiding in here heard her announcement."

                    "You feel bad for how nervous she is. You didn’t mean to freak her out."

                    "You tell her that she sounds super convincing. And why shouldn’t she, because she’s clearly telling the truth!"

                    "If you were an Imperial Drone, you would definitely be satisfied right now with her clearly law-abiding and neutral ways."

                    bro mom "Thank you. That means a lot."

                    "You cast about for something to change the subject, and mention that your ribs are feeling a bit better."

                    show bronya talk

                    "Bronya’s face brightens, and she lifts up your arm gently so she can touch the injured part of your torso, examining it in her typically responsible and authoritative way."

                    "You shiver and wonder if her touch has healing properties."

                    bro mom "I’m glad to hear that. After all, I don’t like it when my friends suffer."

                    "Your heart leaps. You look up, scarcely allowing yourself to hope. Could it be? Or was she just making a general statement?"

                    bro talk "If you’re not in any more pain, hopefully that means your injuries will heal soon. I’ll take care of you until then, {i}my friend{/i}."

                    show bronya mom

                    "You are overcome. Your eyes fill with tears. Bronya smiles at you, and squeezes your hand."

                    call ending ("win bronya", True, True) from _call_ending_12

                    return

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
