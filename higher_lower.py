import game_data
import random
c=random.randint(0,49)
c1=random.randint(0,49)
count=0
count1=0
total_points=0
first_pick={}
second_pick={}
game_lost=False
if(c1==c):
    c1=random.randint(0,49)
def initial_call(c,c1):
    global count
    global count1,first_pick,second_pick
    name1=game_data.data[c]
    name2=game_data.data[c1]
    first_pick=name1
    second_pick=name2
    count=name1['follower_count']
    count1=name2['follower_count']
    print("")
    print(f"The name is : {name1['name']}\nDescription : {name1['description']}\nCountry : {name1['country']}")
    print("")
    print(f"The name is : {name2['name']}\nDescription : {name2['description']}\nCountry : {name2['country']}")
def next_turn_A(c):
    global c1
    c1=random.randint(0,49)
    if(c==c1):
        c1=random.randint(0,49)
    initial_call(c,c1)
def next_turn_B(c1):
    global c
    c=random.randint(0,49)
    if(c==c1):
        c=random.randint(0,49)
    initial_call(c,c1)


    

initial_call(c,c1)
while(game_lost==False):
    print(f"{count} {count1}")
    guess=input("Enter A for the first or B for the second\n")
    if(count>count1 and guess=="A"):
        print("You have got it correct")
        next_turn_A(c)
        total_points+=1
        print(f"Your score is {total_points}")
    elif(count1>count and guess=="B"):
        print("You have got it correct")
        next_turn_B(c1)
        total_points+=1
        print(f"Your score is {total_points}")
    else:
        print("You have guessed it wrong")
        print("You have lost the game")
        print(f"Your total score is {total_points}")
        game_lost=True