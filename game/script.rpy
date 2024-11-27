
# CHARACTERS
define k = Character("Kotarou", color =  "#7F00FF" )
define a = Character("Akane", color =  "#e200b1" )


# BACKRGOUNDS
image school_corridor = im.Scale("bg schoolcorridor.jpg", 1280, 720,)
image enter_classroom = im.Scale("bg enteringclassroom.jpg", 1280, 720,)


label start:

    scene school_corridor with fade
    
    # we will change this
    play music sfx_bell noloop 
   
    "The new school year begins.."

    "and the third-year students settle into their new classroom assignments. Among them is Kotarou Azumi"
    # //Shows Kotarou Character
    "a quiet and introverted boy with a passion for literature—He has a dream of being the greatest writer one day."

    # //Shows Akane Character
    "Akane Mizuno, a dedicated track-and-field athlete, a sports and academic enthusiast who always excels either in the field of sports or academics."

    # // Insert Breathing sound f0r Akane 
    a "Breathe in, breathe out. Stay calm, you will be okay."

    # //worried look on her face
    a " I am feeling nervous about this new school year of mine. But this will be okay, I got this!"

    # // fade this 

    "But despite her capabilities to conquer and excel in everything, she cannot contain her emotions—most especially her nervousness."

    "However,  with encouragement and determination in her soul, Akane then proceeded to enter their classroom premises to attend her first class on her first day of being a third year student."

    # Kotarou's POV
    k "Even in middle school, there is inequality—upper class and middle class, smart and average, and cool clubs and lame ones."

    "On  the other hand, there is a boy filled with wisdom and perception in his mind. A boy full of knowledge with words only wise knows."

    "He has the capabilities to sort his emotions up through writing a literary piece."

    scene enter_classroom with fade
    # //insert students talking sfx (pag walang nahanap na okay na BG wag nalang)

    # //Show Akane slide left to middle

    return
