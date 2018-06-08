# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -2 python:

    iap.register("Volume2", identifier="com.wp.friendsim.volume2", amazon=None, google="com.wp.friendsim.volume2", ios=None, consumable=False)
    iap.register("Volume3", identifier="com.wp.friendsim.volume3", amazon=None, google="com.wp.friendsim.volume3", ios=None, consumable=False)
    iap.register("Volume4", identifier="com.wp.friendsim.volume4", amazon=None, google=None, ios=None, consumable=False)

    if persistent.flash is None:

        persistent.flash = True

    def eyewarp(x):

        return x**1.33

    def eyewarpaxe(x):

        return 1.0 - (1.0 - x)**0.15

define narrator = Character(window_background="gui/textbox_narration.png", what_font='courbd.ttf', what_size=22,  color='#000000', what_color='#000000')
define op = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5)

define a = Character("ARDATA", color='#FFFFFF', image="ardata", window_background="gui/textbox_cobalt.png", who_outlines=[ (4, "#005682") ],)
define e = Character("Litl_E", color='#FF0080', image="litle", window_background="gui/textbox_yellow.png", who_outlines=[ (4, "#FAFF00") ],)
define o = Character ("Osamco", color='#FAFF00', image="osamco", window_background="gui/textbox_fuschia.png", who_outlines=[ (4, "#FF0080") ],)
define die = Character("DIEMEN", color='#FFFFFF', image="diemen", window_background="gui/textbox_rust.png", who_outlines=[ (4, "#a10000") ],)
define dog = Character("DIEMEN", color='#FFFFFF', image="dogless", window_background="gui/textbox_rust.png", who_outlines=[ (4, "#a10000") ],)
define shr = Character("DIEMEN", color='#FFFFFF', image="shirtless", window_background="gui/textbox_rust.png", who_outlines=[ (4, "#a10000") ],)

define stab = Fade(.08, 0.0, .2, color="#FF0000")
define redstab = Fade(0.09, 0.09, 0.15, color="#FF0000")
define bluestab = Fade(0.09, 0.25, 0.25, color="#0000AA")

image ardata = "images/test_sprite.png"
## image side ardata = "images/test_zodiac.png"

image litle standing = "images/litle_standing.png"
image litle silhouette = "images/litle_silhouette.png"

image osamco standing = "images/osamco_standing.png"
image osamco talking = "images/osamco_talking.png"

image ardata disgust = "images/ardata_disgust.png"
image ardata amused = "images/ardata_amused.png"
image ardata laugh = "images/ardata_laugh.png"
image ardata angry = "images/ardata_angry.png"
image ardata smile = "images/ardata_smile.png"
image ardata testy = "images/ardata_testy.png"
image ardata bored = "images/ardata_bored.png"
image ardata murder = "images/ardata_murder.png"
image ardata cry = "images/ardata_cry.png"
image ardata ohoho = "images/ardata_ohoho.png"
image ardata wink = "images/ardata_wink.png"
image ardata hand = "images/ardata_hand.png"

image diemen smile = "images/diemen_smile.png"
image diemen cry = "images/diemen_cry.png"
image diemen die = "images/diemen_die.png"
image diemen curious = "images/diemen_curious.png"
image diemen recoil = "images/diemen_recoil.png"
image diemen shock = "images/diemen_shock.png"
image diemen optimistic = "images/diemen_optimistic.png"
image diemen talk = "images/diemen_talk.png"
image diemen thinking = "images/diemen_thinking.png"
image diemen offer = "images/diemen_offer.png"
image diemen frown = "images/diemen_frown.png"

image splatter = "images/splatter.png"
image sludge = "images/sludge.png"


image bg alternia = "images/background1.png"
image bg alternia2 = "images/background4.png"
image bg alternia3 = "images/background2.png"
image bg alternia4 = "images/background3.png"
image bg house1 = "images/house_outside.png"
image bg house2 = "images/house_inside.png"

