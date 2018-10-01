import random
count=0
while(count<=100):
		a=(input("Enter d to roll a dice"))
		if(a=="d"):
			r=random.randint(1,6)
			print(r)
			count=count+r
			print(count)
			if(count==8):
				count=37
				print("u climbed ladder")
			elif(count==11):
				count=2
				print("u had a snake bite")
			elif(count==13):
   				count=34
   				print("u climbed ladder")
   			elif(count==25):
   				count=4
   				print("u had a snake bite")
   			else:
   				break