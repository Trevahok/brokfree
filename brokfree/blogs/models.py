from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_sentinel_user():
    return User.objects.get_or_create(username='deleted_user')[0]
class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user))
    desc = models.CharField(max_length = 40, blank = True)
    content = models.TextField(max_length = 150)
    likes = models.PositiveSmallIntegerField(default = 0)
    pub_date = models.DateTimeField(auto_now_add = True)
    bhk = models.PositiveSmallIntegerField( choices = zip(range(1,5), range(1,5)), default =1)
    def __str__(self):
        return self.desc