image bg ardata hive = "images/ardata_kitchen.png"
image bg dungeon = "images/ardata_basement.png"

image bg sewer = "images/sewer.png"
image bg meatlocker revealed = "images/meat_locker.png"
image bg meatlocker hidden = "images/meat_locker.png"

image gameover = "images/gameover.png"

image gameover diemen 2 = "images/diemen_lose2.png"
image gameover diemen 1 = "images/diemen_lose1.png"
image gameover ardata = "images/ardata_lose.png"
image gameover litle = "images/litle_lose.png"

image win diemen = "images/diemen_win.png"
image win ardata = "images/ardata_win.png"

style outlined:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "FFFF00"
    bold True

style friend:
    outlines [ (absolute(2), "#FF00FF", absolute(1), absolute(1)) ]
    color "FFFF00"
    font "courbd.ttf"
    size 72

style choice_button_text:
    color "0000FF"
    font "courbd.ttf"


transform bounce:
    ypos 720
    easeout 0.12 ypos 706
    linear 0.12 ypos 720

transform cornerbounce:
    ypos 734
    easeout 0.12 ypos 720
    linear 0.12 ypos 734

transform nod:
    ypos 720
    easeout 0.12 ypos 732
    linear 0.12 ypos 720

transform slowbounce:
    ypos 720
    easeout 0.15 ypos 710
    linear 0.15 ypos 720

transform slowerbounce:
    ypos 720
    easeout 0.1 ypos 714
    linear 0.1 ypos 720

transform bouncing:
    ypos 720
    linear 0.1 ypos 710
    linear 0.1 ypos 720
    repeat

transform shaking:
    ypos 720
    linear 0.07 ypos 718
    linear 0.07 ypos 720
    repeat

transform holdingup:
    easein 0.60 zoom 1.6 yalign 0.9
    easeout 0.45 zoom 2.2 yalign 0.35

transform setdown:
    easein 0.45 zoom 1.6 yalign 0.9
    easeout 0.60 zoom 1.0 yalign 1.0

transform dungeon:
    ypos 734
    linear 0.5 xalign -0.12 zoom 0.75

transform lowered:
    ypos 720
    linear 0.75 ypos 755

transform bloodoverlay:
    zoom 1.25 rotate 65 yalign 0.42 xalign 0.48

transform sweepleft:
    linear 0.66 xalign -1.50

transform sweepright:
    linear 0.66 xalign 2.00

transform hugincoming:

    easeout 0.66 zoom 1.15
    pause 0.25
    easeout 0.66 zoom 1.0

transform hug:

    ypos 720
    easeout 1 zoom 1.75 ypos 1000

transform endhug:

    easein 0.33 zoom 1.0 ypos 720

transform closeup:
    easein 1.5 zoom 1.75 yalign 0.4

transform dogzoom1:
    easein 0.5 zoom 1.9

transform dogzoom2:
    easein 0.5 zoom 2.05

transform dogzoom3:
    easein 0.5 zoom 2.20

transform dogzoom4:
    easein 0.5 zoom 2.35

transform dogzoom5:
    easein 0.5 zoom 2.5

transform dogunzoom:
    easeout 0.1 zoom 1.0

transform dogchoke:

    yalign 1.0 ypos 720
    easeout 0.15 ypos 760
    pause 0.2
    linear 0.03 ypos 756
    linear 0.03 ypos 760
    linear 0.03 ypos 756
    linear 0.03 ypos 760
    linear 0.03 ypos 756
    easein 0.35 ypos 770
    pause 0.15
    linear 0.08 ypos 740
    easein 0.1 ypos 720
    pause 0.3
    repeat

transform diemendies:

    linear 0.04 ypos 720
    easeout 0.8 ypos 500
    pause 0.1
    linear 0.08 rotate 180
    easein 0.35 ypos 1640

