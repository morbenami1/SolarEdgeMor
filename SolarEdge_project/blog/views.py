from django.shortcuts import render
from django.core.paginator import Paginator
from .utils import fetch_posts, fetch_post, fetch_comments

def post_list(request):
    posts = fetch_posts()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, post_id):
    post = fetch_post(post_id)
    comments = fetch_comments(post_id)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})