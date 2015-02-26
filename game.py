import random

def randomOpt():
	options = ['Rock', 'Paper', 'Scissors']
	arbitrary = random.randint(0,2)
	return options[arbitrary]
	
print
print("|-----------> Welcome to ROCK, PAPER, SCISSORS <-----------|")
print
print("You have 3 rounds")
for i in range(0,3):
	print
	print("**ROUND "+str(i+1)+"**")
	while(True):
		try:
			print("1) Rock")
			print("2) Paper")
			print("3) Scissors")
			user = raw_input("Choose one: ")
			user = int(user)
			if(user>=1 and user<=3):
				break
			else:
				print("Option not available. Please, choose the number of the available options")
		except:	
			print("Option not available. Please, choose the number of the available options")

	if user == 1: #User -> Rock
		randomValue = randomOpt()
		if randomValue == 'Rock':
			print ("Oh...try again")
		elif randomValue == 'Paper':
			print ("Oh...try again")
		else:
			print ("YOU WIN!!")
			break
	elif user == 2: #User -> Paper
		randomValue = randomOpt()
		if randomValue == 'Rock':
			print ("YOU WIN!!")
			break
		elif randomValue == 'Paper':
			print ("Oh...try again")
		else:
			print ("Oh...try again")	
	elif user == 3: #User -> Scissors
		randomValue = randomOpt()
		if randomValue == 'Rock':
			print ("Oh...try again")
		elif randomValue == 'Paper':
			print ("YOU WIN!!")
			break
		else:
			print ("Oh...try again")
