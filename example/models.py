from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class Object(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    activated = models.BooleanField(default=False)
    slug = models.SlugField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default = None)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'description'])
        ]
    def __str__(self):
        return self.name
