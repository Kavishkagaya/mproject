from .models import Subjects,Papers
from .serializers import Subjectserializer,Paperserializer, Userserializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


#fastest method (modelviewset)
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = Subjectserializer
    permission_classes = [IsAuthenticated]
    authentication_classes = {TokenAuthentication,}

class PaperViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    serializer_class = Paperserializer
    permission_classes = [IsAuthenticated]
    authentication_classes = {TokenAuthentication,}

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = Userserializer
    permission_classes = [IsAuthenticated]
    authentication_classes = {TokenAuthentication,}
