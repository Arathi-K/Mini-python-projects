#stone paper scissors
import random
options=["stone","paper","scissors"]
comp=0
user=0
print('''Rules:
	Choose "stone"/"paper"/"scissors" to continue playing,
	Or choose "q" to quit the game''')
while comp<5 and user<5:
	print("	Now your point is",user,"and computer's point is",comp)
	choice=input("Enter your choice : ").lower();
	if choice=="q":
		quit()
	if choice not in options:
		continue
	else:
		r=random.randint(0,2)
		print(f"computer chose {options[r]}")
		if r==0 and choice=="paper":
			user+=1
			print("You got 1 point")
		elif r==1 and choice=="scissors":
			user+=1
			print("You got 1 point")
		elif r==2 and choice=="stone":
			user+=1
			print("You got 1 point")
		elif options[r]==choice:
			continue
		else:
			comp+=1
			print("Computer got 1 point")
		
if comp==5:
	print("Computer won this game by",comp-user,"points")
else:
	print("Wohoo!! Congrats!! You won this game by",user-comp,"points")
