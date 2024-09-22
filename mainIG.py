# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:20:20 2024

@author: logan
@function: This is the main driver for the console output
"""
import random, math

#Brute force test for QandP function to absolutly confirm prime identity 
#Credit also due to the slides 
#Input: p - Pseudo prime to test
#Output: boolean true or false 
def testPrime_brute_force(p):
    if p == 2:
        return True
    else:
        for b in range(2, math.floor(math.sqrt(p))):
            if math.gcd(p, b) > 1:
                return False
            else:
                continue
        return True

#Fast Expo from code in blackboard
def fastExpo(a, p, n):
    Y = 1
    while p > 0:
        if p % 2 == 0:
            a = (a * a) % n
            p = p/2
        else:
            Y = (a * Y) % n
            p = p - 1
    return Y
#GCD
#used in key generator to get public key e
#Input: a,b: Integers to find GCD of
#Output a: GDC
def gcd(a, b):
    if b== 0:
        return a
    else:
        return gcd(b, a%b)

#Extended Eucidean
#Input a, b: Integers to test
#Output 3 Integers needed for other things ig
def extended_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

#Generages and tests for 2 pseudo primes p & q    
#Input: n1, n2: two large integers
#        k: a constant integer
#Output: p - a pesudo prime 
def createPrime(n1, n2, k): 
    p = random.randint(n1, n2)
    #Extra Security 
    while p%2*p%3*p%5*p%7*p%11*p%13*p%17 == 0:
        p = random.randint(n1, n2)
    #Fermat Test I think 
    #Credit: Off Slides to find the pseudo prime 
    _prime = False
    while not _prime:
        for i in range(k):
            j = random.randint(2, p)
            if fastExpo(j, p-1, p) > 1:
                p = random.randint(n1, n2)
                break
        _prime = True
    return p
        
#Notes from lecture about creating pseudo primes and slides 
#Input: n1, n2: two large integers
#       k: constant integer
#Output n: n = pq
#       e: public key
#       d: private key
def keyGenerator(n1, n2, k):
    #Get p
    p = createPrime(n1,n2,k)
    while not testPrime_brute_force(p):
        p = createPrime(n1, n2, k)
        
    #Get q
    q = createPrime(n1,n2,k)
    while not testPrime_brute_force(q):
        q = createPrime(n1, n2, k)
    
    #Get n and phi_n
    n = q * p
    phi_n = (q-1)*(p-1)
    
    #Get public key e = gcd(e, phi_n) = 1
    e = random.randint(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n)
    
    #Get private key d = Inverse of e in Zphi (ed mod phi_n = 1)
    de = extended_gcd(e, phi_n)
    d = de[2] % phi_n
    
    #formatted to fit encryption and decryption inputs from flow chart
    return (n, e), (n, d)

#Encypts a message (Output is C)
#Input: m: Message
#       (n,e): Public key
#Output: c: Encrypted Message 
def encrypt(message, pubKey):
    n, e = pubKey
    #Weird calls here had to be looked up in order to 
    # switch from string to integer and back for proper encryption
    enChars = []
    for char in message:
        charIntForm = ord(char)
        encryptedCharInt = fastExpo(charIntForm, e, n)
        enChars.append(encryptedCharInt.to_bytes((encryptedCharInt.bit_length()+7)//8, 'big'))
    return b''.join(enChars)



#Decrypts a message (Output is C)
#Input: m: Message
#       (n,d): Private key
#Output: c: Decrpted Message
def decrypt(C, priKey):
    '''
    n, d = priKey
    CByteForm = int.from_bytes(C, 'big')
    requiredBytes = (n.bit_length() + 7) // 8
    message = fastExpo(CByteForm, d, n)
    return message.to_bytes((requiredBytes.bit_length() + 7) // 8, 'big').decode('utf-8')
    '''
    n, d = priKey
    decChars = []
    for enCharBytes in C.split(b'\x00'):
        if enCharBytes:
            enCharInt = int.from_bytes(enCharBytes, 'big')
            deCharInt = fastExpo(enCharInt, d, n)
            decChars.append(chr(deCharInt))
            
    return ''.join(decChars)
    
    

    
#Decrypts crypt Message (Output is M)
def sign(name, priKey):
    #Signs a signiture and returns it 
    n, d = priKey
    # Simplified signing without hashing for this prototype
    messageByteForm = int.from_bytes(name.encode('utf-8'), 'big')
    signature = fastExpo(messageByteForm, d, n)
    return signature.to_bytes((signature.bit_length() + 7) // 8, 'big')
def authent(S, pubKey): 
#Authenticates a owner signeture (Returns M)
    n, e = pubKey
    SByteForm = int.from_bytes(S, 'big')
    decrypByte = fastExpo(SByteForm, e, n)  # Decrypt the signature
    return decrypByte

def main():
    #Main of Sorts (Frontend)
    #I/O Console First Part Output
    #Needed Variables 
    n1 = 123
    n2 = 123
    k = 100
    encMesgs = []
    signatures = {}
    pubKey, priKey = keyGenerator(n1, n2, k)
    #Call something here to generate keys
    print("RSA keys have been generated.")
    conti = True
    while(conti):
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
                            userMessage = input("Enter a message: ")
                            encMesgs.append(encrypt(userMessage, pubKey))
                            print("Message encrpyted and sent.")
                            #Authenticates a owner signiture 
                        case 2:
                            if len(signatures) == 0:
                                print("There are no signatures to authenticate.")
                                break
                            else:
                                for i in range(len(signatures)):
                                    print("{i+1}. {signatures[i]}")
                            whSig = int(input("\nEnter your choice: ")) - 1
                            message = list(signatures.keys())[whSig]
                            signature = signatures[message]
                            decryptedBytes = authent(signature, pubKey)
                            originalBytes = int.from_bytes(message.encode('utf-8'), 'big')
                            if decryptedBytes == originalBytes:
                                print("Signature is valid.")
                            else:
                                print("Signature is invalid.")
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
                            if len(encMesgs) == 0:
                                print("There are no messages to decrypt.")
                            else:
                                for i,C in enumerate(encMesgs):  
                                    print(f"{i + 1}. (length = {len(C)})")

                                while True:
                                    try:
                                        choice = int(input("Enter your choice: ")) - 1
                                        if 0 <= choice < len(encMesgs):
                                            break
                                        else:
                                            print("Invalid choice! Please enter a number between 1 and", len(encMesgs))
                                    except ValueError:
                                        print("Invalid input! Please enter a number.")

                                try:
                                    deMesg = decrypt(encMesgs[choice], priKey)
                                    print(f"Decrypted message: {deMesg.upper()}")
                                except (ValueError, IndexError):
                                    print("Invalid choice! Please try again.")  
            
                        #Sign Message
                        case 2:
                              message = input("Enter a message to sign: ")
                              signature = sign(message, priKey)
                              signatures[message] = signature
                              print("Message signed.")
                        #Shows keys
                        case 3:
                            print(f"Public key: \n {pubKey}")
                            print(f"Private key: \n {priKey}")
                        #Generates new keys
                        case 4: 
                            n1 = random.randint(1000, 10000)
                            n2 = random.randint(1000, 10000)
                            k = 100
                            pubKey, priKey = keyGenerator(n1, n2, k)
                            encMesgs.clear()
                            signatures.clear()
                            print("New keys generated.")
                        #Exit Owner Menu
                        case 5:
                            selection = 4
                            break 
                        
                    #Exit Program
                case 3:
                    print("Bye for now!")
                    conti = False
                    quit()
                    


        
main()

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

