import os
from Banner import typing_print
from cryptography.fernet import Fernet
from Encryption import encrypt_stored_password, decrypt_stored_password

key_file = "ky.bin"
# ready to save encrypted password
def add_password(login_person):

    application = input(typing_print('Enter the application : ', delay=0.05))
    profil_name = input(typing_print('Enter profil name : ', delay=0.05))
    password = input(typing_print('Enter Password : ', delay=0.05))

    typing_print("Encrypting password...\n", delay=0.05)
    encrypted_password = encrypt_stored_password(password, key_file)

    return application, profil_name,encrypted_password

# Save the hashed password into a separate files for every user
def save_file(profil_name, application, login_person, encrypted_password):

    with open (login_person , "a", encoding='utf-8') as f:
        f.write(f"{application},{profil_name},{encrypted_password}\n")
        typing_print('file has been saved', delay=0.05)
        print('\n')

# View all paswords
def view_file(login_person):
    typing_print("Your stored passwords: ", delay=0.05)
    passwords = []
    
    try:
        with open(login_person, "rb") as f:
            for i, line in enumerate(f, start=1):
                line = line.decode('utf-8').strip()
                parts = line.split(',')
                if len(parts) >= 3:
                    app, profile, encrypted_password = parts[0], parts[1], parts[2]
                    decrypted_pass = decrypt_stored_password(encrypted_password, key_file)
                    typing_print(f"Found: App: {app}, Profile: {profile}, Password: {decrypted_pass}", delay=0.001)

    except FileNotFoundError:
        typing_print("No passwords stored yet.", delay=0.05)
        return

def search_password(login_person):
    password_search = input(typing_print("wich app or account name : ", delay=0.05))
    typing_print("\nsearching password... Done\n", delay=0.05)

    if not os.path.exists(login_person):
        typing_print('No password with this acount.\n', delay=0.05)
        return None
    
    
    with open(login_person, "rb") as f:
        for line in f:
            line = line.decode('utf-8').strip()
            if password_search.lower() in line.lower():
                parts = line.split(',')
                if len(parts) >= 3:
                    app, profile, encrypted_password = parts[0], parts[1], parts[2]

                    decrypted_pass = decrypt_stored_password(encrypted_password, key_file)
                    typing_print(f"Found: App: {app}, Profile: {profile}, Password: {decrypted_pass}\n", delay=0.05)
                    
                break
        else:
            typing_print("No matching password found.\n", delay=0.05)

def delect_password(login_person):
    typing_print("\nYour stored passwords:", delay=0.05)
    passwords = []
    
    try:
        with open(login_person, "rb") as f:
            for i, line in enumerate(f, start=1):
                line = line.decode('utf-8').strip()
                parts = line.split(',')
                if len(parts) >= 3:
                    app, profile = parts[0], parts[1]
                    passwords.append(line)
                    typing_print(f"{i} - App: {app}, Profile: {profile}", delay=0.05)
    except FileNotFoundError:
        typing_print("No passwords stored yet.\n", delay=0.05)
        return
    
    if not passwords:
        typing_print("No passwords to delete.\n", delay=0.05)
        return
    
    # Ask which one to delete
    try:
        choice = int(input(typing_print("Enter the number of the password to delete: ", delay=0.05))) - 1
        if 0 <= choice < len(passwords):
            password_to_delete = passwords[choice]
            
            # Remove the selected password from the list
            passwords.pop(choice)
            
            # Rewrite the file without the deleted password
            with open(login_person, "wb") as f:
                for password_line in passwords:
                    f.write(f"{password_line}\n".encode('utf-8'))
            
            typing_print("Deleting password... Done", delay=0.05)
            typing_print("Password deleted successfully!\n", delay=0.05)
        else:
            typing_print("Invalid selection.\n", delay=0.05)
    except ValueError:
        typing_print("Please enter a valid number.\n", delay=0.05)