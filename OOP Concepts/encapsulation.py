class Register:
    def __init__(self,username,password):
        self.un=username
        self.__ps=password

    def get_username(self):
        print("Your username is "+self.un)
    
    def get_password(self):
        print("Your password is "+self.__ps)

user1=Register("Vedh","12345")
print(user1.un)
user1.get_username()
user1.get_password()