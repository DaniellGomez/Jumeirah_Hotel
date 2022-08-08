import Person

class User(Person):

    def __init__(self):
        self._bookings = int
        self._record = []
    
    def __init__(self, id, name, lastName, phone, email, password, record, bookings):
        super().__init__(id, name, lastName, phone, email, password)
        self._record = record
        self._bookings = bookings

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
    