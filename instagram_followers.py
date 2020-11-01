import instaloader

MY_ACCOUNT = ''
TARGET_USERNAME = 'emmanuelmacron'

L = instaloader.Instaloader()
L.interactive_login(MY_ACCOUNT)

profile = instaloader.Profile.from_username(L.context, TARGET_USERNAME)

print("{} is followed by:".format(profile.username))
for follower in profile.get_followers():
    print(follower.username)
