import time
import sys
import random

# Define possible Options for Answers

yes_list = ("Y", "y", "Yes", "yes", "K", "k", "Ok", "OK", "ok", "YES")
no_list = ("N", "n", "No", "no", "NO")

# Define Player Status and HP
player = {'Name': '', 'Health': 2, 'Gender': ''}
HP = ("Your current HP is: ", player['Health'])

# Def class and inventory system


class Item(object):
    def __init__(self, name, power, type, value, quantity):
        self.name = name
        self.power = power
        self.type = type
        self.value = value
        self.quantity = quantity


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item


def print_items():
    print('\t'.join(['Name', 'Power', 'Type', 'Value', 'Quantity']))
    for item in inventory:
        print('\n' + '\t'.join([str(x) for x in [item.name, item.power, item.type, item.value, item.quantity]]))


# Define an empty inventory and possible Items to get

inventory = []
clothes = Item('Clothes', 70, 'Armor', 3, 1)
ring0 = Item('Ring', 10, 'M. Ring', 500, 1)
ring1 = Item('Ring', 5, 'Ring', 10, 1)
ring2 = Item('Ring', 5, 'Weapon', 11, 1)
ring3 = Item('Ring', 50, 'Weapon', 50, 1)
ring4 = Item('Ring', 5, 'Ring', 12, 1)
paper = Item('paper', 1, 'Paper', 3, 1)
Key = Item('Key', 0, 'Old Key', 0, 1)

# Restart stats and inventory to it's initial position


def restart():
    player = {'Name': '', 'Health': 2, 'Gender': ''}
    inventory = []


# Def options for floor 1 (Floor 2 will be annunced next summer)

floor_1_opt_a = [
        'Inspect Wardrobe',
        'Inspect Fireplace',
        'Inspect Desk',
        'Inspect Old Books',
        'Use the stair',
        'Use the door']

floor_1_opt_b = [
        'Inspect Wardrobe',
        'Inspect Fireplace',
        'Use the stair',
        'Use the door']


# Described situations for this game
situation_1 = """
            With your right arm, you try to reach the top a wooden desk near your bed, even in pain, with a blurry vision, you
            recognized a piece of and old scroll that was partialy hanging from the desk. You grab that piece of papper slowly,
            shaking...

            """
dice_1st_floor_a = """
            11+ : You sucessfully grab the scroll

            You feel the same preassure again, that damn cursed being inside you is starting to move.
            While you hang the scroll with your right hand and start to read it, carefully, you move your left hand inside the
            deep cut between your ribs.
            You fell the "THING" rollep up in your ribs, you grab it with strenght.

            You pulled it out fast.

            A gian worm. Slippery and covered in blood. You could felt it's scales when it passed through the cut.
            It turned to you, ugly, disgusting.

            And then it atacked.

            You used a strenght that you didn't have and threw the "judlo" into the fireplace.
            A shriek and the sound of its body writhing in the embers was like music.

            Finally you cast the spell. A very strong light emanates from the hut, a light that could be seen in distance.

            Your wounds start to heal, you broken ribs are now in the right place, the mark of your theet in your arm disapear.
            Only a little scratch remains where you pulled the animal.
            You feel revigorated. But your still hungry and in a need of a shower.

            """

dice_1st_floor_b = """
            1 - 11 (FAIL): The scroll slips from your hand and fall on the floor.

            You blink, lost your focus, the scroll fell to the floor. You roll over and try to reach the spell on the ground.
            When you stretch your arm a giant worm raises from between your ribs. You look to it, terrified. The worm shrikes,
            showing its sharp theet, a second later it dives to your chest and start to bite. You fell from the bed.

            Bite after bite the worm starts to pierce your chest (it follows your heartbeat).
            You grab the worm with both hands trying to stop it. Blood spreads on the hut walls, you scream in pain.
            You feel the scroll below your backs, you don't have any time.
            You used a strenght that you didn't have. With your left hand you remove the "judlo" from your chest and with the
            right you grab the scroll on the ground.

            You cast the spell.

            The worm twists in your hand. With a quick move, now with both hands free, you grab the animal in front of you and
            starts pulling it in opposite directions. Despite of it's slipperiness, you are determinated.

            The worm body splits in two. A mix of green fluid and red blood (your blood) splatter over your face, floor, and walls.

            Your wounds start to heal, you broken ribs are now in the right place, the mark of your theet in your arm disapear.
            Only a little scratch remains where the animal attacked your chest.
            You feel revigorated. But your still hungry and in a need of a shower.

            """

