from random import randint, random
#START METHOD:
#Greets the user in the console and asks if it wants to add a password to
#the registry or if it wants a new one.
#REQUIERMENTS: NONE
def exe():
    print("----WELCOME TO THE PASSWORD GENERATOR----")

    state=input("Would you like to save a new password or do you you want to create a password?\n-S saved password\n-N create password\n")
    if state=='N':
        create()#If the user decides it wants to save a password
    if state=='S':
        save()#If the user wants a password created
#INFO GATHERING METHOD
#Obtains data from the user to create the registry
#It returns a list with this information
#REQUIREMENTS: NONE
def info(state=None):
    data = [] #create list to save data
    #Save each answer in the list
    data.append(input("For what site will this be used for?\n->"))
    data.append(input("What is your user name?\n->"))
    #Indicate that the sistem is generating the password
    if state:
        print("\n\nMaking your new password...\n\n\n")
    return data #Return list of data
#PASSWORD CREATION METHOD
#This method modifies an empty string with randomly selected characters
#and symols to create a secure password with no afiliation to the user.
#REQUIERMENTS:
#Each list of characters and symbols to create the string
def process(lowerLetters,UpperLetters,symbols):
    final='' #Create empty string to store password
    for i in range(30):#Create a password with 30 characters
        key=randint(1,1000)#Chooses a number between 1 and 1000
        #first checks if the number can be devided by 2
        if (key%2)==0:
            #It will add a random character from a specific list of characters
            #depending if the "key" is greater of smaller then 500
            if key<=500:
                #uselower
                temp=lowerLetters[randint(0,len(lowerLetters)-1)] 
                #choose a character without overlapping ammount of characters available
            if key>500:
                #useupper
                temp=UpperLetters[randint(0,len(UpperLetters)-1)]
        else: #If it is not divisible by 2 it will do the same process but with different characters
            if key<=500:
                #useNumber
                temp=str(randint(0,10))
            if key>500:
                #useSymbol
                temp=symbols[randint(0,len(symbols)-1)]

        #Adds selected character to the final string
        final+=temp
    return final#returns the final string (the generated password)
#MAIN METHOD TO CREATE A PASSWORD AND SAVE IT
#It contains the lists to create the password and calls other methods to create and
#store the info obtained by the user in a txt file
#REQUIREMENTS: NONE
def create():
    lowerLetters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UpperLetters=['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols=['|','#','$','&','%','/','-','+','_']
    
    while True:
        #Collect info for the password
        infor=info(True)
        site=str(infor[0])
        user=str(infor[1])
        #Call method to create the password bassed on the avilable lists
        password=process(lowerLetters,UpperLetters,symbols)
        #Print result and ask for another password
        print(f"--------------\nFor:{site}\nUsername:{user}\nPassword:{password}\n-------------")
        print("Would you like to create another password?")
        ans=input("Choose:\n-Y, create a new password\n-N exit\n->")
        
        #save current password and exit
        if ans=='N' or ans=='n':
            ans=input("Do you want to save the current password?\n->")
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
#SAVE PASSWORD IN txt
#Saves de obtained info in a txt file
#Used for the "create password" method
#REQUIREMENTS:
#The name of the site, name of the user in the site and password
def save_password(site, user, password):
    #abrir achivo txt, crearlo si no existe
    try:
        file = open("Password List.txt",'a')
        file.write("--------------")
        file.write("\nFor:"+site)
        file.write("\nUsername: "+user)
        file.write("\nPassword: "+password)
        file.write("\n--------------\n")
        file.close()
    except Exception as e:
        print(f"Error:{e}")
        return False
    return True
#SAVE PASSWORD IN txt #2
#Saves de obtained info in a txt file
#Used for the "save password" method
#REQUIREMENTS: None
def save():
    infor=info()
    site=str(infor[0])
    user=str(infor[1])
    password=input("Enter Password\n->")
    print(f"--------------\nFor:{site}\nUsername:{user}\nPassword:{password}\n-------------")
    state=save_password(site,user,password)
    if state: print("The password was saved successfully\n")
    else: print("!!!!THERE WAS EN ERROR IN PROCESS PLEASE CHECK IF THE FILE IS NOT CURRUPTED OR MISSING!!!!")
    input("Press ENTER to close")

if __name__=='__main__':
    exe()