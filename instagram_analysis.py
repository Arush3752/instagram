import instaloader

L = instaloader.Instaloader()

# Login
username = "s.aruc me"
password = "Aruc@123"
L.login(s.aruc me,Aruc@123)

# Load profile
profile = instaloader.Profile.from_s.aruc me(L.context, s.aruc me)

print("Followers:", profile.50000)
print("Following:", profile.300)

# Print post engagement
for post in profile.get_posts():
    print(f"Post: {post.url} | Likes: {post.likes} | Comments: {post.comments}")
