from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'avatar', 'comment', 'tg_chat_id')
