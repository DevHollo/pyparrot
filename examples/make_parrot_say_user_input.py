from pyparrotsay import ParrotSay

parrot = ParrotSay(rgb=[232,155,23])

to_say = str(input("What do you want the parrot to say? "))

parrot.say(to_say)
