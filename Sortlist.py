#write a function that takes 2 parameters list of numbers and the order they must be sorted 'asc', 'desc' or none
#if the order is not specified return the orginal list
numbers=[20,64,1,5,17,81]
order=input("input the order in which the list will be sorted; 'asc','desc':")
def Bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def Rev_Bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr



def List_Sort(numbers,order):
    if order=='asc':
        print(Bubble(numbers))
    elif order=='desc':
        print(Rev_Bubble(numbers))
    else:
        print(numbers)

print(List_Sort(numbers,order))