transform dogagony:
    xalign 0.5 ypos 720
    easein 0.25 xalign 0.45 ypos 730
    easeout 0.25 xalign 0.55 ypos 740
    easeout 0.25 xalign 0.45 ypos 750
    easeout 0.25 xalign 0.55 ypos 760
    easeout 0.25 xalign 0.45 ypos 770
    easeout 0.25 xalign 0.55 ypos 780
    easeout 0.25 xalign 0.45 ypos 790
    easein 0.25 xalign 0.5 ypos 800

transform rumbling:

    ypos 720
    linear 0.1 ypos 728
    linear 0.1 ypos 720
    repeat

transform sludgeanim:

    ypos 720
    easein 0.4 ypos 775
    pause 0.2
    easein 0.4 ypos 720
    pause 0.2
    repeat

transform drownanim:

    ypos 720
    easein 0.45 ypos 775
    pause 0.25
    easein 0.35 ypos 720
    pause 0.25
    repeat

transform sludgebegone:

    linear 1.8 ypos 1440

transform lookaround:

    xalign 0.5
    linear 0.6 xalign 0.0
    pause 1.2
    linear 0.3 xalign 0.5
    pause 1.2
    linear 0.3 xalign 1.0
    pause 1.2
    linear 0.6 xalign 0.5

transform menumove:

    xpos 20

    on hover:
        linear .25 xpos 50
    on idle:

        linear .25 xpos 20

transform wiggle:

    rotate 0
    ypos -250

    on hover:
        linear .1 rotate -2
        linear .1 rotate 0
        linear .1 rotate 2
        linear .1 rotate 0

python:

    import os
    import os.path

## DLC BASICS

#python:

#    if renpy.loadable("dlctest.rpy"):

#            renpy.jump("dlctest")


# The game starts here.

label start:

    $ pick = "{color=#000000}>{/color}"

    $ quick_menu = False

    $ volume1 = True

    if renpy.android or renpy.variant("android"):

        jump androidsetup

    if renpy.windows or renpy.macintosh or renpy.linux:

        jump compsetup

    jump start2

label start2:

    stop music fadeout 1.5

    show expression "gui/main_menu.png"

    window hide

    scene black with Dissolve(1.5)

    $ main_menu = True

    call screen vol_select() with Dissolve(1.0)

    return

label androidsetup:

    python:

        iap.restore(interact=True)

        if iap.has_purchased("Volume2"):
            volume2 = True
        else:
            volume2 = False

        if iap.has_purchased("Volume3"):
            volume3 = True
        else:
            volume3 = False

        if iap.has_purchased("Volume4"):
            volume4 = True
        else:
            volume4 = False

        if iap.has_purchased("Volume5"):
            volume5 = True
        else:
            volume5 = False

        volume4 = True

    jump start2

label compsetup:

    python:

        if renpy.loadable("volumes/volume2/vol2script.rpyc"):
            volume2 = True
        else:
            volume2 = False

        if renpy.loadable("volumes/volume3/vol3script.rpyc"):
            volume3 = True
        else:
            volume3 = False

        if renpy.loadable("volumes/volume4/vol4script.rpyc"):
            volume4 = True
        else:
            volume4 = False

        if renpy.loadable("volumes/volume5/vol5script.rpyc"):
            volume5 = True
        else:
            volume5 = False

    jump start2







label volumeone:

    $ pick = "{color=#000000}>{/color}"

    $ quick_menu = False

    stop music fadeout 1.5

    show image "gui/main_menu.png"

    window hide

    scene black with Dissolve(1.5)

    op "After walking for what felt like hours, you finally approach a large, multi-coloured building that appears to be another hive."

    op "You’re far from any other form of civilization, and this hive is sitting on a seemingly endless expanse of green grassland."

    op "It is very late, and you are very tired."

    op "Not to mention in dangerous need of medical attention."

    op "What you really need most of, however, is..."

    op "{size=80}{=friend}FRIENDSHIP!{/=friend}{/size}"

    op "You cautiously knock on the door."

    op "..."

    op "No answer."

    op "after a second knock, you hear someone opening the door!"

    op "When the door opens, you see..."

    call screen troll_select1

    with Pause(0.25)

    return

