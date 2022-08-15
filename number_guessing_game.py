import random
l=input("Give the lower limit(non-negative) here: ")
if not l.isdigit():
	print("Invalid lower limt. Please enter a number next time.")
	quit()

h=input(f"Give the upper limit (greater than {l}) here: ")
if not h.isdigit():
	print("Invalid upper limt. Please enter a number next time")
	quit()
if int(l)>int(h):
	print(f"Invalid upper limt. Please enter a number greater than or equal to {l}")
	quit()
	
l=int(l)
h=int(h)
r=random.randint(l,h)


count=0
while True:
	count+=1
	guess=input(f"Guess a number between {l} and {h} : ")
	if guess.isdigit():
		guess=int(guess)
	else:
		print("Please enter a number next time")
		continue
	if guess==r:
		print("You got it!!")
		break
	elif guess>r:
		print("You were above the number!")
	else:
		print("You were below the number!")

print("You got it in",count,"guesses")	# since it is "___",count,"___" it automatically adds space in front and at the end of count variable.
	
