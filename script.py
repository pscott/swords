username = raw_input("What's your name? ")
coins = 1000

print "\nYou've got %s gold coins remaining %s.\n" % (coins, username)
print "Let's go through the weapons I sell one by one:"

print "How many knives would you like to buy?"
knives = int(input('5 gold per knife: '))

print "How many axes would you like to buy?"
axes = int(input('12 gold per axe: '))

print "How many swords would you like to buy?"
swords = int(input('15 gold per sword: '))

print "Ok, you want to buy %s knives, %s axes and %s swords." % (knives, axes, swords)

def buy(knives, axes, swords):
    cost = knives + swords + axes
    print "Sooo... That'll be %s gold coins." % cost
    coins_left = coins - cost
    print "You've got %s coins left %s.\n" % (coins_left, username)

buy(knives * 5, axes * 12, swords * 15)
print "Thanks for stopping by!"
