from django.shortcuts import render

def blog_index(request):
    context = {
        
    }
    return render(request, 'blog/blog_index.html', context)
