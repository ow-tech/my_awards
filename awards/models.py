from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_name = models.CharField(max_length=30)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='images/', default='some string')
    project_live_link =models.URLField(max_length=100000, default='some string')



    def __str__(self):
        return self.author, self.project_name

 
    def save_project(self):
        self.save()

    @classmethod
    def delete_project(cls, id):
        project = cls.objects.filter(id).all()
        project.delete()