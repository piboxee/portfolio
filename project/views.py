from django.shortcuts import render

def project_index(request):
    context = {
        
    }
    return render(request, 'project/project_index.html', context)
