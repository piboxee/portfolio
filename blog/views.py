from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .models import Post, Author
from .forms import PostModelForm


def blog_index(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts
    }

    return render(request, 'blog/blog_index.html', context)


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/post_details.html', context)


def post_create(request):
    author, created = Author.objects.get_or_create(
        user=request.user,
        email=request.user.email,
        cellphone_num=53782372932
    )
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        return redirect('/blog/')

    context = {
        'form': form
    }

    return render(request, 'blog/post_create.html', context)


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('/blog/' + slug)

    context = {
        'form': form
    }

    return render(request, 'blog/post_edit.html', context)


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return redirect('/blog/')
