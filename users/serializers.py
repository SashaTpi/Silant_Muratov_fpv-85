from rest_framework.serializers import Serializer, ModelSerializer, CharField
from rest_framework.authtoken.models import Token
from users.models import CustomUser


class UserSerializer(ModelSerializer):

    class Meta:
        class Meta:
         model = CustomUser
         fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']


class TokenSeriazliser(ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']
        

class IssueTokenRequestSerializer(Serializer):
    model = CustomUser
    username = CharField(required=True)
    password = CharField(required=True)


