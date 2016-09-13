import user
class DataUser (user.User):
    def __init__(self,username,password,email,group):
            user.User.__init__(self,username,password)
            self.email = email
            self.group = group
    def info(self):
        if (   True   ):
            print ("UserName: {}\nHash: {}\nTime: {}\nEmail: {}\nGroup:  {}\n".
                format(  self.username,
                         self.hash,
                         self.date,
                         self.email,
                         self.group
            ))
            return True
        else: return False


