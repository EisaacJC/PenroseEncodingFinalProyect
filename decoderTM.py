import numpy as np
import pandas as pd
import os
def decimal2binary(dec_number):
    input_binary = bin(dec_number).replace("0b", "")
    #TM_binary = str('110') + input_binary + str('110')
    return input_binary

def expansion(n):
	n=decimal2binary(n)
	n=[int(x) for x in (n)]
	n2=[]
	n2.append(0)
	while len(n)!=0:
		if n[0]==0 & (len(n) >= 1):
			n2.append(0)
			del n[0]
		elif (n[0]==1) & (len(n) >= 1):
			n2.append(1)
			n2.append(0)
			del n[0]
		#print(n)
	n2.append(1)
	n2.append(1)
	n2.append(0)
	return n2

def decoder(lista, cinta):
	estado=0
	movimiento=["L","R","H"]
	cabezal=0

#print(expansion("hola", 2))

for i in algo:
	dictionary[i]={"val1":res1, "val2":res2, "val3":res3}
