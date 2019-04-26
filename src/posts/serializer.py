# rest-framework
from rest_framework import serializers

# custom imports
from .models import Post, User, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']


class PostSerializer(serializers.ModelSerializer):

    user_details = UserSerializer(source='user', read_only=True)
    # post_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        read_only_fields = ['user_details']
        fields = [f.name for f in model._meta.fields] + read_only_fields

    # def get_post_count(self, obj):
    #     return obj.user.count()

    @staticmethod
    def setup_eager_loading(queryset):
        """
        Performs necessary eager loading of data.
        """
        queryset = queryset.prefetch_related('user_details')

        return queryset


class LikeSerializer(serializers.ModelSerializer):
    # count = serializers.IntegerField()

    class Meta:
        model = Like

        fields = [f.name for f in model._meta.fields]
