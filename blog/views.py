from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comments
from .models import Post




 #post_category
def post_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-published_date")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/post_category.html", context)


#post_list
def post_list(request):
    posts = Post.objects.all().order_by("-published_date")
    context = {
        "posts": posts,
    }
    return render(request, "blog/post_list.html", context)


#post_detail
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
        # "comments": comments,
    }

    return render(request, "blog/post_detail.html", context)
