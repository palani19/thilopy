a=int(input("Enter a value for a"))
b=int(input("Enter a value for b"))
c=int(input("Enter a value for c"))
#comparing 3 nos.
if(a>b and a>c):
	print(a,"is greater than b and c")
elif(b>c):
	print(b,"is greater than a and c")
else:
	print(c,"is greater than a and b")