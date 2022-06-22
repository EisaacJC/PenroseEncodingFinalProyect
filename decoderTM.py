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
a=pd.read_csv("procesado.csv", header=None)
a.columns=(["Si","Read","Write","Move","Si+1"])
idx=(a.index[a["Move"]=="H"])
a.loc[idx,"Si+1"]="H"
a.loc[idx,"Move"]="R"
def run_utm(
        state = None,
        blank = None,
        rules = [],
        tape = [],
        halt = None,
        pos = 0):
    cinta=[]
    st = state
    if not tape: tape = [blank]
    if pos < 0: pos += len(tape)
    if pos >= len(tape) or pos < 0: raise "bad init position"
    
    rules = dict(((str(s0), str(v0)), (str(v1), str(dr), str(s1))) for (s0, v0, v1, dr, s1) in rules)
    
    while True:
        print(st, '\t', end=" ")
        for i, v in enumerate(tape):
            if i == pos: print("[%s]" % (v,), end=" ")
            else: print(v, end=" ")
        print()
        if st == halt: break
        if (st, tape[pos]) not in rules: break
        (v1, dr, s1) = rules[(st, tape[pos])]
        tape[pos] = v1
        if dr == 'L':
            if pos > 0: pos -= 1
            else: tape.insert(0, blank)
        if dr == 'R':
            pos += 1
            if pos >= len(tape): tape.append(blank) 
        st = s1
ejecucion=run_utm(
    halt = 'H',
	state = '0',
	blank = '0',
    tape=list(map(str,expansion(4))),
	rules = map(tuple,a.round(0).values.tolist()))
print(ejecucion)