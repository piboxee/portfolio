from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:350] + ' ...'

    def date_published(self):
        return self.published.strftime('%B %Y')

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'

    def get_edit_url(self):
        return f'/blog/{self.slug}/post-edit/'

    def get_delete_url(self):
        return f'/blog/{self.slug}/post-delete/'


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    cellphone_num = models.IntegerField()

    def __str__(self):
        return self.user.username