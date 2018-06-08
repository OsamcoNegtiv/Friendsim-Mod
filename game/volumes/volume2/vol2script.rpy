





define ami = Character("AMISIA", color='#FFFFFF', image="amisia", window_background="gui/textbox_blue.png", who_outlines=[ (4, "#000056") ],)
define cir = Character("CIRAVA", color='#FFFFFF', image="cirava", window_background="gui/textbox_gold.png", who_outlines=[ (4, "#a1a100") ],)

image amisia = "volumes/volume2/images/amisia.png"

image amisia pull = "volumes/volume2/images/amisia_hairpull.png"
image amisia doubt = "volumes/volume2/images/amisia_doubt.png"
image amisia fingers = "volumes/volume2/images/amisia_frame.png"
image amisia growl = "volumes/volume2/images/amisia_growl.png"
image amisia jumping = "volumes/volume2/images/amisia_jump.png"
image amisia nya = "volumes/volume2/images/amisia_nya.png"
image amisia ponder = "volumes/volume2/images/amisia_ponder.png"
image amisia smile = "volumes/volume2/images/amisia_smile.png"
image amisia happy = "volumes/volume2/images/amisia_smile2.png"
image amisia smug = "volumes/volume2/images/amisia_smug.png"
image amisia axe = "volumes/volume2/images/amisia_axe.png"
image amisia confess = "volumes/volume2/images/amisia_confess.png"

image cirava angst = "volumes/volume2/images/cirava_angst.png"
image cirava cross = "volumes/volume2/images/cirava_cross.png"
image cirava feeling = "volumes/volume2/images/cirava_feelingit.png"
image cirava peace = "volumes/volume2/images/cirava_peace.png"
image cirava point = "volumes/volume2/images/cirava_point.png"
image cirava shrug = "volumes/volume2/images/cirava_shrug.png"
image cirava smile = "volumes/volume2/images/cirava_standing.png"
image cirava talk = "volumes/volume2/images/cirava_talk.png"
image cirava vape = "volumes/volume2/images/cirava_vape.png"

image blurred amisia = "volumes/volume2/images/amisia_blur2.png"

image redcircle = "images/redcircle.png"
image vape = "volumes/volume2/images/vape.png"
image high1 = "volumes/volume2/images/high1.png"
image high2 = "volumes/volume2/images/high2.png"
image red = "#FF0000"

image statue = "volumes/volume2/images/statue.png"
image aesthetic = "volumes/volume2/images/aesthetic.png"
image horse = "volumes/volume2/images/hors.png"

image bg studio = "volumes/volume2/images/bg_amisia_studio.png"
image bg ciravablock = "volumes/volume2/images/bg_ciravablock.png"
image bg ciravastream = "volumes/volume2/images/bg_ciravastream.png"
image bg spotlight = "volumes/volume2/images/spotlight1.png"

image spotlight = "volumes/volume2/images/spotlight2.png"
image makeover1 = "volumes/volume2/images/u_cooler.png"
image makeover2 = "volumes/volume2/images/u.png"

image win cirava = "volumes/volume2/images/cirava_win.png"
image win amisia = "volumes/volume2/images/amisia_win.png"

image gameover cirava1 = "volumes/volume2/images/cirava_lose1.png"
image gameover cirava2 = "volumes/volume2/images/cirava_lose2.png"
image gameover amisia1 = "volumes/volume2/images/amisia_lose1.png"
image gameover amisia2 = "volumes/volume2/images/amisia_lose2.png"

define closeeyes = ImageDissolve("eye.png", 0.8, ramplen=128, reverse=True, time_warp=eyewarp)

define openeyes = ImageDissolve("eye.png", 0.8, ramplen=64, time_warp=eyewarp)
define openeyesaxe = ImageDissolve("eye.png", 1.4, ramplen=64, time_warp=eyewarpaxe)

transform blurstart:
    alpha 1.0 xalign 0.5 yalign 1.0
    easeout 1.2 alpha 0
    pause 1.5
    easein 1.2 alpha 1.0
    pause 0.8
    easeout 1.2 alpha 0
    pause 1.5
    easein 1.2 alpha 1.0
    repeat

transform blurend:
    alpha 0.0 xalign 0.5 yalign 1.0
    easeout 1.2 alpha 1.0
    pause 1.5
    easein 1.2 alpha 0.0
    pause 0.8
    easeout 1.2 alpha 1.0
    pause 1.5
    easein 1.2 alpha 0.0
    repeat

transform beingcarried:
    easeout 0.60 zoom 1.6 ypos 1000
    pause 0.5
    easein 0.45 zoom 2.2 ypos 1125

transform beingsetdown:
    ypos 1125
    easein 0.45 zoom 1.6 ypos 1000
    easeout 0.60 zoom 1.0 ypos 720

transform easefade:
    linear 0.8 alpha 0.96
    easeout 0.25 alpha 0.0

transform bloodalpha:
    alpha 0.0
    linear 70.0 alpha 1.0

transform bloodzoom:
    zoom 1.5 xalign 0.5 yalign 0.5 alpha 0.2
    linear 70.0 zoom 1.0 alpha 1.0

transform amizoom1:
    linear 0.35 zoom 2.4 ypos 1150

transform amizoom2:
    linear 0.35 zoom 2.6 ypos 1200

transform amizoom3:
    linear 0.35 zoom 2.8 ypos 1250

transform theincident:
    zoom 1.3 ypos 850

transform calloutzoom1:
    zoom 1.2 ypos 820

transform calloutzoom2:
    zoom 1.35 ypos 860

transform calloutzoom3:
    zoom 1.5 ypos 900

transform calloutzoom4:
    zoom 1.65 ypos 940
    block:

        ypos 940
        linear 0.07 ypos 938
        linear 0.07 ypos 940
        repeat

transform redoverlay1:
    alpha 0.1

transform redoverlay2:
    alpha 0.2

transform redoverlay3:
    alpha 0.3

transform redoverlay4:
    alpha 0.4



transform highanim1:

    alpha 0.0
    linear 5 alpha 0.3
    block:

        alpha 0.3
        easeout 1.8 alpha 0.0
        pause 2.0
        easein 1.8 alpha 0.3
        pause 2.0
        repeat

transform highanim2:

    alpha 0.0
    linear 5 alpha 0.0
    block:

        alpha 0.0
        easeout 1.8 alpha 0.3
        pause 2.0
        easein 1.8 alpha 0.0
        pause 2.0
        repeat

transform floaties1:

    alpha 0.0 align (-0.2, 1.1) rotate -40

    parallel:

        easeout 4 alpha 0.4
        pause 2
        easein 4 alpha 0.0
    parallel:


        linear 10.0 align (0.8, -0.25) knot (.66, .9) knot (.4, 0) rotate 35

    pause 28
    repeat

