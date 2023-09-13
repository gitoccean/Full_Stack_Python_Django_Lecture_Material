
# make a function to check strength of a password
def strength_password(password):
    if len(password) <= 8:  # must be at least 8 characters long
        return False
    elif not any(c.isupper() for c in password):  # must contain at least one uppercase letter
        return False
    elif not any(c.islower() for c in password):  # must contain at least one lowercase letter
        return False
    elif not any(c.isdigit() for c in password):  # must contain at least one digit
        return False
    elif not any(c in '!@#$%^&*' for c in password):  # must contain at least one special character
        return False
    else:
        return True

# make a function to drive new password accordingly conditions
def new_password(password):
    if strength_password(password):
        first_three = password[:3] # extract first 3 character by slice
        last_three = password[-3:] # extract last 3 character by slice
        length = len(password)     #  extract length of actual password
        new_password = f"{first_three}{last_three}{length}"
        return new_password
    else:
        return None


# main portion to run above function
user = input("Enter a password: ")
if new_password(user):
    print("Password Strength: Strong")
    new_password = new_password(user)
    print("New password:", new_password)
else:
    print("Password Strength: Weak")
