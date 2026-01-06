import datetime
def get_date():
    return datetime.datetime.now()
    
def log_food():
    food=input("enter the food you ate:")
    with open("food.txt","a") as f:
        f.write(str(get_date())+":"+food+"\n")
    print("record added sucessfully")
def exercise_log():
    exercise=input("enter the exercise you did")
    with open ("exercise.txt","a") as f:
        f.write(str(get_date())+":"+exercise+"\n")
    print("exercise record added sucessfully")
def view_food():
    try:
        print("food record")
        with open ("food.txt","r") as f:
            print(f.read())
    except:
        print("no record found")
def view_exercise():
    try:
        print("exercise records")
        with open("exercise.txt")as f:
            print(f.read())
    except:
        print("no record for exercises found")
while True:
    print("\n====== Health Logger ======")
    print("1. Log Food")
    print("2. Log Exercise")
    print("3. View Food Records")
    print("4. View Exercise Records")
    print("5. Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        log_food()
    elif ch==2:
        exercise_log()
    elif ch==3:
        view_food()
    elif ch==4:
        view_exercise()
    else:
        break
