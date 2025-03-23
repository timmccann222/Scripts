#!/usr/bin/env python3
import requests
import json
import argparse

# list all resources
def list_all_posts(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # loop through each post
        for post in response.json():
            print(json.dumps(post,indent=4))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error connecting to the API.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# list specified resource
def get_post(url, id, id_type):
    try:
        if id_type == "post_id":
            query = f"{url}/{id}"
            response = requests.get(query)
            response.raise_for_status()
            print(json.dumps(response.json(),indent=4))
        elif id_type == "user_id":
            query = f"{url}?userId={id}"
            response = requests.get(query)
            response.raise_for_status()
            # loop through each post
            for post in response.json():
                print(json.dumps(post,indent=4))
        else:
            print("Error: no --id_type argument value provided!")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error connecting to the API.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# create a new post
def create_post(url, id, id_type, title, body):
    try:
        if id_type == "user_id" and title is not None and body is not None:
            # populate post data
            post_data = {
                'title':title,
                'body':body,
                'userId':id
                }
            response = requests.post(url, json=post_data)
            response.raise_for_status()
            print("Post created successfully!")
            print(json.dumps(response.json(),indent=4))
        else:
            print(f"Failed to create post. Please check body, title, id_type and id arguments are provided. Ensure id_type is set to 'user_id'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error connecting to the API.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# update an existing post
def update_post(url, id, id_type, title, body):
    try:
        if id_type == "post_id" and title is not None and body is not None:
            # populate updated data
            updated_data = {
                'title':title,
                'body':body,
                }
            query = f"{url}/{id}"
            response = requests.put(query, json=updated_data)
            response.raise_for_status()
            print("Post updated successfully!")
            print(json.dumps(response.json(),indent=4))
        else:
            print(f"Failed to update post. Please check body, title, id_type and id arguments are provided. Ensure id_type is set to 'post_id'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error connecting to the API.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# delete an existing post
def delete_post(url, id, id_type):
    try:
        if id_type == "post_id":
            query = f"{url}/{id}"
            response = requests.delete(query)
            response.raise_for_status()
            print("Post deleted successfully!")
            print(json.dumps(response.json(),indent=4))
        else:
            print(f"Failed to delete post. Please check id_type and id arguments are provided. Ensure id_type is set to 'post_id'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error connecting to the API.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# function defines arguments that can be passed by a user.
def parse_args():
    parser = argparse.ArgumentParser(description="Query JSONPlaceholder API.")
    parser.add_argument("--command", choices=['list_all_posts', 'get_post', 'create_post', 'update_post', 'delete_post'], type=str, required=False, help="Specify what function to run.")
    parser.add_argument("--id", type=str, required=False, help="Specify ID for user or post.")
    parser.add_argument("--id_type", choices=['post_id', 'user_id'], type=str, required=False, help="Specify ID type.")
    parser.add_argument("--body", type=str, required=False, help="Specify body message for create_post function.")
    parser.add_argument("--title", type=str, required=False, help="Specify title for create_post function.")
    return parser.parse_args()

# main program logic goes here
def main():
    # base API url
    base_url = 'https://jsonplaceholder.typicode.com/posts'

    # Perform search based on provided input.
    args = parse_args()

    # check provided input
    if args.command == "list_all_posts":
        list_all_posts(base_url)
    elif args.command == "get_post" and args.id.isdigit():
        get_post(base_url, args.id, args.id_type)
    elif args.command == "create_post" and args.id.isdigit():
        create_post(base_url, args.id, args.id_type, args.title, args.body)
    elif args.command == "update_post" and args.id.isdigit():
        update_post(base_url, args.id, args.id_type, args.title, args.body)
    elif args.command == "delete_post" and args.id.isdigit():
        delete_post(base_url, args.id, args.id_type)
    else:
        print("Error: Incorrect value provided!")
        parser = argparse.ArgumentParser()
        parser.print_help()

if __name__ == "__main__":
    main()
