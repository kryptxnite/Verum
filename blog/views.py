from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def posts(request, category_slug=None):
    posts = Post.published.all()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts,
                   'category': category})


def post_detail(request, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post)

    return render(request,
                  'blog/post/detail.html',
                  {"post": post})