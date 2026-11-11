class User:
    def __init__(self,username,password):
        self.username = username 
        self.password = password 

    def check_password(self,password):
        if self.password == password:
            return True
        else:
            return False



u1 = User("alice", "secure1@23")
print(u1.check_password("secure1@23"))