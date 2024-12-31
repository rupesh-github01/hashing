import secrets
#Generating hash
def generate_hash(str):
    newNum = 0 
    length = len(str) 
    for i in range(0, length):
        newNum = newNum + ord(str[i]) * (31 ** i)
    hexNum = hex(newNum)  # Convert the number to hexadecimal
    return hexNum

userDetails = {} # A dictionary to store login credentials
exit_toggle = False 
while not exit_toggle:
    print("Please select the action:")
    print("1. Login")
    print("2. Sign Up")
    print("3. exit_toggle")
    ch = int(input("Enter your choice: "))

    if ch == 2:  # Sign Up action
        newUser = input("Enter new username: ")
        newPass = input("Enter new password: ")
        newSalt = secrets.token_bytes(4)  # Generate a 4-byte random salt
        newSalt = newSalt.hex() #converting salt to a string
        userHash = generate_hash(newSalt + newUser)  # Concatenate salt and username
        passHash = generate_hash(newSalt + newPass)  # Concatenate salt and password
        userDetails.update({newUser: [userHash, passHash, newSalt]})
        print("Registration complete")
        continue

    elif ch == 1:  # Login action
        print("Welcome back")
        login = False 
        while not login:
            user = input("Enter username: ")
            password = input("Enter password: ")
            
            if user in userDetails:  # Check if the user exists
                salt = userDetails[user][2]
                userHash = generate_hash(salt + user)
                passHash = generate_hash(salt + password)

                if userHash == userDetails[user][0] and passHash == userDetails[user][1]:
                    print("Login successful")
                    login = True
                else:
                    print("Entered credentials are wrong, retry")
            else:
                print("Username not found, retry")
        continue

    elif ch == 3:  
        print("Exit complete")
        exit_toggle = True 
        continue

    else:
        print("Invalid choice, please try again.")
