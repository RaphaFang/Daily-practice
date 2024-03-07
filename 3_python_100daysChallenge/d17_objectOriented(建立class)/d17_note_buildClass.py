class User:
    def __init__(self, user_id, username):
        ## when you set 2 paremetors inside the (), 
        ## you have to add 2 items, each time create a new object.
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        ## a default setting "0", will reduse keep adding "0" each time to create object
    def follow(self, user):
        user.followers +=1
        self.following +=1

user_1 = User("001", "Rapha")
user_2 = User("002", "James")

print(user_1.id)
user_1.follow(user_2)

print(user_1.following)