from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Post, Category
from .forms import PostModelForm


class BlogListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'all_posts'
    paginate_by = 5
    template_name = 'blog/blog_index.html'


def blog_category_list_view(request, pk):
    all_posts = get_object_or_404(Category.objects.all(), pk=pk)

    context = {
        'all_posts': all_posts
    }

    return render(request, 'blog/category_index.html', context)


def post_details(request, slug, category):
    post = get_object_or_404(Post, slug=slug, category__slug=category, status='published')

    context = {
        'post': post
    }

    return render(request, 'blog/post_details.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        return redirect('/blog/')

    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
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
