from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from django.contrib.flatpages import views
from .views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('project/', include('project.urls')),
    path('contact/', contact, name='contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
