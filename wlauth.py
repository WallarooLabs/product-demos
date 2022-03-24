import wallaroo
import e2elib
import os


# return the authorized client
def login(filename):
    # this should match the creds file
#    x=e2elib.Keycloak("keycloak", "8080", "admin","admin")
#    x.get_token()
#    x.create_user("nina", "foobar", 'nina@zumel.com') # this is me: user , password , company 

    os.environ["WALLAROO_SDK_CREDENTIALS"] = 'creds.json'

    wl = wallaroo.Client(auth_type="user_password")
    return (wl)