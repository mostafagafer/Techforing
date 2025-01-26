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

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Show owner's username
    members = ProjectMemberSerializer(many=True, required=False)  # Nested serializer for members

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at', 'members']

    def update(self, instance, validated_data):
        # Update the project fields
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Handle members
        members_data = validated_data.pop('members', [])
        for member_data in members_data:
            user_id = member_data['user'].id
            role = member_data['role']
            ProjectMember.objects.update_or_create(
                project=instance,
                user_id=user_id,
                defaults={'role': role},
            )

        return instance

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