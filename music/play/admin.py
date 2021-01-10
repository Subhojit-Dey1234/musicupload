from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import FileUpload,UserDetails,LikesUser
# Register your models here.
# admin.site.register(FileUpload)
admin.site.register(UserDetails)
# admin.site.register(Likes)
User = get_user_model()
admin.site.unregister(User)
class MusicInline(admin.StackedInline):
    model = FileUpload

class UserDetails(admin.ModelAdmin):
    inlines = [MusicInline,]
admin.site.register(User,UserDetails)

class LikeInline(admin.StackedInline):
        model = LikesUser

class FileDetails(admin.ModelAdmin):
        inlines = [LikeInline]

admin.site.register(FileUpload,FileDetails)