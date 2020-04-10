from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Post, Author
from .forms import PostModelForm


class BlogListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'all_posts'
    paginate_by = 5
    template_name = 'blog/blog_index.html'


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/post_details.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        return redirect('/blog/')

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
    if not request.user.is_authenticated:
        return redirect('/blog/')

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
    if not request.user.is_authenticated:
        return redirect('/blog/')

    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return redirect('/blog/')
