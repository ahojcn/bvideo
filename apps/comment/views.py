from rest_framework import viewsets

from apps.comment.models import (
    Comment
)
from apps.comment.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    评论视图
    """

    queryset = Comment.objects.all().order_by('-add_time')
    serializer_class = CommentSerializer

