# pwFile = open("accounts.txt", "r")
userExists = 0

while userExists <= 0:
    answer = input("welcome to Gelos portal would you like to: login(l), create an account(c)?")

    if answer == "l":
        username = input("enter your username ")
        password = input("enter your password ")
    
        with open('accounts.txt', 'r') as pwFile:
            for line in pwFile:
                u,p = line.strip().split(",")
            if username == u and password == p:
                userExists = 1
                loggedIn = True
                print("success")
                break
            else:
                    print("fail")

    elif answer == "c":
        username = input("enter your prefered username ")
        password = input("enter your preferred password ")

        with open('accounts.txt', 'a') as pwFile:
            pwFile.write(username + "," + password + "\n")
            print("success")
            userExists = -1
            pwFile.close
            
        
    else:
        print("try again")

while loggedIn == True and userExists == 1:
    response = input("Would you like a list of users? yes/no")
    if response == "yes":
        with open('accounts.txt', 'r') as pwFile:
            for lines in pwFile:
                u,p = lines.strip().split(",")
                print(u)
                break
    else:
        print("Have a nice day!")
        break