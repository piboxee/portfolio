from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self)\
            .get_queryset()\
            .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique_for_date='published_date')
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default='Default')
    image = models.ImageField()
    description = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:350] + ' ...'

    def date_published(self):
        return self.published_date.strftime('%B %Y')

    def get_absolute_url(self):
        return f'/blog/{self.category.slug}/{self.slug}/'

    def get_edit_url(self):
        return f'/blog/{self.slug}/post-edit/'

    def get_delete_url(self):
        return f'/blog/{self.slug}/post-delete/'


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField()
    description = models.TextField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
