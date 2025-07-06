from django.db import models
from django.contrib.auth.models import User  # Use built-in User model for creator and assignment

class Project(models.Model):
    name = models.CharField(max_length=100)  # Project title
    description = models.TextField()  # Project details
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Linked user who created the project
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation

    def __str__(self):
        return self.name  # Display name in admin and lists

class Task(models.Model):
    STATUS_CHOICES = [  # Task status options
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Task is linked to a project
    title = models.CharField(max_length=100)  # Task name
    description = models.TextField()  # Task details
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Optional assigned user
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')  # Track progress
    due_date = models.DateField()  # Deadline
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"  # Show task title and readable status