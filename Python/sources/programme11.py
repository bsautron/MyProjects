# -*- coding: utf-8 -*-
# Programme tableau

import random
from scipy import *


def affiche_tableau(x1,y1):
	for y in range(y1):
		for x in range(x1):
			print t[y,x],
		print
		
def remplir_tableau(x1,y1):
	for y in range(y1):
		for x in range(x1):
			nb = random.randint(0,10)
			t[y,x] = nb
		
	

t=zeros([8,10],int)   # t[y,x] y=8 et x=10                     
                                
t[0,] = [0,0,0,0,0,0,0,0,0,0]
t[1,] = [0,0,0,0,0,0,0,0,0,0]
t[2,] = [0,0,0,0,0,0,0,0,0,0]
t[3,] = [0,0,0,0,0,0,0,0,0,0]
t[4,] = [0,0,0,0,0,0,0,0,0,0]
t[5,] = [0,0,0,0,0,0,0,0,0,0]
t[6,] = [0,0,0,0,0,0,0,0,0,0]
t[7,] = [0,0,0,0,0,0,0,0,0,0]


affiche_tableau(10,8)   # x=10 et y=8 
print
remplir_tableau(10,8)
affiche_tableau(10,8)




	





                              