import random
import time

Close=["You can do it, go lower!","Get a bit closer..","Getting there...","Almost there!", "Closer!"]
Far=["You're far..","Colder than snow.","Dang you're cold."]
Medium=["50/50 cold and hot!","You're in between of both.","You're getting closer."]

while True:
    try:
        print()
        time.sleep(1)
        THEALMIGHTYNUMBER = random.randint(1,50)
        listofallnumbertries = []
        chance = 0
        decision = input("What mode do you want to play?\n\n1. 5 Chances of Hell\n2. Unlimited chances\n\nType here: ")
        if decision == "1":
            print("")
            time.sleep(1)
            print("Alright, you have 5 guesses, use them wisely, good luck!")
            
            while chance < 5:
                time.sleep(1)
                print("")
                guess = int(input("What is your guess?"))
                distance = abs(THEALMIGHTYNUMBER - guess)
                
                if distance >= 40:
                    print("")

                    time.sleep(1)
                    print(Far[random.randint(0,2)])
                
                elif distance >= 30:
                    print("")
                    time.sleep(1)
                    print(Medium[random.randint(0,2)])
                
                elif distance >= 20:
                    print("")
                    time.sleep(1)
                    print(Medium[random.randint(0,2)])
                
                elif distance >= 10:
                    print("")
                    time.sleep(1)
                    print(Medium[random.randint(0,2)])

                
                elif guess == THEALMIGHTYNUMBER:
                    print("")
                    time.sleep(1)
                    print("Congratulations you guessed the number correctly!")
                    print("")
                    time.sleep(1)
                    print(f"The number was {THEALMIGHTYNUMBER}!")
                    break
                    

                chance += 1


                if chance == 5:
                    print("")
                    time.sleep(1)
                    print("Too bad, you couldn't guess the number")
                    print("")
                    time.sleep(1)
                    print(f"The number was {THEALMIGHTYNUMBER}, goodbye!")
                    print("")
                    time.sleep(1)
                    exit()
        
        elif decision == "2":
            print("")
            time.sleep(1)
            print("Alright, you have unlimited guesses, use them wisely, good luck!")
            
            while True:
                time.sleep(1)
                print("")
                guess = int(input("What is your guess?"))
                if distance >= 40:
                    print("")
                    time.sleep(1)
                    print(Far[random.randint(0,2)])
                
                elif distance >= 30:
                    print("")
                    time.sleep(1)
                    print(Medium[random.randint(0,2)])
                
                elif distance >= 20:
                    print("")
                    time.sleep(1)
                    print(Medium[random.randint(0,2)])
                
                elif distance >= 10:
                    print("")
                    time.sleep(1)
                    print(Medium[random.randint(0,4)])

                elif guess == THEALMIGHTYNUMBER:
                    print("")
                    time.sleep(1)
                    print("Congratulations you guessed the number correctly!")
                    print("")
                    time.sleep(1)
                    print(f"The number was {THEALMIGHTYNUMBER}!")
                    print(f"You guessed {listofallnumbertries}.")
                    break               

        else:
            print("")
            time.sleep(1)
            print("That's not an option, retry.")
            continue


    except ValueError as e:
        print("")
        time.sleep(1)
        print(f"Something went wrong: {e}.")
        continue