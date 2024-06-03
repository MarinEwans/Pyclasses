#this code checks if the number of 'X's are equal to numbers of 'O's
def Counter(string):
    count_x = 0
    count_o = 0
    string = string.lower()
    
    for i in string:
        if i == 'x':
            count_x += 1
        elif i == 'o':
            count_o += 1
    
    # If there are no x's and o's in the string, return True
    if count_x == 0 and count_o == 0:
        return True
    
    # Return True if counts of x and o are equal, otherwise False
    return count_x == count_o

string = input("Input your string: ")
print(Counter(string))

#the other method using dictionary

def X_and_O(string):
    string =string.lower()
    count_dict={'x':0, 'o':0}
    for i in string:
      if i=='x' or i=='o':
        count_dict[i]+=1
    if count_dict['x']==0 and count_dict['o']==0:
        return True
    elif count_dict['x']==count_dict['o']:
        return True
    else:
        return False
string = input("enter string:")
print(X_and_O(string))