transform floaties2:

    alpha 0.0 align (-0.1, -0.25) rotate 25

    pause 14

    parallel:

        easeout 4 alpha 0.4
        pause 2
        easein 4 alpha 0.0
    parallel:


        linear 10.0 align (0.25, 1.3) knot (.4, .7) knot (.3, .66) rotate -10

    pause 14
    repeat

transform floaties3:

    alpha 0.0 xpos 900 ypos 225

    pause 28

    parallel:

        easeout 4 alpha 0.4
        pause 2
        easein 4 alpha 0.0
    parallel:


        easein 2.5 ypos 75
        easeout 2.5 ypos 225
        easein 2.5 ypos 75
        easeout 2.5 ypos 225
    parallel:


        linear 10.0 xpos 200

    repeat

label volumetwo:

    $ renpy.block_rollback()

    $ main_menu = False

    show expression "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)

    op "You stumble through the streets of a strange alien world."

    op "Ever since you crash landed on this hostile planet, you have been desperate."

    op "Desperate for information, for provisions, and possibly for a bit of medical attention."

    op "Along the way you’ve had some laughs, embarrassing missteps, and maybe even an encounter with alien meat products? You don’t really want to get into it."

    op "What you do want to get into is... "

    op "{size=80}{=friend}FRIENDSHIP.{/=friend}{/size}"

    op "An entire planet of endless friend opportunities awaits you."

    op "Honestly, at this point you’d make friends with one of those weird purple bushes. You’re not picky."

    op "Wait. You see something, in the distance. Or perhaps... Someone?"

    call screen troll_select2 with Dissolve(1.0)

    with Pause(0.25)

    return

