import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np

def decimal2binary(dec_number):
    input_binary = bin(dec_number).replace("0b", "")
    TM_binary = str('110') + input_binary + str('110')
    return TM_binary

def even_or_odd(number):
    if number % 2 == 0:
        return 0
    else:
        return 1

def Penrose_coding(number):
    output=[]
    binary_number = decimal2binary(number)
    TM_list = [int(x) for x in (binary_number)]
    current_state = 0
    count_state = 0
    new_state = []
    TM_decode = []
    fail = False
    while len(TM_list)!=0:
        bin_current_state =bin(current_state).replace("0b","")
        bin_new_input = even_or_odd(count_state)
        if (TM_list[0] == 0) & (len(TM_list) >= 1):
            TM_decode.append(0)
            new_state.append(0)
            del TM_list[0]
        elif (TM_list[0] == 1) & (TM_list[1] == 0) & (len(TM_list) >= 2):
            TM_decode.append(1)
            new_state.append(1)
            del TM_list[0:2]
        elif (TM_list[0] == 1) & (TM_list[1] == 1) & (TM_list[2] == 0) & (len(TM_list) >= 3):
            TM_decode.append('R')
            if (len(new_state) == 0):
                new_state.append(0)
                new_state.append(0)
            output.append(str(bin_current_state) + str(bin_new_input) + ' -> '  + ''.join(str(x) for x in new_state) + 'R')
            count_state = count_state + 1
            new_state.clear()
            del TM_list[0:3]
            if (even_or_odd(count_state) == 0):
                current_state = current_state + 1
        elif (TM_list[0] == 1) & (TM_list[1] == 1) & (TM_list[2] == 1) & (TM_list[3] == 0) & (len(TM_list) >= 4):
            TM_decode.append('L')
            if (len(new_state) == 0):
                new_state.append(0)
                new_state.append(0)
            output.append(str(bin_current_state) + str(bin_new_input) + ' -> ' + ''.join(str(x) for x in new_state) + 'L')
            count_state = count_state + 1
            new_state.clear()
            del TM_list[0:4]
            if (even_or_odd(count_state) == 0):
                current_state = current_state + 1
        elif (TM_list[0] == 1) & (TM_list[1] == 1) & (TM_list[2] == 1) & (TM_list[3] == 1) & (TM_list[4] == 0) & (len(TM_list) >= 5):
            TM_decode.append('H')
            if (len(new_state) == 0):
                new_state.append(0)
                new_state.append(0)
            output.append(str(bin_current_state) + str(bin_new_input) + ' -> ' + ''.join(str(x) for x in new_state) + 'H')
            count_state = count_state + 1
            new_state.clear()
            del TM_list[0:5]
            if (even_or_odd(count_state) == 0):
                current_state = current_state + 1
        else:
            fail = True
            a=str(bin_current_state) + str(bin_new_input) + ' -> ' + ''.join(str(x) for x in new_state) + '?'
            output.append(a)
            break
    TM_decode_str = [str(x) for x in (TM_decode)]
    return binary_number, TM_decode_str, fail, output
def codificacion(n):
    TM_decimal = n
    binn, tmstr, fail, output = Penrose_coding(TM_decimal)
    if fail==True:
        print("TM not represented correctly \n \t ")
    print('TM converted to binary: ', binn)
    print('TM after Penrose Coding: ', ''.join(tmstr))
    representation={"Instructions from TM": output}
    rep=pd.DataFrame(representation)
    #fi={'TM converted to binary: ': binn, 'TM after Penrose Coding: ': ''.join(tmstr),
    #    "Instructions from TM": output}
    fi=output
    filename=str(n)+".txt"
    with open("universal.txt", 'w') as file:
        file.write(str(fi))
    print(rep)
print(codificacion(int(input("Enter the Turing Machine number in decimal notation: "))))
