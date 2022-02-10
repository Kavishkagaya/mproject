from django.contrib import admin
from django.urls import path , include
from api.views import SubjectViewSet ,PaperViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('subjects',SubjectViewSet,basename='subjects')
router.register('papers',PaperViewSet,basename='papers')
router.register('users',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
