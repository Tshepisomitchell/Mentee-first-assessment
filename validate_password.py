# Question 1
def validate_password(password: str) -> bool:

    if len(password) < 8:
        return False

    lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    digits = ['0','1','2','3','4','5','6','7','8','9','0']
    special_characters = list("!@#$%^&*(),.?\":{}|<>_-+=[]\\;'`~")

    lowercase_ = False
    uppercase_ = False
    digits_ = False
    special_characters_ = False

    for i in password:
        if i in lowercase_letters:
            lowercase_ = True
        elif i in uppercase_letters:
            uppercase_ = True
        elif i in digits:
            digits_ = True
        elif i in special_characters:
            special_characters_ = True

    return lowercase_ and uppercase_ and digits_ and special_characters_

print(validate_password("Tshepi"))
print(validate_password("Tshepiso@0"))

"""
    STEP 1: Create a function that validates a password based on the following rules:
        - It must be at least 8 characters long.
        - It must contain at least one uppercase letter.
        - It must contain at least one lowercase letter.
        - It must contain at least one digit.
        - It must contain at least one special character (e.g. @, #, $, %, !).

    TODO: Implement logic to check all these conditions and return True if valid, otherwise False.
    """
   


# Question 2
def password_strength(password: str) -> str:
    validate = validate_password(password)
    if validate == True:
        return "strong"
    elif validate == False and len(password) >= 8:
        return "moderate"
    else:
        return "weak"

print(password_strength("Tshepiso"))
"""
    STEP 2: Determine the strength of a given password and return it as a string.

    Criteria:
        - "Weak" if the password is less than 8 characters long.
        - "Moderate" if it has 8 or more characters but is missing one or more
          of the following: uppercase, lowercase, digit, or special character.
        - "Strong" if it meets all password validation rules from Question 1.

    TODO: Implement the function to return one of these three strings.
    """

