from User import User

user1 = User('001', 'Daniel', 'Lopera', '313453443', 'daniel@.com', '123456', 3, [], 'user')

print("")
print("****USERS******")
print(user1.get_id())
print(user1.get_type_user())

print(user1.set_typeUser('Admin'))


from Admin import Admin

print("")
print("****ADMINS******")
admin1 = Admin('001', 'Camilo', 'Urrego', '31345234', 'camilo@gmail.com', '34562345', 'Admin')


print(admin1.get_name())
print(admin1.get_typeUser())
print(admin1.set_typeUser('admin'))


