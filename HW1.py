import time

shipName = "Homework"
captain = "Mike"
location = "Pacific Ocean"
password = "Noclass"
count = 0

pAttempt = input("Enter the password:")
for i in range(0, 3): 
    if pAttempt != password:
        print("password incorrect")
        pAttempt = input("Enter the password:")
        count += 1
    if count == 2:
        print("You are not the captain, go away!")
        break
    if pAttempt == password:
        print("Password correct. Welcome to the ship " + shipName)

        print('')
        print('This ' + shipName + " is ready the " + location + ', ' + captain + ", please give the order.")

        choice = ""
        a_choice = ''
        while True: 
            if choice != '/exit':
                print("What would you like to do, " + captain + "?")
                print("")
                print("a. Set off immediately") #即刻出發
                print("b. Change course") #更改航道
                print("/exit to cancel sailing")
                print("")
                choice = input("Enter your choice: ")
            if choice == 'a':
                print ('3')
                time.sleep(1)
                print('2')
                time.sleep(1)
                print('1')
                print('Let we Go!')
                time.sleep(3)
                print(captain + ", what should we do next?")
                print('')
                print('a. Fighter take-off reconnaissance')#戰鬥機起飛偵查
                print('b. Launch missiles')#發射導彈
                print('c. Attack Japan') #進攻日本
                print('d. End the voyage') #結束航行
                a_chioce = input("Enter your chioce: ")
                if a_chioce == 'a':
                    print('3')
                    time.sleep(1)
                    print('2')
                    time.sleep(1)
                    print('1')
                    print('Fighter take-off!')
                    time.sleep(2)
                    print("Let's go home!")
                    time.sleep(2)
                    print(captain + " see you next time!")
                    break  
                elif a_chioce == 'b':
                    print('3')
                    time.sleep(1)
                    print('2')
                    time.sleep(1)
                    print('1')
                    print('Launch missiles!')
                    time.sleep(2)
                    print("Let's go home!")
                    time.sleep(2)
                    print(captain + " see you next time!")
                    break  
                elif a_chioce == 'c':
                    print("This is unwise, let's go home" )
                    time.sleep(2)
                    print(captain + " see you next time!")
                    break  
                elif a_chioce == 'd':
                    print("Let's go home!")
                    time.sleep(2)
                    print(captain + " see you next time!")
                    break  

            if choice == 'b':
                print(captain + " where to go?")
                time.sleep(1)
                print("a. Atlantic Ocean")
                print("b. Indian Ocean")
                print("c. Arctic Ocean")
                print('d. Southern Ocean')
                new_location = input("Enter a location: ")
                if new_location == 'a':
                    time.sleep(2)
                    print('Ok, ' + captain + " let's go to the Atlantic Ocean now")
                if new_location == 'b':
                    time.sleep(2)
                    print('Ok, ' + captain + " let's go to the Indian Ocean now")
                if new_location == 'c':
                    time.sleep(2)
                    print('Ok, ' + captain + " let's go to the Arctic Ocean now")
                if new_location == 'd':
                    time.sleep(2)
                    print('Ok, ' + captain + " let's go to the Southern Ocean now")    
                choice = 'a' 
            if choice == "/exit":
                print(captain + " see you next time!")
                break  
        break  
            
        
