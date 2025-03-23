# JSONPlaceholder

This python script allows the user to interact with the **JSONPlaceholder** API. The script provides the following functionality:

1. List all posts
2. Get a specific post based on ID
3. Create a new post
4. Updating an existing post
5. Delete a post

## Script Usage

```bash
usage: api_script.py [-h] [--command {list_all_posts,get_post,create_post,update_post,delete_post}] [--id ID] [--id_type {post_id,user_id}]
                     [--body BODY] [--title TITLE]

Query JSONPlaceholder API.

options:
  -h, --help            show this help message and exit
  --command {list_all_posts,get_post,create_post,update_post,delete_post}
                        Specify what function to run.
  --id ID               Specify ID for user or post.
  --id_type {post_id,user_id}
                        Specify ID type.
  --body BODY           Specify body message for create_post function.
  --title TITLE         Specify title for create_post function.
```


## What is an API?

An **API** stands for **Application Programming Interface**, which is a set of rules and protocols that allow different software applications to communicate with each other.

## Common API Terms

* **Request**: What you send to the API (e.g., GET /weather?city=London)
* **Response**: What you get back from the API (e.g., { "temp": "15°C" })
* **Endpoint**: A specific URL where you send your request (e.g., /api/users)
* **HTTP Methods**:
	- `GET` (read data)
	- `POST` (create data)
	- `PUT/PATCH` (update data)
	- `DELETE` (remove data)
* **JSON:** Common format for sending/receiving data with APIs

