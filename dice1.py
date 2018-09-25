while True:
	a=(input("Enter some character"))
	if(a=="r"):
		import random
		r=random.randint(1,6)
		print(r)
	else:
		print("Bye")
		break