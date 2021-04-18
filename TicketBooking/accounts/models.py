from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('Other','Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    profile_img = models.FileField(upload_to="images", default="images/avatar.jpg", null=True, blank=True)
    phone = models.CharField(max_length=10, default=None, null=True, blank=True)
    location = models.CharField(max_length=200, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


  