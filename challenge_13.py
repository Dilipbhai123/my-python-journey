user = {'id': 3, 'name': 'Dilip Kumar', 'email': 'dilip@example.com', 'password': 'secure_password_hash', 'city': 'Ahmedabad', 'bio': 'Python Developer & Tech Enthusiast', 'is_student': 1}

user.update({"id": 1})
# print(user)

all_keys = user.keys()
# print(all_keys)

all_values = user.values()
# print(all_values)

all_items = user.items()
# print(all_items)


#dictionary keys convart in the list
all_list = list(all_keys)
print(all_list)