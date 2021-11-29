from random import randint, random
#start method
def exe():
    print("----WELCOME TO THE PASSWORD GENERATOR----")

    state=input("Would you like to save a new password or do you you want to create a password?\n-S saved password\n-N create password")
    if state=='N':
        create()
    if state=='S':
        save()

#collect info for new register
def info():
    data = []
    data.append(input("For what site will this be used for?\n->"))
    data.append(input("What is your user name?\n->"))
    print("\n\nMaking your new password...\n\n\n")
    return data
#create the password
def process(lowerLetters,UpperLetters,symbols):
    final=''
    for i in range(30):
        key=randint(1,1000)
        if (key%2)==0:
            if key<=500:
                #uselower
                temp=lowerLetters[randint(0,len(lowerLetters)-1)]
            if key>500:
                #useupper
                temp=UpperLetters[randint(0,len(UpperLetters)-1)]
        else:
            if key<=500:
                #useNumber
                temp=str(randint(0,10))
            if key>500:
                #useSymbol
                temp=symbols[randint(0,len(symbols)-1)]


        final+=temp
    return final

def create():
    lowerLetters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UpperLetters=['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols=['|','#','$','&','%','/','-','+','_']
    
    while True:
        #collect info for the password
        infor=info()
        site=str(infor[0])
        user=str(infor[1])

        #ask for another password
        password=process(lowerLetters,UpperLetters,symbols)
        print("--------------\nFor:",site,"\nUsername: ",user,"\nPassword: ",password,"\n-------------")
        print("Would you like to create another password?")
        ans=input("Choose:\n-Y, create a new password\n-N exit\n->")
        
        #save current password and exit
        if ans=='N' or ans=='n':
            ans=input("Do you want ot save the current password?\n->")
            if ans=='Y' or ans=='y':
                save_password(site,user,password)
                print("The password was saved successfully\n")

            else:
                print("ok...")
                print("Password deleted...\n")
                
            print("---THANKS FOR USING OUR PROGRAM---")
            break
        
        #save created password and create a new one
        if ans=='Y' or ans=='y':
            ans=input("Do you want ot save the current password?\n-Y, create a new password & save current\n-N New password and dont save current\n->")
            if ans=='y' or ans=='Y':
                save_password(site,user,password)
            else:
                print("ok...")
                print("Password deleted...\n")

def save_password(site, user, password):
    #abrir achivo txt, crearlo si no existe
    file=open("./Password List.txt", "a")
    file.write("--------------")
    file.write("\nFor:"+site)
    file.write("\nUsername: "+user)
    file.write("\nPassword: "+password)
    file.write("\n--------------\n")
    file.close()

def save():
    infor=info()
    site=str(infor[0])
    user=str(infor[1])
    password=input("Enter Password\n->")
    print("--------------\nFor:",site,"\nUsername: ",user,"\nPassword: ",password,"\n-------------")
    save_password(site,user,password)
    print("The password was saved successfully\n")
    print("---THANKS FOR USING OUR PROGRAM---")
    
exe()