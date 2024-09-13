# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:20:20 2024

@author: logan
@function: This is the main driver for the console output
"""

def menu(selection):
#Where to go based on selection    
    match selection:
    #Public User Menu
        case 1:
            #Public User Page (Not Implemented)
            print(1)
    #Key Owner Menu
        case 2:
            #Key Owner Page (Not Implemented)
            print(2)
    #Exit Program
        case 3:
            quit()
            
            
            
            
#Main of Sorts
#I/O Console First Part Output
#While loop is to reshow if an improper selection is input
selection = 4
while (selection > 3 or selection < 1):
    print("RSA keys have been generated.")
    print("Please select your user type: ")
    print("       1. A public user")
    print("       2. The owner of the keys")
    print("       3. Exit program")
    selection = int(input("Enter your choice: "))
menu(selection)


        




