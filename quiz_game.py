answer=input("Ready to start? (yes/no) ")
if answer.lower()!="yes":
	quit()
print("Get ready!! Lets play :)\n")
	
score=0

answer=input("1.What is the full form of CPU?	")
if answer.lower()=="central processing unit":
	print("Congrats! You got 1 point for this question.\n")
	score+=1
else:
	print("sorry.That wasn't correct. The right answer is central processing unit\n")
	
answer=input("2.What is the full form of GPU?	")
if answer.lower()=="graphics processing unit":
	print("Congrats! You got 1 point for this question.\n")
	score+=1
else:
	print("sorry.That wasn't correct. The right answer is graphics processing unit\n")
	
answer=input("3.What is the full form of RAM?	")
if answer.lower()=="random access memory":
	print("Congrats! You got 1 point for this question.\n")
	score+=1
else:
	print("sorry.That wasn't correct. The right answer is random access memory\n")
	
answer=input("4.What is the full form of ROM?	")
if answer.lower()=="read only memory":
	print("Congrats! You got 1 point for this question.\n")
	score+=1
else:
	print("sorry.That wasn't correct. The right answer is read only memory\n")

answer=input("5.What is the full form of PSU?	")
if answer.lower()=="power supply unit":
	print("Congrats! You got 1 point for this question.\n")
	score+=1
else:
	print("sorry.That wasn't correct. The right answer is power supply unit\n")
	
print(f"Thankyou for attending the quiz.\nYou got {score}(out of 5) questions correct.")
print(f"Your score is {score/5 *100}%")
