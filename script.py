# PATRONIMUS'S LAIR

from sys import exit


def main(name):
    print "Wake up?\n\nType \"yes\"\n"
    choice = raw_input("> ").lower()
    if "yes" in choice:
        print "You wake up startled and gasping for air."
        exit(0)
    else:
        print "You should wake up."
        main(name)

# DREAM TUTORIAL: Here the player learns the following commands: -dodge, -attack, -go to PLACE, -search PLACE and -open PLACE. 

def commands(name):
    fail = "\nCome on, this is quite simple. Just follow the instructions in the prompt.\n"
    wake = "YOU GOTTA WAKE UP!"
    punch_dodged = False
    man_ko = False
    at_car = False
    car_opened = False
    cigarettes_found = False
    while True:
        choice = raw_input("> ").lower()

        if "dodge" in choice:
            punch_dodged = True
            print "\nThe drunk man misses and stumbles.\n"
            print "You hear Joe's voice: \"Nice! Now strike him with one of those nasty upercuts you got!\"\n\nType \"attack\" to strike.\n"
        elif "attack" in choice and punch_dodged:
            man_ko = True
            print "\nYou hit him so hard he instantly gets knocked out and falls to the ground.\n"
            print "After this roughed up \"conversation\", you need a cigarette. But where are they?\n"
            print "You can't find them on you so you tell your co-workers you're going to look for them in your car.\n"
            print "Type \"go to PLACE\" to move the character to the car.\n"
        elif "go to" in choice and "car" in choice and punch_dodged and man_ko:
            at_car = True
            print "\nType \"open PLACE\" to open your car.\n"
        elif "open" in choice and ("car" in choice or "door" in choice or "car door" in choice) and punch_dodged and man_ko and at_car:
            car_opened = True 
            print "\nYou open the car, searching for the cigarette pack."
            print "\nYou now remember your cigarettes are in the glovebox."
            print "\nType \"search PLACE\" to search.\n"
        elif "open" in choice and "trunk" in choice and punch_dodged and man_ko and at_car:
            print "\nThe trunk is closed and you know for sure the cigarettes are in the car."
        elif "search" in choice and "glovebox" in choice and punch_dodged and man_ko and at_car and car_opened:
            cigarettes_found = True
            print "\nYou find the cigarettes."
            print "\nType \"grab\" to grab the cigarettes and light one.\n" 
        elif "search" in choice and "trunk" in choice and punch_dodged and man_ko and at_car and car_opened:
            print "\nThe trunk is closed and you know for sure the cigarettes are in the glovebox.\n"
            print "Type \"search PLACE\" to search."
        elif "grab" in choice and punch_dodged and man_ko and at_car and cigarettes_found:
            print "\nYou light a cigarette."
            print "As you inhale the smoke you ease up a little. \"This job sucks.\" you think to yourself.\n"
            print "You hear a familiar voice: \"So how've you been %s?\"\n" % name
            scroll = raw_input("Press the ENTER KEY to keep scrolling.\n\n> ")
            print "\nYou turn to your right and on the passenger seat is Joe. Your jaw drops."
            print "You just can't understand what he's doing in your car. He's eating a slice of pizza as usual.\n"
            print "\"Joe?! What on earth are you doing here? How did you get in my car?! You died like 4 years ago!\""
            print "He grins at you and says: \"Tell me about it! There's no pizza up there!\""
            print "He bites into the slice of pizza and continues: \"I'm here to tell you something..."
            print "\nThis makes no sense to you. You listen, confused and unable to speak.\n"
            keep_scrolling = raw_input("\nPress the ENTER KEY to keep scrolling.\n\n> ")
            print "\n\"I'm here to tell you that you gotta wake up!\"\n"
            print "You stay silent.\n"
            print "\"You gotta wake up %s!\"" % name
            print "\nHis eyes turn black and his teeth seem to be sharp as razors..."
            print "A twisted smile appears on his face as he screams louder and louder:\n\"YOU GOTTA WAKE UP!\"\n\n"
            print "He starts vigorously agitating his arms and starts lascerating you while repeatidly shouting:\n\n\"%s %s %s\"\n\n" % (wake, wake, wake)
            main(name)
        elif not "attack" in choice and punch_dodged:
            print "%s" % fail
            print "Type \"attack\" to strike.\n"
        elif not "go to" in choice and punch_dodged and man_ko:
            print "But WHERE do you want to go?"
            print "%s" % fail
            print "Type \"go to PLACE\" to go to the car.\n"
        elif "go to" in choice and "club" in choice and punch_dodged and man_ko:
            print "This is not the time!"
            print "%s" % fail
            print "Type \"go to PLACE\" to go to the car.\n"
        elif not "open" in choice and (not "car" in choice or "door" in choice) and punch_dodged and man_ko and at_car:
            print "%s" % fail
            print "Type \"open PLACE\" to open the car.\n"
        elif not "search" in choice and not "glovebox" in choice and punch_dodged and man_ko and at_car and car_opened:
            print "%s" % fail
            print "Type \"search PLACE\" to search.\n" 
        else:
            print "\nThe man hits you with a hard punch and aims for another one."
            print "%s" % fail
            print "Type \"dodge\" to avoid getting punched.\n"

def dream():
    print """\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n\nOn a late thursday night in front of the Shogun club were you work as a bouncer, a guy who obviously has had too many drinks starts being aggressive with you.\nHe drunkenly asks you:\n\n"What's your name buddy?"\n """

    name = raw_input("> ")
    print "\n\"And how much time have you been a bouncer here? I've never seen your face before.\""
    print "You answer: \"I moved here a couple of months ago with my...\""
    print "He barely listens and starts arguing: \"Why won't you let me in man? My daughter's in there you know.\"\n"
    print "You calmly respond that he's too drunk to enter, and that maybe he souldn't be going out with his daughter on a weekday.\n"
    print "\"And who the hell are you to be telling me what to do?\""
    print "You patiently answer: \"I'm the guy that has the power to let you in or not.\"\n"
    scroll = raw_input("\nPress ENTER KEY to keep scrolling.\n\n> ")
    print "\nYou've apparently made him mad, and he clumsily tries to punch you.\n"
    print "At that moment, you remember Joe, your gym trainer, back in your boxing career days, screaming at you while fighting in the ring: \"Dodge the first blow %s!\"\n" % name
    print "Type \"dodge\" to avoid getting punched.\n"
    commands(name)


def death(why):
    print why
    print "You died...\n\nGAME OVER\n\n\n"
    main(name)

def start():
    print """\nWelcome to PATRONIMUS'S LAIR !\n
    Instructions : Read carefully the prompt.\n
    Enter commands when "> " is displayed.\n
    Thanks for playing! Good luck and have fun!\n"""
    dream()

start()   
