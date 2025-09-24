import os
import base64
import hashlib
from cryptography.fernet import Fernet

stored_password_file_type = "strdpss.bin"
stored_master_password_file_type = "mstrps.bin"
key_file = "ky.bin"

# Hash the master password, this is the password used to login to the password manager.
def hash_master_password(master_password, stored_master_password_file_type):

    '''sha256 encryption used'''

    data = master_password.encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(data)
    hashed_password = hasher.hexdigest()

    # Find current count (x)
    if os.path.exists(stored_master_password_file_type):
        with open(stored_master_password_file_type, "rb") as f:
            lines = f.readlines()
        x = len(lines)   # number of existing records
    else:
        x = 0

    x += 1  # increment for the new entry

    with open(stored_master_password_file_type, "ab") as f:
        f.write(f"persson {x}, {hashed_password}\n".encode('utf-8'))

# The saved password will be encrypted beforr being stored.
def encrypt_stored_password(password, key_file):

    if os.path.exists(key_file):
        with open(key_file, "rb") as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)

    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))

    encrypted_password_b64 = base64.b64encode(encrypted_password).decode('utf-8')
    return encrypted_password_b64
    #return encrypted_password

# The saved password will be decrypted for usage.
def decrypt_stored_password(encrypted_password_b64, key_file):
    with open(key_file, "rb") as f:
        key = f.read()
    f = Fernet(key)
    
    encrypted_password = base64.b64decode(encrypted_password_b64.encode('utf-8'))
    decrypted_message = f.decrypt(encrypted_password)
    return decrypted_message.decode('utf-8')