welcome = """
            Just another little slip,
            A little sip,
            A bit drunk,
                A night of sleep.

            The dream dissipated slowly while you woke up...

            You open your eyes. All you see is the partialy rotten black-brown wood logs of the little hut where you hide.
            Shadows dance under the effect of the blue fire that still resists inside the stone hearth.

            You start to wake up and try to get in your feet, but before you could see or think of anyhting else, you felt
            a deep, painfull and dying pain when your broken ribs starts to pierce your left lung.
            You remembered one thing that your old friend used to say:
            "Wrong move darling."

            Fast, vary fast...
            Your left hand is over a deep cut on the left side of your body.
            You move your right arm to your mouth.
            Big mistake ah? Maybe not..
            That was the only thing you had to prevent your screams to run out from your body and probably save your life.
            Your vision went black for a half a second. A litle blood trail was formed from where you nailed your theet, it
            run, reached your elbow. Blood drops dye your chest clothes in a strange pattern.

            In this moment you feel something terrible, maybe even worse than that indescribable pain.
            Maybe the pain was too strong to fell before or maybe you just wanted not to believe in it, but...

            There was SOMETHING moving inside your wound, between your ribs, scratching your lungs.

            You feel an itch, a kinda pressure and then it cames.

            C..CR..CRACK!!

            The sound of another rib being broken was loud, but not louder than your scream. The "thing" is eating you from inside,
            braking your body, drinking your fluids!!!
            You wanted to cry like a baby,  but you stay silent. Tears runs like rivers through your cheeks. Your green eyes are now
            an opaccity dark black.

            If there was noises outside, they don't bother you anymore. There are real importants things to worry about.

            You want to scream again, THAT thing (or things) inside you, is starting to move again. That feeling awake you from your
            panic state.

            You think: I'M GOING TO DIE?!!?!

            You have ONLY ONE option... but you must take it!

            """


# def possible items to get in "DESK"
def desk_item():
    value = random.randrange(1, 100)
    if value <= 5:
        print("You get a very rare item!", value)
        inventory.append(ring0)
        time.sleep(2)
        print("Magic Ring Added to your Inventory")

    elif value > 5 and value <= 10:
        print("You get a normal item!", value)
        inventory.append(ring1)
        time.sleep(2)
        print("Ring Added to your Inventory")

    elif value > 10 and value <= 15:
        print("You get a normal item!", value)
        inventory.append(ring2)
        time.sleep(2)
        print("Ring Added to your Inventory")

    elif value > 15 and value <= 20:
        print("You get a rare item!", value)
        inventory.append(ring3)
        time.sleep(2)
        print("Atack Ring Added to your Inventory")

    elif value > 49:
        print("You get a normal item", value)
        inventory.append(ring4)
        time.sleep(2)
        print("Ring Added to your Inventory")


