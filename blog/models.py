from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db.models import Q


# category
class Category(models.Model):
    name = models.CharField(max_length=250, default='General')
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('blog:list_of_post_by_category', args=[self.slug])

    def __str__(self):
        return self.name


# Test
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(Q(status='published') | Q(status='Published'))\
            .filter(published__lte=timezone.now())


# Test
def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


# Post
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.FileField(null=True, blank=True, upload_to='media/')
    # image_alt_text = models.CharField(max_length=140)
    """image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field",
                              )"""

    content = models.TextField()
    seo_title = models.CharField(max_length=250)
    seo_description = models.CharField(max_length=160)
    author = models.ForeignKey(User, related_name='blog_posts')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

    # Test
    objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])


class Comment(models.Model):
    COMMENT_STATUS = (
        ('pending', 'pending'),
        ('approved', 'Approved')
    )
    post = models.ForeignKey(Post, related_name='comments')
    user = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

        def __str__(self):
            return self.user
