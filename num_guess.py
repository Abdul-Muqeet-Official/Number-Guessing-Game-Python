import random
x=random.randint(0,11)
print('Computer will guess the number in between 0-10')
turns=int(input("How many turns you need to guess the number :"))
for i in range (turns):
	user_input= int(input("Enter the Number you want to guess."))
	if x==user_input:
		print("You guess right .")
		print("You won")
		break
	elif x>user_input:
		print("your guess is low:")
	elif x<user_input:
		print("your guess is high:")
	else:
		print("Nope :")