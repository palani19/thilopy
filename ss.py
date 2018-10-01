import random
count=0
while(count<=100):
	a=input("enter r to roll the dice")
	if a=='r':
		r=random.randint(1,6)
		print(r)
		count=count+r
		print("score is",count)
		if(count==100):
			print("you win")
			print("your score is ",count)
		elif(count==8):
			count=37
			print("you have climbed the ladder")
		elif(count==11):
			print("oops!!!")
			print("you have a snake bite")
			count=2
		elif(count==13):
			count=34
			print("you have climbed the ladder")
		elif(count==25):
			print("you have a snake bite")
			count=4
		elif(count==38):
			print("oops!!!")
			print("you have a snake bite")
			count=9
		elif(count==40):
			print("you have climbed the ladder")
			count=68
		elif(count==52):
			print("you have climbed the ladder")
			count=81
		elif(count==65):
			print("oops!!!")
			print("you have a snake bite")
			count=46
		elif(count==76):
			print("you have climbed the ladder")	
			count=97
		elif(count==89):
			print("oops!!!")
			print("you have a snake bite")
			count=70
		elif(count==93):
			print("oops!!!")
			print("you have a snake bite")
			count=64
	else:
		break	