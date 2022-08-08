import Person

class Admin(Person):

    def __init__(self):
        self._typeUser = "ADMIN"

    def __init__(self, id, name, lastName, phone, email, password, typeUser):
        super().__init__(id, name, lastName, phone, email, password)
        self._typeUser = typeUser
    
    #Getters
    def get_typeUser(self):
        return self._typeUser

    #Setters
    def set_typeUser(self, typeUser):
        if(self._typeUser == typeUser):
            return True
        else:
            return False
