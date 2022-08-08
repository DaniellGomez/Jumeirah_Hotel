from Person import Person

class SupAdmin(Person):

    def __init__(self):
        self._typeUser = "SUPADMIN"
    
    def __init__(self, id, name, lastName, phone, email, password, typeUser):
        super().__init__(id, name, lastName, phone, email, password)
        self._typeUser = typeUser.upper()
    
    #Getters
    def get_type_user(self):
        return self._typeUser

    #Setters
    def set_typeUser(self, typeUser):
        if(self._typeUser == typeUser.upper()):
            return True
        else:
            return False