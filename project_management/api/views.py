from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Project, Task, Comment, ProjectMember
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer, CommentSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny

# Custom Permission Class
class IsProjectAdmin(permissions.BasePermission):
    """Check if the user is an Admin for the project."""
    def has_object_permission(self, request, view, obj):
        # For Project-related views
        if isinstance(obj, Project):
            return ProjectMember.objects.filter(
                project=obj, user=request.user, role='Admin'
            ).exists()
        # For Task-related views
        elif isinstance(obj, Task):
            return ProjectMember.objects.filter(
                project=obj.project, user=request.user, role='Admin'
            ).exists()
        return False


# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all users.",
        responses={200: UserSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific user.",
        responses={200: UserSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new user.",
        request_body=UserSerializer,
        responses={201: UserSerializer()},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectAdmin]  # Add custom permission

    @swagger_auto_schema(
        operation_description="Retrieve a list of all projects.",
        responses={200: ProjectSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific project.",
        responses={200: ProjectSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new project. The authenticated user will be the owner and Admin.",
        request_body=ProjectSerializer,
        responses={201: ProjectSerializer()},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an existing project. Only Admins can perform this action.",
        request_body=ProjectSerializer,
        responses={200: ProjectSerializer()},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a project. Only Admins can perform this action.",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all tasks.",
        responses={200: TaskSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific task.",
        responses={200: TaskSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new task.",
        request_body=TaskSerializer,
        responses={201: TaskSerializer()},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an existing task.",
        request_body=TaskSerializer,
        responses={200: TaskSerializer()},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a task.",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all comments.",
        responses={200: CommentSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific comment.",
        responses={200: CommentSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new comment.",
        request_body=CommentSerializer,
        responses={201: CommentSerializer()},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an existing comment.",
        request_body=CommentSerializer,
        responses={200: CommentSerializer()},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a comment.",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# User Registration View
class RegisterUser(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated access

    @swagger_auto_schema(
        operation_description="Register a new user.",
        request_body=UserSerializer,
        responses={201: UserSerializer()},
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # This will call the `create` method in the serializer
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login View
class LoginUser(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated access to this view

    @swagger_auto_schema(
        operation_description="Authenticate a user and generate a token.",
        request_body=LoginSerializer,
        responses={
            200: "Token generated successfully",
            400: "Invalid credentials or missing fields",
        },
    )
    def post(self, request):
        # Validate input data using the serializer
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)  # Debug: Print serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Extract validated data
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        print(f"Attempting to authenticate user: {username}")  # Debug: Print username

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            print(f"User authenticated: {user.username}")  # Debug: Print authenticated user
            # Generate or retrieve the token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            print("Authentication failed: Invalid credentials")  # Debug: Print authentication failure
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )