 #convert decimal number into binary
mynum=int(input("input the decimal number:"))
def Binary_Converter(mynum):
    binary_num=[]
    while mynum>0:
        remainder=mynum %  2
        binary_num.append(remainder)
        mynum = mynum//2 
        binary_num.reverse()
        binary_string=''.join(map(str, binary_num))
    return binary_string
#binary_string=''.join(map(str, binary_number))
print("the binary representation:", Binary_Converter(mynum))