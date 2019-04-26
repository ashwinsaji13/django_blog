from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE


class User(AbstractUser):
    phone_no = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=128, default='fILL ME')
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, related_name='user_posts', null=True, on_delete=CASCADE)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, related_name='user_likes', on_delete=CASCADE)
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=CASCADE)

