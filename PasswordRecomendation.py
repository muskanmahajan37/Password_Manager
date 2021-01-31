import random,string


def PasswordGenerator():
    PasswordLength=10

    PasswordCharacters = string.ascii_letters+string.digits+string.punctuation

    Password = []

    for elements in range(PasswordLength):
        Password.append(random.choice(PasswordCharacters))

    return ''.join(Password)