label litle:

    scene black with Dissolve(1.0)

    scene bg house1 with dissolve

    $ quick_menu = True

    "The door opens and a troll steps out holding a flashlight. You remember how dark it is."

    "You can only barely see a silhouette of the troll, and you’re blinded by the light."

    window hide

    show litle silhouette with moveinbottom

    play sound "voices/VoiceLitle1.mp3"

    e ">Oh… uh… whom ar_E you? I thought you w_Er_E Osamco.<"

    "You quickly explain to your new potential friend that you don’t know who Osamco is, but you would like to be friends."

    "You ask if you can step inside and have a quick rest, and maybe some medical attention."

    play sound "voices/VoiceLitle2.mp3"

    e ">Alright. Just stay qui_Et and com_E with m_E.<"

    "Your potential buddy disappears into the doorway again, along with the blinding light. You blink a few times to get rid of the purple dots before following."

    show bg house2 with wipeleft

    show litle standing at default

    "You emerge in a room with similarly multicoloured furniture. Standing in the centre of the room is the troll you just met. You see the flashlight he was previously wielding sitting on a table near you."

    e ">W_Elcom_E to my hiv_E. I do not b_Eli_Ev_E w_E hav_E b_Ecom_E aquaint_Ed y_Et. My nam_E is Litl_E."


    menu:

        "What should you say?"

        "[pick] Ask how to spell wierd name.":

            "You ask how one would go about spelling such an exotic name."

            e ">It’s sp_Ell_Ed ‘L’ ‘I’ ‘T’ ‘L’ Und_Erscor_E ‘E’.<"

            "Excuse me, but who the h*ck has an underscore in their name, you cry out in pure shock. You immediately realize this is a horrible mistake."

            e ">Fri_Ends do not mak_E fun of th_Eir fri_Ends’ nam_Es. G_Et out.<"

            scene black with Dissolve (0.5)

            $ renpy.pause(0.5)

            $ quick_menu = False

            play music "music/game_over.mp3" fadeout 1.0

            scene gameover litle with Dissolve(1.0)

            $ renpy.pause()

            stop music fadeout 1.0

            scene black with Dissolve(1.0)

            return

        "[pick] Nod silently and pretend you understand this culture’s naming conventions.":

            "You nod along, pretending to be savvy to this culture’s naming customs. Your potential buddy buys your savviness to a T!"

    e ">And what is your nam_E?<"

    "You tell Litl_E your name. He nods, calculating the information for a few moments."

    e ">Int_Er_Esting. Your cultur_E s_E_Ems to us_E v_Ery short nam_Es. I hav_E n_Ev_Er h_Eard anyon_E us_E four l_Ett_Ers b_Efor_E.<"

    "You aren’t sure whether to take it as a compliment or as an insult, but hey! He’s your friend-to-be! He would never insult you!"

    menu:

        "What should you do next?"

        "[pick] >Ask about the weird colour scheme.":

            "You point to the couch and ask why it’s in that specific colour palette."

            e ">W_Ell, typically in troll cultur_E th_E furnitur_E and basically _Ev_Erything _Els_E is th_E colour of th_E blood of th_E troll whom liv_Es in said hiv_E.<"

            "You nod. So your blood is… a mix of fuschia and yellow…?"

            e ">Oh h_Eck no. I am a y_Ellow blood. Osamco is a fuschia blood. It is not normal for two trolls to liv_E tog_Eth_Er.<"

            "You ask for a little more information on this “Osamco” fellow."

            e ">Osamco found m_E as a grub. I was all alon_E, about to b_E cull_Ed for b_Eing a mutant… th_En Osamco swoop_Ed in and grabbed m_E. I hav_E b_E_En living with him _Ev_Er sinc_E.<"

            "You nod, holding in a tear from this boy’s touching story."

            e ">Anyways, I should g_Et you patch_Ed up. That arm looks lik_E it had b_Ett_Er days.<"

            "Litl_E turns and walks out through a door. You guess you should follow him. You follow him down a hallway and up some stairs, then down another hallway. Litl_E opens a door labeled “K_E_Ep out, Osamco.”"

            e ">W_Elcom_E to my r_Espit_Eblock.<"

            "You assume that “Respiteblock” is the alien version of “Laboratory.” There’s a large metal object that looks like some form of hazardous material container above a desk with an alien laptop on the right wall, and a wooden box and a poster on the left. There’s a sword mounted on the wall by the door."

            e ">G_Et up th_E ladd_Er and hop into th_E recup_Eracoon. That will h_Eal you right up.<"

            "You turn to climb the ladder by the metal desk/material-container thing, then Litl_E stops you."

            e ">You ar_E going to want to tak_E off your cloth_Es first. You do not want to g_Et thos_E cov_Er_Ed in sopor, do you?<"

            "You blush a little, as your new friend just asked you to take off your clothes."

            "You ask him to turn away, then, after he does so, you cautiously slide off your shirt. You make sure his back is still thoroughly turned, and proceed to remove the rest of your clothes."

            e ">You don_E yet? Onc_E you ar_E, hop into th_E sopor. Th_E gr_E_En stuff.<"

            "You hop up the ladder and look into the green, potentially radioactive sludge."

            "You slowly slide into the metal holding container, expecting to feel a burning pain as your skin singes away, but instead you feel a chill pass over your body. You immediately feel drowsy..."

            scene black with Dissolve(1.5)

            e ">H_Ey. Wak_E up. You hav_E b_E_En asl_E_Ep for n_Early a day.<"

            "You groggily open your eyes. Five more minutes, you groggily mumble."

            e ">Nop_E. Out you go.<"

            "You slide out partially, then remember that you aren’t wearing any clothes."

            e ">Do not worry. I will turn around.<"

            "Litl_E turns around as you slide out of the container and slide down the ladder. You brush off the green sludge that stuck to your skin, then you put on your clothes."

            e ">Your small injuri_Es and s_Ev_Eral of your bigg_Er on_Es should b_E h_Eal_Ed now.<"

            "You thank your friend for his kindness."

        "[pick] >Let him choose the conversation topics!":

            "And whΩ are yΩu, exactly?"

            e "And whΩ are yΩu, exactly?"

            o "And whΩ are yΩu, exactly?"

    "you have reached the end of what is available for Litl_E. There will be more soon!"

    return

