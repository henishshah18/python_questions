from collections import Counter, defaultdict

posts = [
    {"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["weather", "life"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["python", "learning"]}
]

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120}
}

tag_counter = Counter()
likes_per_user = defaultdict(int)

for post in posts:
    tag_counter.update(post["tags"])
    likes_per_user[post["user"]] += post["likes"]

top_posts = sorted(posts, key=lambda x: x["likes"], reverse=True)

user_summary = {}
for user in users:
    post_count = sum(1 for post in posts if post["user"] == user)
    total_likes = likes_per_user[user]
    user_summary[user] = {
        "posts": post_count,
        "likes": total_likes,
        "followers": users[user]["followers"],
        "following": users[user]["following"]
    }

print("Most Popular Tags:", tag_counter.most_common())
print("User Engagement (Total Likes):", dict(likes_per_user))
print("Top Posts by Likes:", [(p["id"], p["likes"]) for p in top_posts])
print("User Activity Summary:", user_summary)
