num=19
print("you have total 9 try.")
print("game starts")
for i in range (1,10):
    ch=int(input("enter your choice"))
    if ch>num:
        print("the guessed number is larger .")
        print("you left with ",(9-i),"guesses")
    elif ch<num:
        print("the guessed number is smaller.")
        print("you left with ",9-i,"guesses")
    else:
        print("cogo!!!you guessed the number right in ",i,"number of guesses.")
        break
print("game over!")
        
