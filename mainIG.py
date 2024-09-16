# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:20:20 2024

@author: logan
@function: This is the main driver for the console output
"""

#Generages and tests for 2 pseudo primes p & q
def keyGenerator(n1, n2):
    
    
def getQandP():
    
    
def encrypt(message, pubKey):
#Encypts a message (Output is C)
def decrypt(C, priKey):
#Decrypts crypt Message (Output is M)
def sign(name, priKey):
#Signs a signiture and returns it 
def authent(S, pubKey): 
#Authenticates a owner signeture (Returns M)
            
            
def main():
    #Main of Sorts (Frontend)
    #I/O Console First Part Output
    
    #Call something here to generate keys
    print("RSA keys have been generated.")
    
    #While loop is to reshow if an improper selection is input
    selection = 4
    while (selection > 3 or selection < 1):
        print("Please select your user type: ")
        print("       1. A public user")
        print("       2. The owner of the keys")
        print("       3. Exit program")
        selection = int(input("Enter your choice: "))
        
        #Where to go based on selection    
        match selection:
            #Public User Menu
            case 1:
                print("As a public user, what would you like to do?")
                print("       1. Send an encrypted message")
                print("       2. Authenticate a digital signature")
                print("       3. Exit\n")
                
                #Operation based off User Selection
                pubSelection = int(input("Enter your choice: "))
                match pubSelection:
                    #Sends an encrypted message
                    case 1: 
                        #(Not Implemented)
                    #Authenticates a owner signiture 
                    case 2:
                        #(Not Implemented)
                    #Exits User Menu
                    case 3:
                        #Sets selection to an illegal answer to restart while loop
                        selection = 4
                        break
                    
            #Key Owner Menu
            case 2:
                print("As the owner of the keys, what would you like to do?")
                print("       1. Decrypt a received message")
                print("       2. Digitally sign a message")
                print("       3. Show the keys")
                print("       4. Generating a new set of the keys")
                print("       5. Exit \n")
                
                #Operation based off Owner Selection
                owSelection = int(input("Enter your choice: "))
                match owSelection:
                    #Decrypt Message
                    case 1:
                        #(Not Implemented)
                    #Sign Message
                    case 2:
                        #(Not implemented)
                    #Shows keys
                    case 3:
                        #(Not Implemented)
                    #Generates new keys
                    case 4: 
                        #(Not Implemented)
                    #Exit Owner Menu
                    case 5:
                        selection = 4
                        break 
            
            #Exit Program
            case 3:
                print("Bye for now!")
                quit()


        


#Coding Tips for Project
#Getting a pesudo Primes - p = random.randint(n1,n2), where n1 and 2 are parameters of function
#, to random integers 
#Check for prime - pow(j, p-1, -), where j is random int from random.randint(2, p)
#Do in while loop till it is a pesudo prime 
#Get a prime in a different function than that of getting both q and p. 
#Call first function in second function for both q and p 
#
#pow (a,b,c) is the fast expo function 
#

