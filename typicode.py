import requests

from pprint import pprint

import sys

def get_all_titles():
	res = requests.get("https://jsonplaceholder.typicode.com/posts")
	posts = res.json()
	list_of_titles = []

	for post in posts:
		post_title = post.get('title')
		list_of_titles.append(post_title)

	pprint(list_of_titles)

def user_id5_email():
	res = requests.get("https://jsonplaceholder.typicode.com/users?id=5")
	user_id5 = res.json()
	email = user_id5[0].get('email')

	print(f'The email of the user with the id # 5 is: {email}')

def created_postid():
	res = requests.post("https://jsonplaceholder.typicode.com/posts", data={"userId": 11, "id": 101, "title": "Why I should be hired for the programmer role at the NML", "body": "I should be hired because I believe I have the necessary skills needed to immediate fulfil all the responsibilities and needs required in this position in an effective manner while delivering great results.  Also I am someone who loves to build and expand my skills to contribute more and work towards the next step of my career in the agency. I will also be a great fit with the team and also the culture of the of the agency."})

	post_id = res.json().get('id')

	print(f'The id of the created post is {post_id}')

def get_titles_of_userId5():
	res = requests.get("https://jsonplaceholder.typicode.com/posts?userId=5")

	posts = res.json()
	list_of_titles = []

	for post in posts:
		post_title = post.get('title')
		list_of_titles.append(post_title)

	pprint(list_of_titles)

def update_post14_title():
	res = requests.put("https://jsonplaceholder.typicode.com/posts/14", data={"title": "I passed the test!"})

	print(res.json())

def determine_number_of_TODOs1():
	res = requests.get("https://jsonplaceholder.typicode.com/todos?userId=5")
	number_of_TODOs = len(res.json())

	print(f'The number of TODOs is {number_of_TODOs}')

# OR

def determine_number_of_TODOs2():
	res = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": 5})
	number_of_TODOs = len(res.json())

	print(f'The number of TODOs is {number_of_TODOs}')

def call_specific_operation(parameter):
	if (parameter == "list_all_titles"):
		get_all_titles()
	elif (parameter == 'uid_5_email'):
		user_id5_email()
	elif (parameter == 'id_of_createdpost'):
		created_postid()
	elif (parameter == 'titles_of_uid_5_posts'):
		get_titles_of_userId5()
	elif (parameter == 'update_post14_title'):
		update_post14_title()
	elif (parameter == 'number_of_uid5_todos1'):
		determine_number_of_TODOs1()
	elif (parameter == 'number_of_uid5_todos2'):
		determine_number_of_TODOs2()
	else:
		print("You gave a wrong parameter")

def main():
	if (len(sys.argv) < 2):
		print("To execute all the required operations, type yes, or give a specific parameter")

		parameter = input().lower()

		if (parameter == "yes"):
			get_all_titles()
			user_id5_email()
			created_postid()
			get_titles_of_userId5()
			update_post14_title()
			determine_number_of_TODOs1()
			determine_number_of_TODOs2()
		else:
			call_specific_operation(parameter)
	else:
		parameter = str(sys.argv[1].lower())
		call_specific_operation(parameter)

if __name__ == "__main__":
	main()