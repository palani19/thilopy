while True:
	a=(input("Enter some character"))
	if(a=="r"):
		import random
		r=random.randint(25,30)
		print("Banglore temperature is ",r)
	else:
		print("Bye")
		break