# Define actions and game for Fisrt Floor
def first_floor():
    for s in ("""

            You are standing at the side of the bed and started to observe the room...
            ROLL A DICE d20 (PRESS ANY KEY): """):
            sys.stdout.write(s)
            sys.stdout.flush()
            time.sleep(0.04)

    input("")
    d20 = random.randint(1, 20)
    print("""
            You get """, d20)

    if d20 > 15:
        for s in ("""
            15+ : Your gaze roams the room very carefully. You see a small old fashioned wardrobe with a mirror, a fireplace and the bed.
            There is also a stair that leads up and a door. You spend some more time observing the room. There is a desk behind you
            and a papper on the ground.

            Press a number betwen 1 and 6.

            """):
            sys.stdout.write(s)
            sys.stdout.flush()
            time.sleep(0.04)

        while len(floor_1_opt_a) > 1:
            print("""Choose a number (1 for 1st option, etc...):
            
            """)
            print("\n".join(floor_1_opt_a))
            try:
                option = int(input())
                if option < 1 or (option - 1) > len(floor_1_opt_a):
                    raise ValueError
                else:
                    act = (floor_1_opt_a[option - 1])
                    if act == "Inspect Wardrobe":
                        player['Name'] = input("You looked at the mirror and remembered your name...Choose a name for your Character: ")
                        print("Your name is: ", player['Name'])
                        player['Gender'] = input("Choose a Gender for your Character: ")
                        print("Your Gender is: ", player['Gender'])
                        floor_1_opt_a.pop(option - 1)
                        inventory.append(clothes)
                        time.sleep(2)
                        print("You've obtained 'Clean Clothes'!")

                    elif act == "Inspect Fireplace":
                        print("""It's a strong magical fire.There's something shining between the embers.
                        
                        """)
                        game_over = input("""Try to pick the shining object?
                        
                        """)
                        if game_over in yes_list:
                            for s in ("""
                                You are on your knees and you move your right hand quickly and try to pick up the object. Before you could reach your objective, your hand
                                stoped in the middle of the air. You tried to move your arm, but it seemed that it no longer belongs to you. Slowly, your arm started
                                to seems heavier and heavier. The magical fire started to petrify your arm, and soon your whole body....
                                
                                """):
                                sys.stdout.write(s)
                                sys.stdout.flush()
                                time.sleep(0.04)
                            print("GAME OVER")
                            the_begining()                            

                        else:
                            print("""You realized that the flames are quite dangerous. Maybe you can find something to put out the fire""")
                            floor_1_opt_a.pop(option - 1)

                    elif act == "Inspect Desk":
                        desk_item()
                        inventory.append(Key)
                        time.sleep(2)
                        print("You've obtained 'Rusted Key'")
                        floor_1_opt_a.pop(option - 1)

                    elif act == "Inspect Old Books":
                        print("""You take a quick look trough the books, but one called your attention. You flip it's pages and found something
                        interesting inside..
                        
                        """)
                        inventory.append(paper)
                        time.sleep(2)
                        print("Blank Paper Added to your Inventory")
                        floor_1_opt_a.pop(option - 1)

                    elif act == "Use the door":
                        if Key in inventory and len(floor_1_opt_a) == 1:
                            print("""You use the keys that you found and tried to open the door. For a second, you thought if you really wanted to leave
                            the place. With no regreats, you turned the door knob and left the house. For the first time in a long time (a time that you
                            don't know how long it was), you saw the stars and felt the wind. You remembered who you are, and now you have to find out what
                            in the hell you are doing here.

                            CONGRATULATIONS YOU WIN!
                            """)
                            break
                            the_begining()
                        else:
                            print("You Still can't open this door.")

            except ValueError:
                print("""Please choose a valid Number:
                
                """)

    else:
        for s in ("""
            1 - 15: Your gaze roams the room. You see a small old fashioned wardrobe with a mirror, a fireplace and the bed. There is also a
            stair that leads up and a door. Maybe you're missing something in the desk behind you, but you don't want to touch that place again.

            Press the corresponding number 1 to 4:

            """):
            sys.stdout.write(s)
            sys.stdout.flush()
            time.sleep(0.04)

        while len(floor_1_opt_b) > 1:
            print("""Choose a number (1 for 1st option, etc...):
            
            """)
            print("\n".join(floor_1_opt_b))
            try:
                option = int(input())
                if option < 1 or (option - 1) > len(floor_1_opt_b):
                    raise ValueError
                else:
                    act = (floor_1_opt_b[option - 1])
                    if act == "Inspect Wardrobe":
                        player['Name'] = input("You looked at the mirror and remembered your name...Choose a name for your Character: ")
                        print("Your name is: ", player['Name'])
                        player['Gender'] = input("Choose a Gender for your Character: ")
                        print("Your Gender is: ", player['Gender'])
                        floor_1_opt_b.pop(option - 1)
                        inventory.append(clothes)
                        time.sleep(2)
                        print("You've obtained 'Clean Clothes'!")

                    elif act == "Inspect Fireplace":
                        print("""It's a strong magical fire.There's something shining between the embers.""")
                        game_over = input("Try to pick the shining object?")
                        if game_over in yes_list:
                            print("""You are on your knees and you move your right hand quickly and try to pick up the object. Before you could reach your objective, your hand
                            stoped in the middle of the air. You tried to move your arm, but it seemed that it no longer belongs to you. Slowly, your arm started
                            to seems heavier and heavier. The magical fire started to petrify your arm, and soon your whole body....""")
                            print("GAME OVER")
                            the_begining()
                        else:
                            print("""You realized that the flames are quite dangerous. Maybe you can find something to put out the fire""")
                            floor_1_opt_b.pop(option - 1)

                    elif act == "Inspect Desk":
                        desk_item()
                        inventory.append(Key)
                        time.sleep(2)
                        print("You've obtained 'Rusted Key'")
                        floor_1_opt_a.pop(option - 1)

                    elif act == "Use the door":
                        if Key in inventory and len(floor_1_opt_b) == 1:
                            print("""You use the keys that you found and tried to open the door. For a second, you thought if you really wanted to leave
                            the place. With no regreats, you turned the door knob and left the house. For the first time in a long time (a time that you
                            don't know how long it was), you saw the stars and felt the wind. You remembered who you are, and now you have to find out what
                            in the hell you are doing here.

                            CONGRATULATIONS YOU WIN!
                            """)
                            break
                            the_begining()
                        else:
                            print("You Still can't open this door.")

            except ValueError:
                print("Please choose a valid Number:")

# Def the begining of the game


def the_begining():

    restart()
    answer = input("Start a New Game? ")

    if answer in yes_list:
        # print(welcome)
        for e in welcome:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.04)

        decision = input("""Use Scroll Heal Massive Wounds?
            """)

        while decision not in yes_list:
            decision = input("""Use Scroll Heal Massive Wounds? """)

        if decision in yes_list:
            for s in situation_1:
                sys.stdout.write(s)
                sys.stdout.flush()
                time.sleep(0.04)

            input("""ROLL A DICE d20 (PRESS ANY KEY): """)
            d20 = random.randint(1,20)
            print("""
            You get """, d20)

            if d20 > 11:
                for s in dice_1st_floor_a:
                    sys.stdout.write(s)
                    sys.stdout.flush()
                    time.sleep(0.04)

                time.sleep(2)
                print("Your current Hp is: ", player['Health'])

                first_floor()

            if d20 < 12:
                player['Health'] -= 1
                for s in dice_1st_floor_b:
                    sys.stdout.write(s)
                    sys.stdout.flush()
                    time.sleep(0.04)

                time.sleep(2)
                print("Your current Hp is: ", player['Health'])

                first_floor()

    else:
        return


the_begining()
