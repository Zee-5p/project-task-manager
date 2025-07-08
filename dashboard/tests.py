from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Project, Task
from django.urls import reverse
from datetime import date

class DashboardTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.client = Client()
        self.client.login(username='testuser', password='pass')
        self.project = Project.objects.create(
            name='Test Project',
            description='Description here',
            created_by=self.user
        )
        self.task = Task.objects.create(
            project=self.project,
            title='Test Task',
            description='Do something',
            assigned_to=self.user,
            status='TODO',
            due_date=date.today()
        )

    def test_project_str(self):
        self.assertEqual(str(self.project), 'Test Project')

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task (To Do)')

    def test_project_list_view(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')