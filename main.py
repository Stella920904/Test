from TC_Login import TC_login_Class
from TC_NF_Plan_FreeTrialStart import TC_NF_Plan_FreeTrialStart_Class
from TC_Signup import TC_Signup_Class

def login_test():
    login = TC_login_Class
    login.login_def()

def freetrial_test():
    Freetrial = TC_NF_Plan_FreeTrialStart_Class
    Freetrial.freetrialstart_def()
def signup_test():
    Signuptest = TC_Signup_Class
    Signuptest.signup_def()


if __name__ == "__main__":
    # signup_test()
    login_test()
    # freetrial_test()


