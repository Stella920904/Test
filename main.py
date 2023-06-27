from TC_Login import TC_login_Class
from CommonLogin import CommonloginClass
from TC_NF_Plan_FreeTrialStart import TC_NF_Plan_FreeTrialStart_Class
from TC_Signup import TC_Signup_Class

def LoginTest():
    login = TC_login_Class
    login.LoginDef()

def FreetrialTest():
    Freetrial = TC_NF_Plan_FreeTrialStart_Class
    Freetrial.FreetrialStartDef()
def SignupTest():
    Signuptest = TC_Signup_Class
    Signuptest.SignupDef()


if __name__ == "__main__":
    # SignupTest()
    # LoginTest()
    FreetrialTest()


