from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, SearchForm
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count

from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline
)



# Post section
# ========================
def posts(request, category_slug=None, tag_slug=None):

    posts = Post.published.all()
    category = None
    tag = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 12)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/post/list.html',
        {
            'posts': posts,
            'category': category,
            'tag': tag,
        }
    )



# Post detail section
# ========================
def post_detail(request, post):

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post)
        
    comments = post.comments.filter(active=True)
    form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                    'comments': comments,
                    'form': form,
                    'similar_posts': similar_posts})



# Comment section
# ========================
@require_POST
def post_comment(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED)
        
    comment = None
    form = CommentForm(data=request.POST)

    if form.is_valid:
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(
        request,
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment
        }
    )



def post_search(request):

    form = SearchForm(request.GET or None)
    query = None
    results = []

    if form.is_valid():

        query = form.cleaned_data['query']    

        search_vector = (
            SearchVector('title', weight='A') +
            SearchVector('body', weight='B')
        )

        search_query = SearchQuery(query)

        results = Post.published.annotate(
            rank = SearchRank(search_vector, search_query),
            headline = SearchHeadline(
                'body',
                search_query,
                start_sel = '<mark>',
                stop_sel = '</mark>'
            )
        ).filter(rank__gte=0.1).order_by('-rank')

    return render(
        request,
        'blog/post/search.html',
        {
            'form': form,
            'query': query,
            'results': results
        }
    )



def about(request):
    return render(request, 'blog/post/about.html')

def contact(request):
    return render(request, 'blog/post/contact.html')