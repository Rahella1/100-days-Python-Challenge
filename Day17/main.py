class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Rahel")
user_2 = User("002", "Jery")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# print(user_1.id)
# print(user_1.username)
# print(user_2.id)
#print(user_1.followers)

# attributes are things which  the object will have variables are conneted to the object
# user_1 =User()
# user_1.id = "001"
# user_1.user_name = "Rahel"
# user_1.followers = 0

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Jery"
# user_2.followers = 1


