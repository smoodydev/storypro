from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="uprofile")
    header = models.CharField(max_length=200, blank=True)
    bio = models.TextField()
    is_premium = models.BooleanField(default=False)
    join_date = models.DateField(auto_now_add=True)
    last_online = models.DateField(auto_now=True)
    img_profile = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.user
