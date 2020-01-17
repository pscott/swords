username = raw_input("What's your name? ")
coins = 1000
knife_price = 5
axe_price = 12
sword_price = 15

print "\nYou've got %s gold coins remaining %s.\n" % (coins, username)
print "Let's go through the weapons I sell one by one:"

print "How many knives would you like to buy?"
num_knives = int(input('%s gold per knife: ' % knife_price))

print "How many axes would you like to buy?"
num_axes = int(input('%s gold per axe: ' % axe_price))

print "How many swords would you like to buy?"
num_swords = int(input('%s gold per sword: ' % sword_price))

print "Ok, you want to buy %s knives, %s axes and %s swords." % (num_knives, num_axes, num_swords)

def compute_cost(num_knives, num_axes, num_swords):
    cost = num_knives * knife_price + num_swords * sword_price + num_axes * axe_price
    return cost

def remainder(initial_coins, purchase_cost):
    return initial_coins - purchase_cost

purchase_cost = compute_cost(num_knives, num_axes, num_swords)
print "Sooo... That'll be %s gold coins." % purchase_cost

coins_left = remainder(coins, purchase_cost)
print "You've got %s coins left %s.\n" % (coins_left, username)
print "Thanks for stopping by!"
