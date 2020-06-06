from django.test import TestCase
from .models import Project


class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_project= Project(project_name='Delani', project_description="A website for delani photo studio")

    def test_instance(self):
        self.assertTrue( isinstance(self.new_project, Project))

    def test_save_method(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) >0)

    def test_delete_method(self, id):
        self.new_project.save_project()
        self.new_project.delete_project(id)
        after = Project.object.all()
        self.assertTrue(len(after)< 1)
