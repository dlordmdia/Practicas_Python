import time
import os
import random
import webbrowser
play = True
wrong = True

while  play:
    numerorand = random.randint(1, 10)
    wrong = True
    while wrong:
        start = input("-x to Exit | Which is the number? (from 1-10)\n- ")
        
        if start == "x":
            play = False
            wrong = False

        elif int(start) == numerorand:
            print("You guessed it! Nice one!")
            time.sleep(1)
            wrong = False
            os.system('cls' if os.name=='nt' else 'clear')
            print("New Game!\n")
        
        else:
            if int(start) > numerorand:
                print("!!WRONG!! The number is LOWER than yours.")
                time.sleep(1.5)
                print("PUNISHMENT!!!!")
                time.sleep(1)
                webbrowser.open("https://www.youtube.com/watch?v=poa_QBvtIBA")
                os.system('cls' if os.name=='nt' else 'clear')
            else:
                print("!!Try Again!! The number is HIGHER than yours.")
                time.sleep(1.5)
                os.system('cls' if os.name=='nt' else 'clear')

            wrong = True
