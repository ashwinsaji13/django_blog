from django.contrib import admin
from .models import Post, User, Like


# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'date_joined', 'is_staff']

    class Meta:
        model = User

    def save_model(self, request, user, form, change):
        if user.password and len(user.password) < 30:
            user.set_password(user.password)
        user.save()


admin.site.register(User, UserModelAdmin)


class LikeModelAdmin(admin.ModelAdmin):
    """
    like model
    """
    list_display = ['post']

    class Meta:
        model = Like


admin.site.register(Like, LikeModelAdmin)
