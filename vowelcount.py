#this code counts the number of vowels in a word using set() 
mystr=input("input the word:")
def Vowels(str):
    vowel={'a','e','i','o','u'}
    count=0
    for i in str:
        if i in vowel:
            count+=1
    return count
print(Vowels(mystr))
