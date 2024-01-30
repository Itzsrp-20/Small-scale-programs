"""Program to create a game where the computer picks a random number between 1 to 100 and
based on the difficulty gives the user no of tries to guess the number"""
import random 
print("") 
print("WELCOME TO NUMBER GUESSER".center(100))
print("")
print("Thinking of a number between 1 to 100".center(100))
print("")
print("Enter difficulty".center(100))
print("Enter 'easy' for easy difficulty".center(100))
print("Enter 'hard' for hard difficulty".center(100))
print("")
diff=input().lower()
random_num=random.randint(1,100)
guess_num=0
tries=-1
win=False
if(diff=="easy"):
    tries=10
    print(f"You have {tries} tries")
elif(diff=="hard"):
    tries=5
    print(f"You have {tries} tries")
else:
    print("Enter valid difficulty")
def guess():
    global guess_num
    global tries
    global win
    guess_num=int(input("enter guessed number\n"))
    if(guess_num>random_num):
        print("TOO HIGH")
        tries -=1
        print(f"You have {tries} left")
    elif(guess_num<random_num):
        print("TOO LOW")
        tries -=1
        print(f"You have {tries} left")
    else:
        print("CONGRATULATIONS YOU HAVE GUESSED IT")
        win=True
    

while(tries>0 and win==False):
    guess()
if(tries==0 and win==False):
    print("YOU HAVE LOST ALL TRIES")