label osamco:

    scene black with Dissolve(1.0)

    scene bg house1 with dissolve

    $ quick_menu = True

    "You hear what sounds like somebody running full-speed into the door, before it swings open, revealing a incredibly tall troll on the other side."

    show osamco standing with moveinbottom

    o talking "And how may I hELp you today, siR?"

    show osamco standing

    "you straiten yourself out from the shock of his suddenness, and tell him about your glourious quest for friendship."

    o talking "That sounds prEtty CooL."

    o "I do enjoy haVing friEnds..."

    show osamco standing

    "His considering you fills you with glee! You explain that your willing to do almost anything for friendship at this point."

    o talking "Anything...?"

    show osamco standing

    "You begin to regret your choice of words, but stick by them nontheless."

    o talking "WELL come on in thEn!"

    show osamco standing

    show bg house2 with wipeleft

    "You step in, afraid of what he might request, but optamistic that this could work out."

    o talking "Want a snack?"

    menu:

        "Do you?"

        "[pick] Sure.":

            o talking "aLright, I'LL bE right back!"

            hide osamco with moveoutright

            "You wait for a while, looking at the strange colouration of the surrounding furnature."

            "He finally returns, carrying a plate with a single slice of cheese."

            show osamco standing with wipeleft

            o "HERE you go!"

        "[pick] I'm alright, don't want to be a bother.":

            o talking "Alright!"

    "you have reached the end of what is available for Osamco. There will be more soon!"

    return
