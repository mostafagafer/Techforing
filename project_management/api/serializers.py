from rest_framework import serializers
from .models import User, Project, ProjectMember, Task, Comment

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']  # Include 'password'
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):
        # Create a new user with the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # Ensure password is hashed
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['id', 'user', 'role']

from rest_framework import serializers
from .models import Project, ProjectMember

class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['user', 'role']

class ProjectSerializer(serializers.ModelSerializer):
    members = ProjectMemberSerializer(many=True, required=False)  # Make 'members' optional

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'members']

    def create(self, validated_data):
        # Extract the nested 'members' data (if provided)
        members_data = validated_data.pop('members', [])
        
        # Get the current user (project creator)
        creator = self.context['request'].user
        
        # Create the project
        project = Project.objects.create(**validated_data)
        
        # Add the creator as an Admin by default
        ProjectMember.objects.create(project=project, user=creator, role='Admin')
        
        # Add other members (if provided)
        for member_data in members_data:
            ProjectMember.objects.create(project=project, **member_data)
        
        return project
    

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)  # Accept user ID
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())  # Accept project ID

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    task = serializers.StringRelatedField()  

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'task', 'created_at']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
