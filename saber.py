# IMPORTS
import random
# END IMPORTS

# Define game start
def play():
	name = "Jedi "
	print ("What's your name?")
	name += input ("> ")
	print ("Hello " + name + ". By the way, you're a Jedi now.")
	print ("Congrats on your promotion.")
	print (name + " look out! They're coming through the window!")
	print ("Lord Dawku wants to fight you one on one.")
	print ('Lord Dawku: "What is your weapon of choice?"')
	
	# Define weapon choice
	def choice():
		print ("[G] Gun, [L] Laser or [S] Lightsaber.")
		weapon = input ("> ")

		if weapon == "g" or weapon == "G":
			weapon = "gun"
		elif weapon == "l" or weapon == "L":
			weapon = "laser"
		elif weapon == "s" or weapon == "S":
			weapon = "lightsaber"
		else:
			print ('Lord Dawku: "I SAID PICK A WEAPON!"')
			choice()

		rnumber = random.random()
		if rnumber <= 0.33:
			ldweapon = "gun"
		elif rnumber > 0.33 and rnumber < 0.66:
			ldweapon = "laser"
		else:
			ldweapon = "lightsaber"

		# Define start of fight
		def fight():
			if weapon == ldweapon:
				print("We're too evenly matched with a " + weapon + ".")
				print("Re-choose your weapon and let's try again.")
				choice()
			else:
				if weapon == "gun":
					if ldweapon == "laser":
						print('Lord Dawku: "You thought a ' + weapon + ' would match up to my ' + ldweapon + '?')
						print('You thought wrong and now you die."')
					else:
						print('Lord Dawku: "How did that ancient' + weapon + ' beat my ' + ldweapon + '?')
						print('You have won this time."')
				elif weapon == "laser":
					if ldweapon == "gun":
						print('Lord Dawku: "You are just too fast with your ' + weapon + ".")
						print('My ' + ldweapon + ' stood no chance."')
					else:
						print('Lord Dawku: "Did you really think a ' + weapon + ' would stand up to my ' + ldweapon + '?')
						print('Think again while you die slowly."')
				else:
					if ldweapon == "laser":
						print('Lord Dawku: "You are so strong and fast with that ' + weapon + ".")
						print('I fear my ' + ldweapon + ' and I have suffered defeat."')
					else:
						print('Lord Dawku: "My ' + ldweapon + ' may be old, but ' + weapon +'s do not stop bullets.')
						print('You die to the beat of my boom."')
					#laser beats gun
					#gun beats lightsaber
					#lightsaber beats laser
					
		#Start of fight
		fight()

	# Weapon choice
	choice()

# Start game
play()