import pickle

class LoginInfo(object):
    def __init__(self, email, password):
        # self.website = website
        self.email = email
        self.password = password

if __name__ == "__main__":
    # execute only if run as a script
    facebookInfo = None
    twitterInfo = None

    while(True):
        website = input("What websites do you want to log into?\nEnter a number between 1-2:\n1. Facebook\n2. Twitter\n0. Finish\n")
        if(website == "1"):
            email = input("Enter your Facebook email: ")
            print("You entered", email)
            password = input("Enter your Facebook password: ")
            print("You entered", password)
            facebookInfo = LoginInfo(email, password)
        if(website == "2"):
            email = input("Enter your Twitter email: ")
            print("You entered", email)
            password = input("Enter your Twitter password: ")
            print("You entered", password)
            twitterInfo = LoginInfo(email, password)
        if(website == "0"):
            break

    with open('login_data.pkl', 'wb') as output:
        pickle.dump(facebookInfo, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(twitterInfo, output, pickle.HIGHEST_PROTOCOL)

