import datetime
import hashlib
import sys
sys.path.append("./project/database")
import db
class User(object):

    def __init__(self,username,password):
            self.date = datetime.datetime.now()
            self.username = username
            self.hash = hashlib.sha512(str(password).encode("UTF8")).hexdigest() #add soul
            self.id = db.new_id_user()
            del password
            self.check = None
            self.auth = None
    def info(self):
        if (   True   ):
            print ("UserId: {}\nUserName: {}\nHash: {}\nDate: {}\n".
                format(self.id,self.username,self.hash,self.date,  ))
            return True
        else: return False
    def rename(self,newusername):
        self.username=newusername
    def repas(self,newpassword):
        pass
