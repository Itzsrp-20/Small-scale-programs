#This program is a calculator program used to do basic  mathematical operations
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("Enter a number \n"))

choice="y"
ans=0
y=0
def calc(a):
    ch=input(f"+\n-\n*\n\\\n")
    b=int(input("Enter the next number\n"))
   
    if(ch=="+"):
        y=add(a,b)
    elif(ch=="-"):
        y=sub(a,b)
    elif(ch=="*"):
        y=multi(a,b)
    elif(ch=="\\"):
        y=div(a,b)
    else:
        print("Enter a correct operation")
    
    
    return y
while(choice=="y"):
    choice=input("if you want to continue operation enter y else enter n\n")
    if(choice=="y"):
        ans=calc(a)
        a=ans
        print(ans)
    else:
        print(ans)


    