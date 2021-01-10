from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class FileUpload(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=256,blank=False,null=False)
    file = models.FileField(upload_to='media',blank=True)
    time = models.TimeField(blank=True,null=True,auto_now_add=True)
    images = models.ImageField(default='images/Background.png')
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=256,null=True)
    profile_image = models.ImageField(upload_to="profile",null=True,blank=True,default='profile/Profile.jpg')

    def __str__(self):
        return self.name

class LikesUser(models.Model):
    user = models.ForeignKey(FileUpload,null=True,default=True,on_delete=models.CASCADE)
    name = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.name
    
class Comments(models.Model):
    user = models.ForeignKey(FileUpload,null=True,default=True,on_delete=models.CASCADE)
    name = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    comment = models.TextField(max_length=512)

    def __str__(self):
        return self.user.name