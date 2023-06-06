usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = list(zip(usernames, passwords))
print(type(users))
for i in users:
    print(i)

users = dict(zip(usernames, passwords))
print(type(users))

for key, value in users.items():
    print(key + " : " + value)

login_date = ["1/1/2023", "1/2/2023", "1/3/2023"]
users = zip(usernames, passwords, login_date)
for i in users:
    print(i)
