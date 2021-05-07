import pickle

class LoginInfo(object):
    def __init__(self, email, password):
        # self.website = website
        self.email = email
        self.password = password

if __name__ == "__main__":
    # execute only if run as a script
    email = input("Enter an email: ")
    print("You entered", email)
    password = input("Enter a password: ")
    print("You entered", password)

    facebookInfo = LoginInfo(email, password)

    with open('login_data.pkl', 'wb') as output:
        pickle.dump(facebookInfo, output, pickle.HIGHEST_PROTOCOL)

