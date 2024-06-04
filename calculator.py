#a function that gets 3 parameters '+','-','*','/' , two others are numbers the it returns mathematical calculations
arg1=float(input("enter first number:"))
arg2=float(input("enter second number:"))
operation=input("enter the operation:")
def Calculator(arg1, operation,arg2):
   if operation=='+':
     return arg1+arg2
   elif operation=='-':
     return arg1-arg2
   elif operation=='/':
     return arg1 / arg2
   elif operation=='*':
     return arg1 * arg2
print(Calculator(arg1,operation,arg2))