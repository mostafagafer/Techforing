from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet, RegisterUser, RegisterUser, LoginUser


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('', include(router.urls)),
]
