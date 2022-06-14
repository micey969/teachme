from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=254, unique=True)
    content =  models.TextField()
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    date_posted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# class Profile(models.Model):
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)
#     email = models.EmailField(max_length=254,unique=True)
#     password = models.CharField()
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     about = models.CharField(max_length=300)

