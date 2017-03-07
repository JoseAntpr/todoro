from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User()
        user.first_name = validated_data.get("first_name")
        user.last_name = validated_data.get("last_name")
        user.username = validated_data.get("username")
        user.email = validated_data.get("email")
        user.set_password(validated_data.get('password'))
        user.save()

        return user




    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()

        return instance

    def validate(self,attrs):
        #actualizo el usuario sin cambiaer el username -> ok
        # actualizo el usuario cambiendo el username -> ok si nuevo userame no esá usado
        if self.instance is None and User.objects.filter(username = attrs.get("username")).exists():
            raise ValidationError("Username already exists")

        if self.instance is not None and self.instance.username != attrs.get("username") and User.objects.filter(username = attrs.get("username")).exists():
            raise ValidationError("Username already exists")
        return attrs