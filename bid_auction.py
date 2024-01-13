print("WELCOME TO THE SECRET AUCTION ")
auc={}
max=0
name=""
def auc_list():
    name=input("enter the name of the bidder\n")
    bid=int(input("enter the bid amount\n"))
    auc[name]=bid


next_bidder=True
while next_bidder==True:
    
    auc_list()
    a=input("Enter 'yes' if there are any other bidders left else enter 'no'\n").lower()
    if(a=="yes"):
        next_bidder=True
    else:
        next_bidder=False

for key in auc:
    if(auc[key]>max):
        max=auc[key]
        name=key
print(f"the highest bidder is {name}")
print(f"the highest bid is {max}")