import jsonpickle;
class UserDetails(dict):
    def __init__(self, r):
        self.user_id = r[0]
        self.first_name = r[1]
        self.last_name = r[2]
        self.email = r[3]
        self.dob = r[4]
        self.doj = r[5]
        self.contact_no =r[6]
        self.photo_url = r[7]
        self.designation = r[8]
        self.department = r[9]
        self.gender = r[10]
        self.marital_status = r[11]
        dict.__init__(self, user_id = self.user_id, first_name = self.first_name, last_name= self.last_name,email = self.email,dob = self.dob, doj= self.doj, designation = self.designation, department =self.department, marital_status = self.marital_status)
    
