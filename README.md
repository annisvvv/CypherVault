# Password Manager

A secure, command-line password manager built in Python that helps you store, retrieve, and manage your passwords locally with strong encryption.

## 🔐 Features

### Core Functionality
- **Secure Password Storage**: All passwords are encrypted using Fernet encryption (AES 128) before being stored
- **Master Password Authentication**: Protected by a master password using SHA-256 hashing
- **Multiple User Support**: Each user has their own encrypted password file
- **Password Management**: Add, view, search, and delete stored passwords
- **Password Strength Validation**: Built-in password strength checker with customizable requirements

### Security Features
- **AES Encryption**: Uses cryptography library's Fernet for symmetric encryption
- **SHA-256 Hashing**: Master passwords are hashed using SHA-256
- **Base64 Encoding**: Encrypted passwords are Base64 encoded for safe storage
- **Unique Encryption Keys**: Each installation generates its own encryption key
- **File-based Storage**: Passwords stored locally in encrypted format

## 📋 Requirements

```
cryptography>=3.0.0
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/annisvvv/CypherVault.git
cd password-manager
```

2. Install dependencies:
```bash
pip install cryptography
```

3. Run the application:
```bash
python Main.py
```

## 💻 Usage

### First Time Setup
1. Run `python Main.py`
2. Choose 'n' when asked if you have an account
3. Create a strong master password (this will be your main access key)

### Daily Usage
1. Run the application and log in with your master password
2. Choose from the following options:
   - **Add Password (1)**: Store a new password for an application/service
   - **Search Password (2)**: Find a specific password by application name
   - **Delete Password (3)**: Remove a stored password
   - **View All Passwords (4)**: Display all stored passwords
   - **Exit (5)**: Close the application

## 🛡️ Security Implementation

### Encryption Process
1. **Key Generation**: A unique Fernet key is generated and stored in `ky.bin`
2. **Password Encryption**: User passwords are encrypted using the Fernet key
3. **Base64 Encoding**: Encrypted data is Base64 encoded for safe file storage
4. **Master Password Hashing**: Master passwords are SHA-256 hashed for authentication

### File Structure
- `ky.bin`: Contains the encryption key
- `mstrps.bin`: Stores hashed master passwords
- `person X.txt`: Individual user password files (encrypted)

### Password Strength Requirements
- Minimum 14 characters
- At least one lowercase letter
- At least one uppercase letter
- At least one digit
- At least one special character

## 📁 File Structure

```
password-manager/
│
├── Main.py                 # Main application entry point
├── Profil.py              # User profile management and authentication
├── Password_handling.py   # Password CRUD operations
├── Password_strenght.py   # Password strength validation
├── Encryption.py          # Encryption and decryption functions
├── ky.bin                 # Encryption key (generated on first run)
├── mstrps.bin            # Master password hashes
└── person X.txt          # User password files
```

## 🔧 Technical Details

### Core Modules

#### `Main.py`
- Application entry point and main menu loop
- Handles user interaction and menu navigation

#### `Profil.py`
- User account creation and authentication
- Master password verification
- Multi-user support implementation

#### `Password_handling.py`
- Password storage and retrieval operations
- File I/O operations for password data
- Search and delete functionality

#### `Encryption.py`
- Fernet encryption/decryption implementation
- Key generation and management
- Master password hashing

#### `Password_strenght.py`
- Password complexity validation
- Strength requirement enforcement

## 🚀 Roadmap & Future Updates

- [ ] **GUI Interface**: Tkinter or PyQt-based graphical interface
- [ ] **Password Generator**: Built-in secure password generation
- [ ] **Import/Export**: Support for importing from other password managers
- [ ] **Backup & Sync**: Cloud backup functionality
- [ ] **Two-Factor Authentication**: Additional security layer
- [ ] **Browser Integration**: Browser extension support
- [ ] **Mobile App**: Cross-platform mobile application
- [ ] **Advanced Search**: Category-based organization and advanced filtering
- [ ] **Password Sharing**: Secure password sharing between users
- [ ] **Biometric Authentication**: Fingerprint/face recognition support
- [ ] **Security Audit**: Password breach checking and security reports
- [ ] **Auto-fill**: Automatic form filling capabilities
- [ ] **Multi-device Sync**: Seamless synchronization across devices
- [ ] **Team Management**: Organization and team password sharing
- [ ] **API Integration**: REST API for third-party integrations
- [ ] **Advanced Analytics**: Usage statistics and security insights
- [ ] **Plugin System**: Extensible architecture for custom features

## ⚠️ Security Considerations

- **Master Password**: Choose a strong, unique master password - it's your only way to access stored data
- **Backup**: Regularly backup your `ky.bin` and user files
- **Environment**: Use only on trusted devices
- **Updates**: Keep the cryptography library updated for latest security patches

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request

## 🐛 Known Issues

- Password strength checker regex patterns need adjustment (currently using string literals instead of character classes)
- File encoding handling could be improved for better cross-platform compatibility
- Error handling could be more comprehensive

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact the maintainer.

---

**⚠️ Disclaimer**: This password manager is provided as-is. While it implements strong encryption standards, users should evaluate their security requirements and consider professional security audits for critical applications.
