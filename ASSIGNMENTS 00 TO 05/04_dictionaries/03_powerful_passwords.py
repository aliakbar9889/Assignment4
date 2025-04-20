# 03_powerful_passwords

import hashlib

print('PowerFull Password')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Store hashed passwords
stored_login = {
    'user1@example.com': hash_password('1234'),
    'user2@example.com': hash_password('25154'),
    'user3@example.com': hash_password('124578')
}

def login(email, password):
    if email in stored_login:
        return stored_login[email] == hash_password(password)
    else:
        print('Invalid email')
    return False

if __name__ == '__main__':
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if login(email, password):
        print('Login successful!')
    else:
        print('Login failed!')
