class Person:

    def __init__(self):
        self._id = ""
        self._name = ""
        self._lastName = ""
        self._phone = ""
        self._email = ""
        self._password = ""

    def __init__(self, id, name, lastName, phone, email, password):
        self._id = id
        self._name = name
        self._lastName = lastName
        self._phone = phone
        self._email = email
        self._password = password

    #Getters
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name

    def  get_lastName(self):
        return self._lastName

    def get_phone(self):
        return self._phone
    
    def get_email(self):
        return self._email

    def get_password(self):
        return self._password
    
    #Setters

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        if( type(name).isalnum()):
            self._name = name
        else:
            return "Format invalid"
    
    def set_lastName(self, lastName):
        if( type(lastName).isalnum()):
            self._lastName = lastName
        else:
            return "Format invalid"
        
    def set_phone(self, phone):
        if(type(phone).isalnum()):
            self._phone = phone
        else:
            return "Format invalid"
        
    def set_email(self, email):
        if( type(email).isalnum()):
            self._email = email
        else:
            return "Format invalid"
        
    def set_password(self, password):
        if( type(password).isalnum()):
            self._password = password
        else:
            return "Format invalid"

        
    
        

    

    
