from rest_framework import serializers
from .models import Papers,Subjects
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model =  Subjects
        fields = ['id','title','imgurl']

class Paperserializer(serializers.ModelSerializer):
    class Meta:
        model = Papers
        fields = ['id','title','imgurl','fileurl','subject']

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
