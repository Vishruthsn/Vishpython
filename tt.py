a=[1,2,3,4,5,6,7,8,9]
def table():
	print("------------")
	print("|",a[0],"|",a[1],"|",a[2],"|")
	print("------------")
	print("|",a[3],"|",a[4],"|",a[5],"|")
	print("------------")
	print("|",a[6],"|",a[7],"|",a[8],"|")

playerone=True
while True:
	table()
	p=int(input("Enter a value to select position "))
	if(p in a):
		if(a[int(p)-1]=="X" or a[int(p)-1]=="O"):
			print("place taken, choose another place...")
			continue
		else:
			if playerone:
				print("player one >>")
				a[int(p)-1]="X"
				playerone=not playerone
			else:
		   	    print("player two >>")
		  		a[int(p)-1]="O"
				playerone=not playerone
		   	for i in(0,3,6,)
		   		if(a[i]==a[i+1] and a[i]==a[i+1]):
		   			print("Game over")
		   			exit()
		   	for i in range(3):
		   		if(a[i]==a[i+3] and a[i]==a[i+6]):
		   		 	print("Game over")
		   		 	exit()
		   		if(a[0]==a[4] and a[0]==a[8]):
		   			print("Game over")
		   			exit()
		   		if(a[2]==a[4] and a[2]==a[6]):
		   			print("Game over")
		   			exit()
	
		  
