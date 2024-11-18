import requests

API_BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_posts():
    response = requests.get(f"{API_BASE_URL}/posts")
    return response.json()

def fetch_post(post_id):
    response = requests.get(f"{API_BASE_URL}/posts/{post_id}")
    return response.json()

def fetch_comments(post_id):
    response = requests.get(f"{API_BASE_URL}/posts/{post_id}/comments")
    return response.json()