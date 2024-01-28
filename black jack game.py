#This program is designed for playing the black jack game
#Rules are two cards are drawn at random for the user and 1 card is drawn by the dealer 
#Closest to 21 wins the game and any amount of drawns is given but the closest to 21 wins 
#If the sum goes over 21 then the game is over automatically
import random as rp
card=[11,2,3,4,5,6,7,8,9,10,10,10]
user=[]
user_t=0
dealer=[]
dealer_t=0
choice="y"
con=True
for i in range(0,2):
    c=rp.randint(0,11)
    user.append(card[c])
    user_t=user_t+card[c]
c1=rp.randint(0,11)
dealer.append(card[c1])
dealer_t=dealer_t+card[c1]

def user_next_turn():
    c=rp.randint(0,11)
    user.append(card[c])
    print(user)
    return card[c] 

while(choice=="y" and user_t<=21):
    print(f"Your cards are {user} \nThe dealer's first card is {dealer[0]} Do you wish to draw more cards.\nIf yes press 'y' else press 'n'")
    choice=input().lower()
    if(choice=='y'):
        y=user_next_turn()
        user_t=user_t+y
        print(user_t)

while(dealer_t<=21 and con==True):
    cd=rp.randint(0,11)
    dealer_t=dealer_t+card[cd]
    dealer.append(card[cd])
    if(dealer_t>21):
        dealer_t-=card[cd]
        dealer.remove(card[cd])
    if(dealer_t>=17):
        con=False
if(user_t>21):
    print("YOU LOSE")
    print(f"Your total cards are {user} \nTotal sum is {user_t}")
    print(f"Dealers total cards are {dealer} \nTotal sum is {dealer_t}")
if(user_t<=21):
    print(f"Your total cards are {user} \nTotal sum is {user_t}")
    print(f"Dealers total cards are {dealer} \nTotal sum is {dealer_t}")
    if(user_t>dealer_t):
        if(user_t==21):
            print("YOU HIT A BLACK JACK")
        print("YOU WIN")
    elif(user_t<dealer_t):
        if(dealer_t==21):
            print("DELAER HIT A BLACK JACK")
        print("DEALER WINS")
    elif(user_t==dealer_t):
        print("ITS A DRAW")

    

   






