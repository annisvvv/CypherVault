import os
from Banner import typing_print
import hashlib
from cryptography.fernet import Fernet
from Encryption import hash_master_password

def profilcheckcreation():
    stored_master_password_file_type = "mstrps.bin"
    log = False
    while log == False:
        x = input(typing_print('Do you have an account (y,n) : ', delay=0.05)).lower()
        print('\n')
        if x == 'y':
            
            if not os.path.exists(stored_master_password_file_type):
                typing_print("No accounts exist. Please create a new account.\n", delay=0.05)
                
            elif os.path.exists(stored_master_password_file_type):
                #logg = False
                #while logg == False:
                typing_print('Provide us with your mester password : ', delay=0.05)
                master_password = input()

                data = master_password.encode('utf-8')
                hasher = hashlib.sha256()
                hasher.update(data)
                hashed_password = hasher.hexdigest()

                with open(stored_master_password_file_type, "rb") as login:
                    found_match = False
                    for line in login:
                        line = line.decode('utf-8').strip()
                        if line:  # Skip empty lines
                            parts = line.split(', ')
                            if len(parts) >= 2:
                                person_part = parts[0]  # "person 1"
                                stored_hash = parts[1]  # the hash
            
                                if hashed_password == stored_hash:
                                    login_person = person_part + ".bin"  # Create filename like "person 1.txt"
                                    typing_print('login in... Done\n', delay=0.05)
                                    return login_person
                                
                    if not found_match :
                        typing_print('\nno match for your password. try another password or create a new account if you havent.\n', delay=0.05)
                                    
                                #elif hashed_password != stored_hash:
                                    #print("This account does not exist, check your password or create a new account if you haven't.")
                                    #logg = False
                                    
        
        elif x == 'n':
            typing_print("Enter the master password, be careful only you have to know it!", delay=0.05)
            master_password = input(typing_print('Masterpassword : ', delay=0.05))

            data = master_password.encode('utf-8')
            hasher = hashlib.sha256()
            hasher.update(data)
            hashed_password = hasher.hexdigest()
    
            # Check if this password already exists
            if os.path.exists(stored_master_password_file_type):
                with open(stored_master_password_file_type, "rb") as login:
                    for line in login:
                        line = line.decode('utf-8').strip()
                        if line:  # Skip empty lines
                            parts = line.split(', ')
                            if len(parts) >= 2:
                                person_part = parts[0]  # "person 1"
                                stored_hash = parts[1]  # the hash
                        
                                if hashed_password == stored_hash:
                                    login_person = person_part + ".txt"
                                    typing_print("This password exists, you are logged in!", delay=0.05)
                                    return login_person
    
            # Create new account
            hash_master_password(master_password, stored_master_password_file_type)
            typing_print("Account creation... Done", delay=0.05)
    
            # Find the person number that was just created
            with open(stored_master_password_file_type, "rb") as login:
                for line in login:
                    line = line.decode('utf-8').strip()
                    if line:  # Skip empty lines
                        parts = line.split(', ')
                        if len(parts) >= 2:
                            person_part = parts[0]  # "person 1"
                            stored_hash = parts[1]  # the hash
                    
                            if hashed_password == stored_hash:
                                login_person = person_part + ".bin"
                                typing_print("login in... Done\n", delay=0.05)
                                return login_person
    
            typing_print("A problem just occurred :( .Retry", delay=0.05)

            log = 1
        else:
            typing_print("A problem just occurred :( .Retry", delay=0.05)