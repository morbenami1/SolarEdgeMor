from django.db import models

class Post:
    id: int
    title: str
    body: str

class Comment:
    id: int
    postId: int
    name: str
    email: str
    body: str
