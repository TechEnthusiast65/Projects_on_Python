from time import *
import random as r
def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error+1
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,user_input):
    time_delay = time_e - time_s
    time_R = round(time_delay / 60, 2)  # convert time delay to minutes
    word_count = len(user_input.split())
    speed = word_count / time_R
    return round(speed, 2)

while True:
    chk=input("Are you ready to start the test? Yes/No ")
    chk1=chk.lower()
    if chk1=="yes":
        test=["the quick brown fox jumped over the lazy dog","Now that you have a feeling for the keyboard and typing easy words, you will move on to full sentences with capitalization.","Take your time and focus on keeping your eyes off of your keyboard!"]
        test1=r.choice(test)
        print("     ***** Typing Speed Calculator *****     ")
        print("---------------------------------------------")
        print(test1)
        print()
        print()
        time_1=time()
        testinput=input("Enter your texts below:\n") 
        time_2=time()

        print("Speed : ",speed_time(time_1,time_2,testinput),"words/min[WPM]")
        print("Error(s)",mistake(test1,testinput))
    elif chk1=="no":
        print("Thank you for visiting!")
        break
    else:
        print("Wrong Input! Please enter valid input in the form of Yes/No")