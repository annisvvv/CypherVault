import os
import hashlib
from cryptography.fernet import Fernet
from Encryption import hash_master_password

def profilcheckcreation():
    stored_master_password_file_type = "mstrps.bin"
    log = False
    while log == False:
        x = input('do you have an account (y,n) : ')
        if x == 'y':
            
            if not os.path.exists(stored_master_password_file_type):
                print("No accounts exist. Please create a new account.")
                
            elif os.path.exists(stored_master_password_file_type):
                #logg = False
                #while logg == False:
                master_password = input("Provide us your master password: ")

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
                                    login_person = person_part + ".txt"  # Create filename like "person 1.txt"
                                    print("You are logged in")
                                    return login_person
                                
                    if not found_match :
                        print('no match for your password. try another password or create a new account if you havant')
                                    
                                #elif hashed_password != stored_hash:
                                    #print("This account does not exist, check your password or create a new account if you haven't.")
                                    #logg = False
                                    
        
        elif x == 'n':
            print("Enter the master password, be careful only you have to know it!")
            master_password = input("Master password: ")

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
                                    print("This password exists, you are logged in!")
                                    return login_person
    
            # Create new account
            hash_master_password(master_password, stored_master_password_file_type)
            print("Account created.")
    
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
                                login_person = person_part + ".txt"
                                print("You are logged in!")
                                return login_person
    
            print('A problem just occurred :( . retry')

            log = 1
        else:
            print('you did a mistake. retry')