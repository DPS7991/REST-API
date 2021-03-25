import requests

from pprint import pprint

def get_all_titles():
	res = requests.get("https://jsonplaceholder.typicode.com/posts")
	posts = res.json()
	list_of_titles = []

	for post in posts:
		post_title = post.get('title')
		list_of_titles.append(post_title)

	pprint(list_of_titles)

# get_all_titles()

def user_id5_email():
	res = requests.get("https://jsonplaceholder.typicode.com/users?id=5")
	user_id5 = res.json()
	email = user_id5[0].get('email')

	print(f'The email of the user with the id # 5 is: {email}')

# user_id5_email()

def created_postid():
	res = requests.post("https://jsonplaceholder.typicode.com/posts", data={"userId": 11, "id": 101, "title": "Why I should be hired for the programmer role at the NML", "body": "I should be hired because I believe I have the necessary skills needed to immediate fulfil all the responsibilities and needs required in this position in an effective manner while delivering great results.  Also I am someone who loves to build and expand my skills to contribute more and work towards the next step of my career in the agency. I will also be a great fit with the team and also the culture of the of the agency."})

	post_id = res.json().get('id')

	print(f'The id of the created post is {post_id}')

# created_postid()

def get_titles_of_userId5():
	res = requests.get("https://jsonplaceholder.typicode.com/posts?userId=5")

	posts = res.json()
	list_of_titles = []

	for post in posts:
		post_title = post.get('title')
		list_of_titles.append(post_title)

	pprint(list_of_titles)

# get_titles_of_userId5()

def update_post14_title():
	res = requests.put("https://jsonplaceholder.typicode.com/posts/14", data={"title": "I passed the test!"})

	print(res.json())

# update_post14_title()

def determine_number_of_TODOs1():
	res = requests.get("https://jsonplaceholder.typicode.com/todos?userId=5")
	number_of_TODOs = len(res.json())

	print(f'The number of TODOs is {number_of_TODOs}')

# determine_number_of_TODOs1()

# OR

def determine_number_of_TODOs2():
	res = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": 5})
	number_of_TODOs = len(res.json())

	print(f'The number of TODOs is {number_of_TODOs}')

# determine_number_of_TODOs2()