label amisia:

    $ renpy.block_rollback()

    scene black with Dissolve(1.0)

    scene bg alternia with dissolve

    $ quick_menu = True

    "Lo, what light through yonder weirdly organic architecture breaks? A small figure approaches."

    window hide

    play music "volumes/volume2/music/amisia_loop.wav" loop

    show amisia nya with moveinbottom

    ami "oh."

    ami "oh my gosh."

    show amisia ponder at lowered

    ami "youu are so..."

    "So far you’ve swallowed quite a few insults in regards to your looks and intelligence level. You aren’t really the type to let the shallow opinions of others get you down, but it’s been kind of a rough day. You brace yourself."

    show amisia happy at bounce

    ami "cuute!"

    "Oh. OH."

    show amisia smile

    "She gives you a sweet, sincere smile."

    ami "i’ve never seen anything like youu"

    ami fingers "it’s giving me all sorts of new ideas!"

    "Boy do you hope some of those ideas are about FRIENDSHIP. Now that you’ve got a taste of it you are hungry for more."

    "You take a stumbling step forward and your ribs remind you that the although the potential of camaraderie is enough to improve your mental health, it can’t cure acute injuries."

    ami doubt "oh..."

    ami "youu don’t look so good"

    ami nya "come inside!"

    ami "i’ve been looking for new contribuutors!"

    "Contributors? Could she mean... friendship contributors? No, that’s dumb."

    "Maybe she runs some sort of alien newspaper and she wants you on staff. She looks a little young for that, but what the heck do you know about alien management hierarchy?"

    "You follow her to a nearby building, and now that you’re looking up from your ravenous hunt for companionship you notice that you’ve wandered into kind of an upscale part of town."

    "There’s a lot less garbage and people collapsed in the street. You see one of those spiky robot things, but it’s washing a window instead of shooting a laser at a group of children. If that’s not high class you don’t know what is."

    "Before you can follow her inside she turns around in the threshold, blocking your way."

    ami ponder "real quuick"

    ami "you don’t happen to be an artist"

    ami "do youu??"

    "Artistry? Well, as a matter of fact..."

    menu:
        "Artistry? Well, as a matter of fact..."
        "[pick] Tell her yeah, it isn’t exactly your whole deal but you’ve been known to dabble.":



            ami growl "{i}oh.{/i}"

            ami "i see how it is"

            ami smug "well youu aren’t going to snake-rodent any trade secrets ouut of me!"

            ami growl "goodbye!"

            call ending ("gameover amisia1", False, True) from _call_ending_2

            return
        "[pick] Tell her no, you’ve never had much of a knack for it.":


            ami happy "oh good"

            ami nya "friendships between artists can be so frauught"

            ami "muuch better to juust keep things between artists and art appreciators"

            show amisia happy at bounce

            ami "that way no one can get jealouus!"

            "The girl’s smile widens even further and you feel an unbelievable rush of joy. Have you finally found someone who isn’t a total fucking maniac?"

            "And she brought up friendship without you having to mention it at all! It puts a spring in your step. Or as much of a spring as possible with a broken arm and misaligned torso."

            show amisia smile

            "Amisia leads you into an elevator with buttons labeled in spiky letters that make absolutely no sense to you. You realize that probably nothing is ever going to make sense to you again."

            "That’s okay. Your hierarchy of needs has adjusted, recently."

            "Your new friend (you are jumping the gun with this descriptor but you are feeling seriously good about this encounter) stands in the corner of the elevator, wringing her claws."

            ami doubt "i wish i’d known i was going to have company"

            ami "i wouuld have cleaned up a little"

            ami ponder "it’s been a while since i’ve met anyone new"

            "You assure her that whatever disaster her house is it can’t be any worse than some other places you’ve seen here."

            show amisia smile

            "Although you kind of get what she means; she’s wearing an artist’s smock that’s covered in splashes of paint."

            "Actually... it doesn’t really look like paint. But it couldn’t be anything else, could it? It’s every color of the rainbow."

            show bg studio with wipeleft

            "The elevator door slides open and you step into a space that you are relieved to find is totally recognizable."

            "A table overflows with messy palettes and brushes, cloudy jars of water, and sponges. Several easels stand beside the windows to catch the light of the two moons, and a number of canvases lean against the wall, turned so you can’t see what’s on them. "

            show amisia nya at bounce

            ami "first things first!"

            "Amisia brings you over to a wallscreen that looks way more high-tech than anything you have on your now defunct spaceship, tapping away at a series of unreadable symbols. She then indicates you should take off your sling."

            ami smile "here."

            ami "go ahead and stick it in there!"

            "She seems to want you to put your injured arm into a large hole in the wall, which you do, because you are sure your new friend has your best interests at heart."

            with vpunch

            "The hole shrinks down like a blood pressure cuff, sending bolts of agony through you."

            show amisia doubt with vpunch

            "You want to yank your arm back out but you don’t. Even if it’s broken you still like having it attached to you. Instead you shout a lot and thrash your other limbs around."

            ami growl "calm down youu big wriggler!"

            ami "it’s like youu’ve never seen a medicalizer before!"

            ami doubt "if youu don’t stop moving it won’t work!"

            "Tears spill down your cheeks but you force yourself still. You’ll bear the pain. You’ll do it for your friend."

            show amisia smile

            "She’s looking at you so hopefully, and she’s so delicate and pretty, almost angelic. You look at her face and tell yourself it’s all going to be okay."

            "Finally the hole releases you and you pull your arm back out to find it... completely healed. You can move your fingers. It doesn’t even hurt anymore. Hey, things are looking up!"

            show amisia happy at bounce

            ami "see"

            ami "i told youu!"

            "This is great! You are overwhelmed with the urge to celebrate."

            menu:
                "This is great. You are overwhelmed with the urge to celebrate."
                "[pick] Be chill about it.":



                    "You thank Amisia profusely but you manage to keep it to the strictly verbal sort."

                    "Medicalizers are great! This part of the city is great! You really need to get more rich friends."

                    "You tell her this, throwing in a compliment of her studio while you’re at it. See? This friendship stuff is easy."

                    ami smile "ahahaha i’m glad youu feel that way"

                    ami "youu’re obviouusly really strange and uunder-socialized"

                    ami smug "buut youu don’t seem to be a complete cuultuural idiot"

                    ami nya "pluus i think it’s really endearing how helpless and truusting youu are "

                    "You laugh, slightly unnerved. You want to take that as a compliment, but after a recent encounter with another girl in blue..."

                    "Well. It all ended up okay. And Amisia is so nice and friendly, and she keeps calling you cute, which you think is pretty generous of her considering what a disgusting mess you are at this point."

                    ami ponder "speaking of lowbloods"

                    ami "what’s youur blood color??"

                    ami nya "juust ouut of cuuriosity"

                    "Blood color? You aren’t really sure what she’s talking about... but... red? You tell her it’s red. She looks a little disappointed."

                    ami ponder "i’ve got plenty of buurguundy"

                    show amisia happy at bounce

                    ami "oh well"

                    ami "good thing i have a delivery coming soon"

                    ami smile "hey do you think youu can help me set a few things uup before they get here?"

                    "They? Visitors? As in, plural? As in multiple potential friends? Oh hell yes."

                    "You are all over that, especially considering your newly-healed arm. You are anxious to display all the simple motor functions you can perform."

                    "Amisia gives you another radiant smile. You live for those smiles, man. They are just so full of the glowing nectar of bromance."

                    show amisia happy at bounce

                    ami "perfect!"

                    ami smile "lets do this"

                    ami "work always goes faster with two pairs of hands after all"

                    "Yes, absolutely it does. And even if by that she seems to mean her hands are pointing while she tells you where to put things, you’re totally fine with that."

                    "Your ribs are still kind of killing you but you swallow down the pain. You are getting pretty good at that."

                    "Too bad you can’t stick your whole torso into that magical science fiction hole in the wall. Well, maybe you could. But not right now. Right now you’ve got a friend to help."

                    "Amisia instructs you to clear all the furniture to the edges of the room and lay down a big purple tarp. Apparently tarps aren’t blue on this planet."

                    "Amisia answers her phone, and then buzzes open the apartment door. She runs over to the elevator with a squeal of delight."

                    show amisia happy at bouncing

                    ami "they’re here!"

                    show amisia smile at default

                    ami "sorry i’m getting so giggly abouut this"

                    show amisia nya at bounce

                    ami "it’s juust been awhile since i’ve had any new paints"

                    "Wait, paints? That’s what’s coming?"

                    "Now that you think about it, there is something pretty crucial missing from this whole artist aesthetic she’s got going here. There aren’t any paints."

                    "No tubes dribbling color or pots with their tops left partially unscrewed. There aren’t even any pencils."

                    "The elevator opens and two trolls come in. They have pretty similar shaped horns and are almost the exact same height. Brothers? Do trolls have brothers?"

                    "From their uniforms and the douchey, swaggering way they walk you get the idea that they are some sort of law enforcement."

                    "That, and the third troll in handcuffs they are dragging between them."

                    show amisia happy at bounce

                    ami "thank youu guuys!"

                    ami smile "youu always bring me the best materials"

                    "They don’t say anything. They just bring the third troll to the center of the tarp and force them into a kneeling position. Then they bow to Amisia and leave the way they came."

                    hide amisia with moveoutright

                    show amisia axe with moveinright

                    "This doesn’t look great. Even before Amisia runs out of the room and comes back in with an axe the size of her whole body. You are not loving this."

                    "The troll on the tarp trembles and bites back a sob, but they don’t say anything or try to run."

                    "She... isn’t really going to do what it looks like, is she?"

                    "You can’t bring yourself to believe that this cute little alien girl is going to straight-up axe-murder a dude right in front of you. Presumably to finger paint with their blood."

                    "You stammer something to this effect. Amisia laughs."

                    ami nya "well i don’t uuse my fingers"

                    ami smug "i’m not a fuucking animal"

                    show amisia ponder

                    "She considers you for a few moments, tapping a claw against her mouth."

                    show amisia happy at bounce

                    ami "i know!"

                    ami "youu can help me!"

                    ami doubt "i only ever let one other person help with my work"

                    ami "and she’s ouut of town right now"

                    ami smile "buut youu and i have a connection"

                    ami nya "youu feel it too"

                    ami "right?"

                    "You do. God, you do. You’ve been feeling it so much lately, for everyone you meet. You thought you had maybe come across someone who would readily accept your platonic longings without putting you through the ringer first."

                    ami "youu do want to help me"

                    show amisia nya at bounce

                    ami "don’t youu?"

                    "You do. You want that more anything. Amisia looks at you solemnly."

                    ami axe "why don’t youu do the honors."

                    "She holds out her axe."

                    ami "i wouuldn’t offer this to juust anyone"

                    ami "buut i can tell how special youu are"

                    "You’re trembling. The troll on the tarp is also trembling, but unlike you they seem to have accepted their fate."

                    "Slowly, inevitably, you hold out your hand for the axe. Amisia gives it to you with a smile."

                    show amisia nya with vpunch

                    "Goddamn it. You forgot about your broken ribs. And that you’re a human and can’t just pick up gigantic fucking axes with one hand. You drop it and it bounces away from you, like, way more than you think an axe should probably bounce."

                    show amisia happy

                    "You look up at Amisia from where you are doubled over with pain and shame."

                    show amisia axe at bounce

                    "She laughs and scampers over to retrieve the axe, once again swinging it up without any signs of strain. She doesn’t even have any visible muscles. What is this girl made out of?"

                    ami "how silly of me!"

                    ami "youu seem so cuultuurally advanced that for a second i forgot abouut your natuural inferiority"

                    ami "here"

                    ami "i’ll give youu a second chance"

                    "You nod. Yes, please. A second chance that does not include committing gruesome murder."

                    ami ponder "uusuually i just uuse chains"

                    ami nya "buut i’ve got a better idea"

                    "Oh. Oh god. You get what she wants you to do. You hesitate and Amisia’s smile gets even sweeter. Sweet like poison."

                    ami smile "oh?"

                    show amisia smug at bounce

                    ami "youu {i}don’t{/i} want to help me?"

                    "The tarp crinkles underneath you as you kneel. You grasp the troll’s shoulders and mumble an apology. They continue to say nothing. Amisia is sharpening her axe, which already looks pretty damn sharp."

                    ami axe "hold on tight"

                    "You try. You really do!"

                    with hpunch

                    "The problem is, you try to hold on tight but at the same time you try to drag the troll out of the way, some buried instinct to try to preserve life rising up inside you."

                    "You’re weak and injured, though, so all you end up doing is just flopping both of you a little to the side."

                    show amisia growl

                    show oliveblood with olivestab

                    "Instead of coming down on the neck in a clean slice, Amisia’s axe glances off the troll’s collarbone, mortally wounding them instead of killing them outright."

                    "And now you know why they have not been begging for their life. They don’t have a tongue. So they can’t beg, but they sure can yell. And thrash. And bleed olive green alien blood all over you and the tarp."

                    "God. There’s so much blood. It’s just spurting everywhere."

                    "Jesus christ, you are such an idiot. Why couldn’t you just commit?"

                    show amisia pull at dogagony

                    "Now you’re covered in dying alien and so is everything else. Amisia, the work table, and most direly, the canvasses leaning against the wall. Amisia takes one look at them and lets out a wail of rage."

                    show amisia pull at default with move

                    ami "i can’t believe this!"

                    show amisia pull at bounce

                    ami "i let youu into my hive!"

                    show amisia pull at bounce

                    ami "into my life!"

                    show amisia pull at bounce

                    ami "i was planning to let youu into my puusher!"

                    ami "i thouught youu were a refined sophisticate"

                    ami "buut now i see youu’re just..."

                    show amisia pull at bounce

                    ami "a philistine!"

                    show amisia growl

                    "She gives you a shove toward the elevator. Your ribs are screaming and so is the bleeding troll. You try to babble an explanation."

                    show amisia growl at bounce

                    ami "forget it!"

                    ami "i don’t want to hear youur excuses"

                    ami "chahut was right!"

                    show amisia pull at bounce

                    ami "if youu want someone killed right youu have to kill them yourselves!"

                    hide amisia with moveoutright

                    "You ride the elevator back down, kneeling in a pool of blood and failure."

                    call ending ("gameover amisia2", False, True) from _call_ending_3

                    return
                "[pick] Get excited and dance your new friend around the room.":


                    "You try to resist the urge to celebrate."

                    "You fail to resist the urge."

                    ami nya "uum!"

                    "You take Amisia by her tiny hands and twirl her around the studio. Or you try to. You forgot about your busted ribs. You sure are doing that a lot!"

                    with vpunch

                    "You let go of Amisia and go careening into one of the tables. Thankfully, not the one covered in art supplies. You hit the corner and go down onto your already incredibly sore ass."

                    "This is what you get for acting like a huge fucking tool in front of your new friend."

                    ami doubt "are youu okay?"

                    ami ponder "was that some sort of rituualistic rite of healing i’ve never heard of before?"

                    "You shrug against the floor."

                    show amisia smile at beingcarried

                    "Amisia leans down and picks you up in a bridal carry, despite the fact that she’s about half your size. It makes your ribs hurt, but what doesn’t nowadays."

                    show amisia smile at beingsetdown

                    "Amisia lays you down on a weird lumpy couch."

                    ami doubt "are youu suure youu’re okay?"

                    ami "youu look a little..."

                    "She trails off to nothing. She’s looking at your left arm, which you have draped over yourself awkwardly to sort of try to hold your torso together."

                    ami nya "that color"

                    "At first you think she means the color of your skin, which is different than her light grey. Then you think she means the truly fantastic buffet of bruises you got going on."

                    "But {i}then{/i} you realize that in your prancing idiocy you’ve managed to scrape up the inside of your arm. Blood oozes sluggishly from the wound."

                    "Amisia dredges a finger through it. You’re half expecting her to put it in her mouth and for this to become a whole cannibal situation. Well, since you aren’t the same species it wouldn’t really be cannibalism but still. No thanks."

                    "Instead Amisia just holds her finger up, the drop of blood trembling on the tip."

                    ami "this color"

                    ami fingers "i’ve never seen anything like it!"

                    "She dashes off to one of her tables, pulling over a sketchbook and dragging her finger down it. Your blood paints a rusty line down the center. She lets out a little squeak of excitement."

                    ami nya "this is..."

                    show amisia happy at bounce

                    ami "amazing!"

                    "What, red?"

                    ami "not red!"

                    ami smug "there’s a million dirty little ruusties swarming all over this city"

                    ami "i’m drowning in red!"

                    ami doubt "this is..."

                    show amisia happy at bounce

                    ami "crimson!"

                    ami nya "it’s incredible"

                    ami "you muust be some sort of muutant"

                    ami happy "youu’re really luucky i found youu instead of one of the drones!"

                    "Lucky? You? Ha. Haha. Yes. Very lucky. The luckiest."

                    "... Though your arm is healed and you’re out of whatever doubtlessly weird weather happens on this planet. Maybe Amisia’s right. Maybe you are lucky."

                    show blackcover with closeeyes

                    "You close your eyes and try to breathe. Zen yourself out. Really center yourself in your own body and all that garbage."

                    show amisia axe

                    hide blackcover with openeyesaxe

                    "Then you open your eyes and wow you sure aren’t centered anymore."

                    "In fact you roll completely to the left as you try to get away from Amisia, who is back and standing over you with a gigantic axe."

                    ami "watch ouut!"

                    "Amisia grabs you, drags you back up onto the couch and plants her hand on your solar plexus, effectively pinning you down."

                    ami "youu’ll huurt youurself if you keep flopping arouund like a beached bluubberbeast"

                    ami "youu want to be friends don’t youu?"

                    ami "youu want to help me with my artistic aspirations, right?"

                    "You get the feeling that she might be trying to manipulate you. Just, the tiniest little suspicion. It’s possible Amisia has recognized your intense craving for companionship and is trying to exploit it."

                    "You don’t like being suspicious of a new friend, but that is a pretty big axe."

                    ami "i don’t know what’s got youu so worried"

                    ami "i juust want to show youu my axe!"

                    "Oh. Of course. Makes sense. It {i}is{/i} a really nice axe."

                    "You hold out your hand for it, but of course it is too heavy for you and your hands are all sweaty and you fumble it. Fumble the really sharp weapon."

                    show amisia growl

                    show redcircle at bloodalpha

                    show bloodborder at bloodzoom with redstab

                    show amisia doubt

                    "Amisia tries to catch it before it’s too late, and somehow in all the wriggly struggle you end up getting cut. Like, very cut. Across both your wrists."

                    "In fact, you don’t think she could have aimed even better if she’d been trying."

                    ami "oh"

                    ami "oh dear"

                    "Hard agree."

                    show amisia doubt

                    show blurred amisia at blurend

                    ami "don't struuggle"

                    ami "youu’ll only huurt youurself more silly"

                    ami "youu don’t want that do youu"

                    "No. You definitely don’t want that. Not after what a butterfingers you’ve proven to be."

                    "Amisia gets up to put the axe down and you kind of lose track of her for a little while. You are bleeding all over her couch and everything around you starts to go shiny and unreal."

                    "She comes back with a couple little jars that she uses to catch your blood. That’s a good idea. You sure are making a mess. You wonder if they are specifically blood jars. They look like jam jars."

                    "Alien jam.{w} Space jam.{w} God, you love that movie."

                    "It’s been so long since you’ve seen it.{w} Definitely the best PG movie about basketball.{w} Way better than the one with the dog and the clown."

                    "Do they even{w} have basketball here?"

                    "You ask Amisia.{w} She just shushes you and brushes your hair back off your forehead. She keeps smiling and saying comforting things.{w} God, she’s such a good friend."

                    "Before too long, you do what it’s honestly a god damn shock you haven’t done before now."

                    scene black with closeeyes

                    "You pass out."

                    scene bg studio with openeyes

                    "When you come to you are propped up against the wall in a weird way that you wouldn’t love even if you weren’t an invalid, and both of your arms are jammed in the hole in the wall."

                    "The med hole. The glory hole of wellbeing. The magic sphincter. You grunt and pull your arms back out. They’re healed. The cuts on your wrists are just two faded pink lines."

                    with vpunch

                    "You take a step away from the wall and immediately hit the ground. You may not be actively dying anymore, but you did just lose like half the blood in your body. Gosh, you’re tired."

                    show amisia nya with moveinright

                    "A little giggle makes you turn around. Or roll over, since you are still on the floor and probably not getting up any time soon. It’s fine. You’ve met worse floors in your life."

                    "Amisia is sitting at one of her easels, her hair pulled back beneath a scarf and little round glasses perched on her nose."

                    "A jar of your blood sits next to her, and as you watch she dips a brush in."

                    ami happy "i’m glad youu’re awake"

                    show amisia doubt at bounce

                    ami "i was a little worried i’d actuually killed you back there!"

                    show amisia happy

                    "She laughs and you laugh along with her. It’s very funny. Actually, everything is funny right now.{w} It’s probably the blood loss."

                    "You ask her what she’s painting."

                    ami smile "youu of course!"

                    ami fingers "youu inspired me!"

                    "Hmm. Well right now it just looks like a bunch of red squiggles and some lines, but she only just got started. She’s warming up."

                    show amisia doubt

                    "She sits there on her stool, looking at her pallette and chewing on her lip thoughtfully. She looks somewhat nervous."

                    ami ponder "actuually..."

                    ami "i want to show youu something"

                    ami nya "something i’ve never shown anyone else"

                    "She leaps up from her stool and crosses the studio. You roll to your other side to keep her in your line of sight. You really hope she isn’t getting another space jam jar."

                    "She starts turning around the canvases one by one. They are all blank. Except for one, which has a little--wait, no. That’s just a shadow. Every single one of them is blank."

                    "You aren’t sure you understand. You ask her if these are all just new canvasses that she has not gotten the chance to paint on yet. Amisia sighs."

                    ami doubt "no"

                    ami "i’ve had them for forever!"

                    ami "i’m juuust..."

                    show amisia confess at bounce

                    ami "not a real painter"

                    ami "there"

                    show amisia pull at bounce

                    ami "i said it!"

                    "She buries her face in her hands, talking from between her fingers."

                    show amisia confess at bounce

                    ami "i’m really good at all the other parts!"

                    show amisia confess at bounce

                    ami "the materials and the stuudio!"

                    show amisia confess at bounce

                    ami "i even make all my own paints!"

                    ami confess "i juust can never do the actuual sitting down and doing art part"

                    "She just looks so despondent. You wish you could do something, but you don’t really know that much about art, and you probably can’t stand up yet."

                    "You tell her that she looks like she’s moving in the right direction, at least. You don’t even have a studio, or any brushes or stuff like that."

                    "Of course you have no aspirations to being a painter, but you leave that part out."

                    ami smile "that’s juust it!"

                    ami "i feel inspired for the first time ever"

                    ami ponder "i think it has to be youur messed-uup, disguusting muutant blood"

                    ami nya "there’s really no other explanation"

                    show amisia smile at beingcarried

                    "She takes a knee beside you, picking up one of your limp hands with hers. They’re cold, like she’s been been pressing them to a glass window in winter."

                    ami nya "uusuually i juust finish off my contribuutors quuickly"

                    ami smug "i don’t have time to deal with a buunch of injuured lowbloods moaning arouund my stuudio"

                    ami nya "buut i couuldn’t juust uuse youur blood uup all at once"

                    ami "youu’re far too special for that"

                    "You gaze at Amisia. A mist has descended over your vision, and it isn’t even the mist of imminent death."

                    show amisia smile at amizoom1

                    ami "i have to keep this preciouus blood safe"

                    show amisia smile at amizoom2

                    ami "i think youu might be..."

                    show amisia nya at amizoom3

                    ami "my muuse"

                    call ending ("win amisia", True, True) from _call_ending_4

                    return

    return

