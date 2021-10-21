#defining cmp
def cmp(a,b):
	return (a>b)-(a<b)


print("*****************************")
print("*3x3 sliding puzzle game")
print("*type w for sliding up")
print("*type s for sliding down")
print("*type d for sliding right")
print("*type a for sliding left")
print("*type giveup if you wish to discontinue")
print("******************************")
print("")
print("*type the parts of the puzzle [remember the numbers should be from 1-8, and dont forget to leave a space] ")
a=[]
s=[]

#input
# need to add a condition to identify numbers and a check if numbers are <9 

for i in range(3):
	e=input()
	s=[]
	for j in e:
		s.append(j)
	a.append(s)	

ci=4
cj=4
def prnt():
	global cj,ci
	for i in range(3):
	     for j in range(3):
		     print("|",a[i][j], end='|')
		     if a[i][j]==' ':
	     		ci=i
	     		cj=j
	     print()
	print()     
	
	     

prnt()
#print("ci=",ci,"cj=",cj)

prfta=[['1','2','3'],['4','5','6'],['7','8',' ']]  
#condition check

def check():
	global ci , cj
	if cmp(a,prfta)==0 :
	     print("********Perfect!!!!!******")
	     return False
	if  ci==4 :
		print("Sorry but you cant solve this puzzle")
		return False

	else :
		return True
	     
def right(a):
	global cj
	if cj!=0:
		t=a[cj-1]
		a[cj-1]=' '
		a[cj]=t

def left(a):
	global cj
	if cj!=2:
		t=a[cj+1]
		a[cj+1]=' '
		a[cj]=t



while check():
	prnt()
	#print("ci=",ci,"cj=",cj)
	cm=input()
	if cm=='d':
		right(a[ci])

	if cm=='a' :
		left(a[ci])

	if cm=='w':
		#global ci , cj
		if ci!=2:
			t=a[ci+1][cj]
			a[ci+1][cj]=' '
			a[ci][cj]=t

	if cm=='s' :
		#global ci, cj
		if ci!=0:
			t=a[ci-1][cj]
			a[ci-1][cj]=' '
			a[ci][cj]=t
	if cm=='giveup':
		print("Its not a good habit!!!")
		break
			






