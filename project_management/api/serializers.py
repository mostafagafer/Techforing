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


# ProjectMember Serializer
class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ['id', 'user', 'role']


# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    members = ProjectMemberSerializer(many=True, required=False)  # Make 'members' optional
    owner = serializers.StringRelatedField(read_only=True)  # Add owner field

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'members']

    def validate_members(self, value):
        """Validate members data."""
        for member_data in value:
            if not User.objects.filter(id=member_data['user'].id).exists():
                raise serializers.ValidationError(f"User {member_data['user'].id} does not exist.")
        return value

    def create(self, validated_data):
        # Remove 'members' data from validated_data
        members_data = validated_data.pop('members', [])
        
        # Get the current user (project creator) from the context
        creator = self.context['request'].user
        
        # Create the project without the 'owner' field in validated_data
        project = Project.objects.create(owner=creator, **validated_data)
        
        # Add the creator as an Admin by default
        ProjectMember.objects.create(project=project, user=creator, role='Admin')
        
        # Add other members (if provided)
        for member_data in members_data:
            ProjectMember.objects.create(project=project, **member_data)
        
        return project

    def update(self, instance, validated_data):
        # Handle nested 'members' data
        members_data = validated_data.pop('members', [])

        # Update the project instance
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Delete existing members (optional: you can also update them instead of deleting)
        ProjectMember.objects.filter(project=instance).delete()

        # Add new members
        for member_data in members_data:
            ProjectMember.objects.create(project=instance, **member_data)

        return instance
    

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']

    def validate(self, data):
        """Ensure assigned_to is a member of the project."""
        assigned_to = data.get('assigned_to')
        project = data.get('project')
        if assigned_to and not ProjectMember.objects.filter(project=project, user=assigned_to).exists():
            raise serializers.ValidationError("The assigned user must be a member of the project.")
        return data


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Ensure user is read-only
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'task', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True},  # Ensure user is read-only
        }

    def create(self, validated_data):
        # Set the user to the current authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)