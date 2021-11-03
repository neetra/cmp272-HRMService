from datetime import datetime


class BasicUserProfile:
    def __init__(self):
        self.user_id= 0
        self.email = ""
        self.first_name= ""
        self.last_name = ""        
        self.dob= datetime.now()
        self.doj = datetime.now()
        self.phone_number = ""
        self.password= "",
        self.photourl = ""