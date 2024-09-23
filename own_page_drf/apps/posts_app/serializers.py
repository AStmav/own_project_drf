from rest_framework.serializers import ModelSerializer, SerializerMethodField
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Post, PostImage, Comment

class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField() #количество ответов на комментарий
    author = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('content', 'parent', 'author', 'reply_count', 'post')

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_author(self, obj):
        return obj.author.username

class PostSerializer(ModelSerializer):
    images = PostImageSerializer(source='postimage_set', many=True)
    comments = CommentSerializer(source='postcomment', many=True)

    class Meta:
        model = Post
        fields = '__all__'