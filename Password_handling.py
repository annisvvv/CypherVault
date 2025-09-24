import os
from cryptography.fernet import Fernet
from Encryption import encrypt_stored_password, decrypt_stored_password

key_file = "ky.bin"
# ready to save encrypted password
def add_password(login_person):

    application = input('Enter the application : ')
    profil_name = input('Enter profil name : ')
    password = input('Enter Password : ')

    print("Encrypting password...")
    encrypted_password = encrypt_stored_password(password, key_file)

    return application, profil_name,encrypted_password

# Save the hashed password into a separate files for every user
def save_file(profil_name, application, login_person, encrypted_password):

    with open (login_person , "a", encoding='utf-8') as f:
        f.write(f"{application},{profil_name},{encrypted_password}\n")
        print('file has been saved')

# View all paswords (not finished yet desyncription!!!!!)
def view_file(login_person):
#    try:
#        with open(login_person, "rb") as f:
#            for i, line in enumerate(f, start=1):
#                line = line.decode('utf-8').strip()
#                print(f"{i} - {line}")
#    except FileNotFoundError:
#        print("No passwords stored yet.")
    print("\nYour stored passwords:")
    passwords = []
    
    try:
        with open(login_person, "rb") as f:
            for i, line in enumerate(f, start=1):
                line = line.decode('utf-8').strip()
                parts = line.split(',')
                if len(parts) >= 3:
                    app, profile, encrypted_password = parts[0], parts[1], parts[2]
                    decrypted_pass = decrypt_stored_password(encrypted_password, key_file)
                    print(f"Found: App: {app}, Profile: {profile}, Password: {decrypted_pass}")

    except FileNotFoundError:
        print("No passwords stored yet.")
        return

def search_password(login_person):
    print("searching password")
    password_search = input("wich app or account name : ")

    if not os.path.exists(login_person):
        print('no password with this acount')
        return None
    
    
    with open(login_person, "rb") as f:
        for line in f:
            line = line.decode('utf-8').strip()
            if password_search.lower() in line.lower():
                parts = line.split(',')
                if len(parts) >= 3:
                    app, profile, encrypted_password = parts[0], parts[1], parts[2]

                    decrypted_pass = decrypt_stored_password(encrypted_password, key_file)
                    print(f"Found: App: {app}, Profile: {profile}, Password: {decrypted_pass}")
                    
                break
        else:
            print("No matching password found.")

def delect_password(login_person):
    print("\nYour stored passwords:")
    passwords = []
    
    try:
        with open(login_person, "rb") as f:
            for i, line in enumerate(f, start=1):
                line = line.decode('utf-8').strip()
                parts = line.split(',')
                if len(parts) >= 3:
                    app, profile = parts[0], parts[1]
                    passwords.append(line)
                    print(f"{i} - App: {app}, Profile: {profile}")
    except FileNotFoundError:
        print("No passwords stored yet.")
        return
    
    if not passwords:
        print("No passwords to delete.")
        return
    
    # Ask which one to delete
    try:
        choice = int(input("Enter the number of the password to delete: ")) - 1
        if 0 <= choice < len(passwords):
            password_to_delete = passwords[choice]
            
            # Remove the selected password from the list
            passwords.pop(choice)
            
            # Rewrite the file without the deleted password
            with open(login_person, "wb") as f:
                for password_line in passwords:
                    f.write(f"{password_line}\n".encode('utf-8'))
            
            print("Password deleted successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")