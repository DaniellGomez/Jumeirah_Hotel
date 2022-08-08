import Person

class User(Person):

    def __init__(self):
        self._bookings = int
        self._record = []
        self._typeUser = "USER"
    
    def __init__(self, id, name, lastName, phone, email, password, record, bookings, typeUser):
        super().__init__(id, name, lastName, phone, email, password)
        self._record = record
        self._bookings = bookings
        self._typeUser = typeUser

    #Getters

    def get_bookings(self):
        return self._bookings
    
    def get_record(self):
        return self._record

    #Setters
    def set_bookings(self, bookings):
        if(type(bookings).isdecimal()):
            self._bookings = bookings
        else:
            return "Invalid format"
        
    def set_record(self, record):
        if(len(record) == 0):
            return "Record is empty"
        else:
            self._record = record
    
    def set_typeUser(self, typeUser):
        if(self._typeUser == typeUser):
            return True
        else:
            return False
