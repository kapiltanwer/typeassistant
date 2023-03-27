import pyttsx3        #=========>(pyttsx3)  is module used to enable speak function

import datetime      #====used to enable time function

engine = pyttsx3.init('sapi5')      #==========>> inbuilt speak funnction of pc


voices=engine.getProperty('voices')                 ####======> two default voices (male,female)





engine.setProperty('voice',voices[1].id)

def speak(audio):       #### to use engine we will def speak function
    engine.say(audio)   ### used to say command
    engine.runAndWait()
    

def wishme():          #========>>>> all this is used to say time
    hour= int(datetime.datetime.now().hour)
    Command=input("ENTER WHAT DO YOU WANT = ")
    if Command=="time":
        if hour >=0 and hour<12:
            speak("good morning")
            speak(hour)
            print("Your Time is {} ".format(hour))
            speak("To run  program again please press shfit and enter")
        elif hour>=12 and hour<18:
            speak("good afternoon")
            speak(hour)
            print("Your Time is {} ".format(hour))
            speak("To run  program again please press shfit and enter")
            
            
            
            
        else:
            print("Your Time is {} ".format(hour))
            speak(hour)
            speak("good evening")
            print("Your time is {} ".format(hour))
            speak("To run  program again please press shfit and enter")
            
    elif Command=="game":    ######3=====>>> alll the code is of game
        print("GAME START ")
        start=input("Type 'start' to continue game ")
        if start==start:       ### start the game
            print("----RULES----")
            print("1_Answer The Question wisely")
            print("2_WRONG Answer will give you penalty")
            from playsound import playsound
            playsound('C:\\Users\\admin\\Desktop\\Among Us Role Sound Effect.mp3')###====>.. 1st tune
            from playsound import playsound
            playsound("C:\\Users\\admin\\Desktop\\technical_guruji - Copy.mp3") ####3=====>>>>  2ND TUNE
    
        k=0
        while k<=5:
            Question_1=int(input("---GREATEST THREE DIGIT NUMBER--- "))
            if Question_1==999:
                print()
                print("-OKAY NICE TRY--")  ########======>>> QUESTION 1
                k=k+1
            else:
                print("GAME OVER")
                speak("game over")
                speak("To run  program again please press shfit and enter")
                break
            Question_2=int(input(" WHAT IS 2 + 2 = "))
            if Question_2==4:
                print("WELL DONE")
                k=k+2
            else: 
                print("Game over")
                speak("game over")
                speak("To run  program again please press shfit and enter")
                break
            Question_3=input("what is 4**2 = ")
            if Question_3==16:
                print("NICE")
                k=k+1
            else:
                speak("game over")
                print("Game over")
                speak("To run  program again please press shfit and enter")
                break
    elif Command=="reverse":
        speak("Enter your number")
        number=int(input("ENTER YOUR NUMBER"))
        k=len(str(number))
        l=1
        rev=0
        while l<=k:
            m=number%10
            rev=(rev*10)+m
            number=number//10
            l=l+1
        print(rev)
        speak("The reverse number  is{}".format(rev))
    elif Command=="stone":
        import random
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "paper":
                if computer_action == "rock":
                    print("Paper covers rock! You win!")
                else:
                    print("Scissors cuts paper! You lose.")
        elif user_action == "scissors":
                if computer_action == "paper":
                    print("Scissors cuts paper! You win!")
                else:
                        print("Rock smashes scissors! You lose.")
 
        
if _name== "main_" :
    speak("What do you want sir")
    wishme()


