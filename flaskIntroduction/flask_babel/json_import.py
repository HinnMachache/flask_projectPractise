#!/usr/bin/env python3
import json

with open('posts.json', 'r') as file:
	posts_dict = json.load(file)

for post in posts_dict:
	for key in post.keys():
		print(key)	
# for post in posts_dict:
#     post = Post(title=post['title'], content=post['content'], user_id=post['user_id'])



