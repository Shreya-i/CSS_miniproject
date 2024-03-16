list = ['hello','vidyalankar','computer','science']
cipher=['hoell','vakiylnadar','cuoptrme','sncecie']

import random
R = 3
print("key is 3")
word= random.choice(list)
w_index=list.index(word)
c_check = cipher[w_index]
C = len(word)
end_of_game=False
matrix = []
end_of_game= False
dir_down = None
row, col = 0, 0
result= []
for i in range(R):		 
	a =[]
	for j in range(C):	
		s=str(j)
		t=str(i)
		a.append(t+s+'-')
		
	matrix.append(a)

for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()

print(f"word to encrypt {word}")
l_len=len(word)
print(l_len)
c=0
live = 3
while not end_of_game:

	print("enter the index number from matrix to put letter to encrypt")
	num=str(input())
	print("enter the letter")
	letter = input().lower()
	for i in range(R):
		for j in range(C):
			if(matrix[i][j]== num+'-'):
				matrix[i][j]=letter+'  '
				c=c+1
			if(c==l_len):
				end_of_game = True
			print(matrix[i][j], end= "  ")
			
		    
		print( )
for i in range(R):
	for j in range(C):
		ii=str(i)
		jj=str(j)
		if(matrix[i][j] != '\n'and matrix[i][j] != ii+jj+'-'):
			result.append(matrix[i][j])
r= ""
r= r.join(result)

r=r.replace(' ','')
print(f"your answer = {r}")
print(f"correct answer = {c_check}")
if(r==c_check):
	print("you win")
else:
	print("you lose")