label cirava:

    $ renpy.block_rollback()

    scene black with Dissolve(1.0)

    scene bg alternia with dissolve

    $ quick_menu = True

    "Yes, a potential new friend approaches. And they almost look as messed up as you are!"

    show cirava smile with moveinbottom

    play music "volumes/volume2/music/cirava.wav" loop

    cir "woah what the fuck lmao"

    cir point "you an alien?"

    "You nod enthusiastically. You sure hope your prospective new friend is comfortable with extraterrestrials. Things could get pretty awkward otherwise."

    cir smile "you should really like"

    cir "not be outside lmao"

    cir point "freaks like you will get picked off by drones in a hot second"

    show cirava shrug at nod

    cir shrug "no offense lmao"

    "You don’t like the sound of being picked off by drones. That would really inhibit your companionship plans!"

    "You hastily explain to this strange one-eyed troll that you crash landed on this planet, and are in desperate search of friendship. Your plight seems to move them."

    cir point "well shit"

    cir "if you really dont have anywhere to be"

    cir cross "ugh i promised myself i wouldnt do anything cull-risky"

    show cirava shrug at nod

    cir shrug "but what the hell lmao"

    cir "come with me"

    cir peace "names cirava btw"

    show cirava smile

    "You follow Cirava down a twisting stretch of road. Wow, this is going great already! You bet you’ll have a new friend in no time!"

    show bg ciravastream with wipedown

    cir "alright heres my hive"

    cir talk "you can hide out here for now"

    cir "i got a lot of followers who are pretty into aliens"

    show cirava shrug at nod

    cir "they might get a kick outta this lmao"

    show cirava smile

    "You look around Cirava’s hive in awe. They sure seem to have a batshit crazy taste in home decor!"

    cir talk "checkin out my aesthetic?"

    cir peace "i worked pretty hard puttin this place together"

    cir feeling "its all about the look in the bg when ur streaming lmao"

    show cirava shrug at nod

    cir shrug "dont want my fans to think i live in a fuckin dump and spend most of my days depressed and crying lmao"

    cir "{w=0.4}.{w=0.4}.{w=0.4}."

    cir point "you like moisturewave?"

    menu:
        "[pick] What the fuck is a moisturewave?":


            cir cross "seriously?"

            cir "if you dont even know moisturewave i like"

            show cirava shrug at nod

            cir shrug "cant really see why you would want to be friends with me lmao"

            cir point "cause tbh i dont even know how to explain it to you?"

            cir "you just have to like"

            cir "get it"

            "Cirava considers you for a long moment."

            cir talk "actually yeah"

            show cirava shrug at nod

            cir "this isnt gonna work out"

            cir peace "get out of my hive"

            call ending ("gameover cirava1", False, True) from _call_ending_5

            return
        "[pick] Oh yeah. I love it.":


            "You have no idea what the hell a moisturewave is, but you don’t want to offend your new friend! You tell them you love it."

            cir peace "word"

            cir talk "im actually streaming some chill beats as we speak"

            cir feeling "check it"

            "They gesture toward their strangely bulbous alien computer. On the screen is a GrubTube Channel:{p=0}{p=0} “{image=emoji_peace} LOFI {image=emoji_peace} AESTHETIC {image=emoji_peace} INCUBATED BEATS {image=emoji_peace}”"

            "Wow! They sure have a lot of subscribers! You ask them if they drew that very nice anime girl they’re using as the splash art."

            show cirava shrug at nod

            cir "nah i just ripped it off of some eastern alternian movie and recolored it to look like me"

            cir peace "fuckin nailed it lmao"

            "You nod vigorously. This is very impressive!"

            cir feeling "yea im kind of a big fuckin deal online"

            cir peace "i built up my own streaming empire"

            cir "worked my ass off lmao"

            cir "nursed these beats to health from tragically ill sample loops"

            cir point "its not all fun and games tho"

            cir "the life of a popular online guy"

            cir angst "you cant even imagine the hardships ive gone through"

            cir cross "all in the name of lofi chillhop aesthetic moisturewave beats"

            cir "that shit keeps me up at night"

            "Cirava looks into the middle distance pensively, their one eye filled with poignant emotion. You never knew the life of a streamer could be so vaguely filled with torment. You’re moved to cry a single tear."

            cir talk "yeah"

            cir "you get it"

            cir "youre really vibing on my emotional frequency my dude"

            cir angst "you know you gotta SUFFER for POPULARITY"

            "You nod enthusiastically. You don’t think you’ve ever been particularly popular, but you’re very good at suffering! This is going great."

            show cirava shrug at nod

            cir "sigh"

            cir "i wish i could say more"

            cir point "really get all emotionally vulnerable and share my tragic backstory"

            cir "but ever since..."

            show cirava angst at theincident

            show red at redoverlay3

            cir "the incident"

            hide red

            show cirava cross at default

            cir "its been so hard to trust new people lmao"

            cir "you feel me?"

            "The incident? This is so tantalizing. You just KNOW that if you want to make a new friend, you’re going to have to get them to confess their deepest insecurities and embarrassing secrets to you. That is how friendship works."

            "You place a sympathetic hand on Cirava’s shoulder."

            cir point "you know what dude"

            cir "you really wanna be friends?"

            "Yes. YES! You can’t believe how pain-free and easy this experience has been! What a wonderful new friend you’re about to make! You can practically feel the future bro embraces you two will surely share. They feel good. They feel {i}right{/i}."

            cir talk "haha you sure are eager"

            cir "but like"

            cir point "if were gonna be friends we have GOT to work on your look"

            show cirava shrug at nod

            cir "your aesthetic is basically hot garbage rn lmao"

            cir "my followers cant see me hanging out with a fucking rando like this"

            cir point "im sure you understand"

            "You aren’t quite sure you follow. What’s wrong with your look? You’ve always thought you had a simplistic charm. A face you could put on a logo. You’re not sure if you’re ready to change up the tried and true classics for this newfangled teen."

            "But..."

            "You are so thirsty for Cirava’s sweet friendship nectar. You need to taste it. You HAVE to taste it. With a friend like them, you could really go places. You could BE someone."

            "You could finally be DOWN with the HIP YOUTH of today."

            "You tell Cirava you’re willing to try anything to get into the esteemed ranks of their friend list."

            cir talk "well damn"

            cir point "hold up ive got an idea lmao"

            cir "follow me"

            show cirava smile

            "Cirava leads you up the winding stairs of their hive."

            "Lining the walls are pictures of Cirava in strange poses in several different locations. They are surrounded by a few trolls you don’t recognize, in similar silly fashions. Fellow members of the “moisturewave” community?"

            cir cross "sigh"

            cir "i really gotta take that shit down"

            show cirava shrug at nod

            cir "theyre all dead to me lmao"

            "You want to ask if they mean that literally or not... you never know with trolls! But you keep your mouth shut. Best not to offend your new friend."

            cir cross "lets just move on and never speak of this again"

            show cirava smile

            show bg ciravablock with wiperight

            "Cirava leads you into a fairly large loft bedroom. This room is a bit less ostentatious than the streaming area downstairs."

            cir talk "well here we are lmao"

            cir "welcome to my respiteblock"

            cir peace "were gonna get you hooked up lmao"

            cir point "if youre gonna be my new friend you gotta look the part"

            cir "for streams and stuff you know"

            cir "well have to make you a chittr account too"

            cir "its good for my image to have friends lmao"

            cir cross "the pickings have been pretty slim ever since"

            show cirava angst at theincident

            show red at redoverlay3

            cir "the incident"

            hide red

            show cirava smile at default

            "On that ominous note, Cirava presses a button on the wall, and a large door opens to reveal an expansive walk-in closet filled with colorful accessories and clothes. It looks like a regular batshit neon shirtpocolypse."

            cir "well have at it"

            show cirava shrug at nod

            cir "unless you want me to help you pick out a look lmao"

            menu:
                "[pick] Pick out your own look.":


                    "You let Cirava know you are perfectly comfortable picking out your own look. You think you can figure out this “fashion” business easily enough! What could possibly go wrong? This is child’s play."

                    cir talk "yeah man"

                    cir "fashion is just all about like"

                    cir feeling "what youre feelin"

                    show cirava shrug at nod

                    cir "and also whats trending but ya know"

                    cir "were the ones that start the trends"

                    cir point "you strike me as a real influencer lmao"

                    cir peace "go for it my dude"

                    hide cirava with moveoutleft

                    "You enter the closet tentatively. As soon as Cirava is out of sight, your stupid ego deflates like a farting balloon. You don’t know the first thing about the hip youth alien fashion of today!"

                    "This is going to be an absolute shitshow, you reckon. You are fully prepared to make an utter fool of yourself."

                    "Well, might as well get started!"

                    "You pick a few accessories off of the shelves at random: a bright pink hat? Sure! You tilt it jauntily to the side. You’re pretty sure that’s cool?"

                    "Sunglasses: definitely. That’s a no-brainer. No cool guy would be caught dead without a sweet pair of shades. You select the most ostentatious pair available."

                    "You think you’re getting the hang of this moisturewave aesthetic! You just have to look like the biggest tool possible."

                    "Several accessories later..."

                    scene bg spotlight with fade

                    show makeover1 at entranceright

                    show spotlight at entranceleft

                    play music "volumes/volume2/music/aesthetic.mp3" fadeout 0.3 noloop

                    $ renpy.pause()

                    scene bg ciravablock with fade

                    play music "volumes/volume2/music/cirava.wav" loop

                    show cirava talk

                    cir "oh"

                    cir "my"

                    cir "fuck"

                    cir feeling "this shit is transcendent"

                    cir "wow"

                    cir "you got me speechless"

                    cir talk "just"

                    cir "damn"

                    cir "look at you"

                    cir "its like youre a whole new guy"

                    cir feeling "a much chiller and cooler guy who i now gotta be friends with right now immediately"

                    cir peace "now all we gotta do is debut you to my hundreds and thousands of followers lmao"

                    cir "this is gonna be fucking great"

                    cir "lets take some selfies"

                    "Your heart is soaring! You did it! You really did it! You’re down with the kids! And now Cirava wants to take the coveted “selfies” with you. This night couldn’t be going any better!"

                    "You may look like a complete asshole, but if it can win you popularity with a bunch of alien teenagers, then an asshole you will be! Selling out is amazing."

                    cir point "well what are you waiting for"

                    cir talk "get over here were gonna take some ‘fies"

                    "You pose with Cirava for several selfies. They put their arm around you in a gesture of newly-formed friendship. You are beaming with friend-pride."

                    cir feeling "oh hell ya"

                    cir "these are turning out great"

                    cir talk "damn"

                    cir "were killin it"

                    cir "now all i gotta do it post em"

                    "Cirava fiddles around with their phone for a while. You’re so nervous! You’ve never been internet famous before!"

                    "You hope the new fame won’t change you too much. Or maybe you do hope it will change you? Change you into someone with a TON of FRIENDS!"

                    cir "and the likes are rollin in"

                    cir feeling "oh yes"

                    cir "i live for this shit"

                    cir talk "haha this one guy is asking if you want any of your quadrants filled"

                    cir "oh and this girl loves your shades"

                    cir "damn a lot of people asking if ur single lmao"

                    cir point "dont go for it tho"

                    show cirava shrug at nod

                    cir "my followers are fucking freaks dude"

                    "You aren’t quite sure what filling a quadrant is. Sounds like some kind of fucked up alien ritual. But if it’s anything like FRIENDSHIP you are all for it!"

                    cir peace "welcome to my twisted internet fame lmao"

                    cir "lets chill out and listen to some beats"

                    cir point "you vape?"

                    cir "i got a pretty juicy rig downstairs"

                    show bg ciravastream with wipeup

                    "Before you know it, you’re sitting on Cirava’s couch, watching them finagle with a horrifyingly elaborate vape rig that appears to be made out of some sort of living larvae. You don’t wanna know."

                    "Cirava places their mouth on what surely must be a bug anus and inhales deeply. The rig makes an awful high pitched rattling noise. You think you’re going to vomit."

                    show cirava vape at lowered

                    cir "oh man thats the good stuff"

                    cir "here ya go dude"

                    show cirava smile at default

                    "You take the trembling insect into your hands. Well. Here goes. Your final hurdle to eternal friendship and popularity."

                    show vape with dissolve

                    "You VAPE VIGOROUSLY, inhaling as much as you can. The vapor fills your lungs immediately. It burns, a lot."

                    "You suddenly realize that you’re not quite sure if this alien vape juice is compatible with your anatomy. You could have just inhaled a bug-ass-full of poison like a fucking idiot! What a way to die. Your vision swims."

                    cir point "yea u got it"

                    cir talk "just hold it in lmao"

                    show cirava smile at shaking

                    show bg ciravastream at shaking

                    "Tears stream down your face as you hold in your double lungful of insect gas. You sure are glad you have on your pair of COOL SHADES, or you would never be able to live this embarrassment down."

                    "You’re not sure how long you’re supposed to do this? As long as it takes."

                    cir point "uh"

                    cir "you can exhale now"

                    show cirava smile at default

                    show bg ciravastream at default

                    hide vape with dissolve

                    "You cough and sputter, green vapor spewing from your mouth straight into Cirava’s face. You did it. You LIVED."

                    show high1 at highanim1

                    show high2 at highanim2

                    cir peace "ahahah"

                    cir talk "oh man that was sick"

                    show statue at floaties1

                    show aesthetic at floaties2

                    show horse at floaties3

                    "Your head feels light and woozy, and you giggle. Ha ha. Yeah. The two of you kick back and relax on the couch, and you stare up at the ceiling. Woah. When did that huge wasp nest get there? Haha. Crazy, man..."

                    "Cirava’s music suddenly sounds a lot more interesting."

                    cir "dude"

                    cir "today has been way chiller than i ever expected lmao"

                    cir peace "you are officially my best friend for life"

                    show cirava shrug at nod

                    cir "just promise me youll never betray me lmao"

                    show cirava vape at lowered

                    "You promise. This is incredible. You love your new friend. You watch as they effortlessly take another huge rip from their vape rig."

                    show cirava cross at default

                    cir "ive been burned in the past lmao"

                    cir "its not easy being popular online"

                    cir "especially as a lowblood"

                    cir point "i used to be such a fuckin bigshot"

                    cir "got into sassy fights with highbloods on chittr"

                    show cirava shrug at nod

                    cir "always had some shit to say lmao"

                    cir cross "then shit got outta control"

                    cir "im a psionic so bitches started reporting me as way more powerful than i really am lmao"

                    cir "trying to get me all enslaved and shit so i couldnt keep up with my streams"

                    cir angst "its all jealousy ya know"

                    cir "my stupidass friends all turned on me so they wouldnt be targeted next lmao"

                    cir cross "so i took matters into my own hands"

                    cir "gouged out my fuckin eye"

                    cir "it was sick as fuck"

                    cir feeling "cant use ME as a battery bitch"

                    cir talk "i still got a big following but i dont really talk online anymore lmao"

                    show cirava shrug at nod

                    cir "better to just stay under the radar and not piss people off"

                    cir "just be chill"

                    cir talk "and if i dont get close to my followers they cant try to use me"

                    cir cross "course that just means i no longer have any god damn friends lmao"

                    cir "well"

                    cir peace "until you"

                    "You are truly moved. What a special bond you have formed with your new friend, to have them open up to you about their darkest secrets."

                    "This is the most significant and transcendent moment you have ever experienced. The two of you share a beautiful and tender bro embrace, the likes of which will never be replicated in this known universe again, for all time, forever."

                    "Probably."

                    show cirava vape at lowered

                    "You don’t really know, you’re high as fuck right now."

                    call ending ("win cirava", True, False) from _call_ending_6

                    return
                "[pick] Let Cirava help you with your look.":


                    "You admit, you have no idea how to dress yourself. You could really use some expert advice from a teen."

                    cir point "oh shit"

                    cir "cue the makeover sequence bitch"

                    cir feeling "im gonna make you look aesthetic as fuck lmao"

                    "You stand in the center of Cirava’s closet for a good hour as they go back and forth between various fashion items. Man, this troll is really indecisive! You think you’re gonna go blind from all the neon in here."

                    cir point "hmmm"

                    cir "ok"

                    cir "im done lmao"

                    cir talk "that was surprisingly hard"

                    show cirava shrug at nod

                    cir "you have a hard to dress body lmao"

                    cir "just in general youre kinda fucked up looking tbh"

                    cir talk "its chill tho"

                    cir peace "cause now you look fly as hell"

                    "You look at yourself in the mirror..."

                    scene bg spotlight with fade

                    show makeover2 at entranceright

                    show spotlight at entranceleft

                    play music "volumes/volume2/music/aesthetic.mp3" fadeout 0.3 noloop

                    $ renpy.pause()

                    scene bg ciravablock with fade

                    play music "volumes/volume2/music/cirava.wav" loop

                    show cirava feeling

                    cir "iconic"

                    cir talk "now we just gotta get you set up on the social medias my dude"

                    cir "but first"

                    cir peace "selfie time lmao"

                    "You take a variety of cool selfies with Cirava! Wow, this is really going well!"

                    cir talk "aight ill just post these and promo you"

                    cir "youll be internet famous in no time"

                    cir peace "then we can finally be friends lmao"

                    "That’s what it’s all about, baby. That’s what you’ve been working toward this entire time. Cirava’s friendship is so close you can smell it. It smells pretty dank."

                    cir point "hm seems like people are really into you"

                    cir "check it out"

                    "It’s true, the likes and comments and subscriptions are just rolling in. Huh."

                    cir cross "at this rate youll be more popular than me"

                    "You assure Cirava that this will definitely never happen. All you truly desire is FRIENDSHIP, not FANS."

                    cir "thats what they all say"

                    cir angst "all my so called friends"

                    cir cross "they were only in it cuz i was popular"

                    cir "no one ever gave a shit about me as a person lmao"

                    cir "im just a funny meme to them"

                    cir "just a guy they can copy"

                    cir "you know highbloods are always stealing my work"

                    cir "my look"

                    cir "my music"

                    cir angst "im the real influencer but theres violetbloods out there taking my shit and getting twice the followers and tons of money"

                    show cirava angst at shaking

                    cir "and im stuck here in this shitty hive with no friends because they all turned on me"

                    cir cross "but its cool"

                    cir "its chill"

                    show cirava shrug at nod

                    cir "im totally chill with it lmao"

                    "Something shifts in Cirava’s expression as they get a good look at you. You tense up. Your new friend sure is acting weird..."

                    "DING!{w=0.75} Cirava checks the notifications on their phone."

                    cir angst "what"

                    cir "the hell"

                    show cirava angst at bounce

                    cir "did you do"

                    "Huh? What? You didn’t do anything!"

                    show cirava angst at bounce

                    cir "you think you can just steal my look and get away with it?"

                    cir "all my followers think youre the new big thing because you look like me"

                    cir cross "they wanna know what the hell is going on"

                    show cirava cross at bounce

                    cir "whens your new friends stream?"

                    show cirava cross at bounce

                    cir "whats their sign?"

                    show cirava angst at bounce

                    cir "are you kidding me?"

                    cir cross "you havent even done anything"

                    cir "youre"

                    cir "youre just like all the rest"

                    "No, no! You don’t want to be like all the rest! You just want to be friends!"

                    cir "its too late for that now"

                    cir "youve made me look like a fucking idiot"

                    show cirava cross at calloutzoom1

                    show red at redoverlay1

                    cir "and now theres only one thing to do"

                    show cirava cross at calloutzoom2

                    show red at redoverlay2

                    cir "i really didnt want it to come to this"

                    show cirava cross at calloutzoom3

                    show red at redoverlay3

                    cir "but youve left me with no choice"

                    show cirava angst at calloutzoom4

                    show red at redoverlay4

                    cir "{size=+12}im writing a callout post{/size}"

                    "NOOOOOOOOOOOOOO!"

                    show cirava angst at default

                    hide red

                    "Cirava types furiously on their device. You can’t stand to look. This is the worst possible thing that could have happened. Now... no one will be your friend ever again. You’ll be forced to live on the outskirts of society, a pariah."

                    "You can’t even begin to imagine the things that Cirava must be writing about you. You must have fucked up so many things in your life, to lead you to this point."

                    "There’s only one thing to do."

                    hide cirava with dissolve

                    show bg ciravastream with wipeup

                    "You stagger downstairs, past all the portraits of Cirava’s ex-friends. You wonder if they met the same horrible fate as you. Their grinning faces taunt you with slivers of friendship that could never be."

                    show bg alternia with wipeup

                    "You burst out of the front door of Cirava’s hive, and make your way to a conveniently placed stump. You sit on it in complete despair. There’s no point living anymore. With trembling hands, you reach inside..."

                    call ending ("gameover cirava2", False, True) from _call_ending_7

                    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
