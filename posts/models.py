from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category


def custom_upload_miniature(instance, filename):
    try:
        old_instance = Post.objects.get(pk=instance.pk)
        old_instance.miniature.delete()
        return 'posts/images/' + filename
    except:
        return 'posts/images/' + filename


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to=custom_upload_miniature)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name = 'posts'
        verbose_name_plural = '03 Posts'

    def __str__(self):
        return self.title

