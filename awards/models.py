from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_name = models.CharField(max_length=30)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='images/', default='some string')
    project_live_link =models.URLField(max_length=100000, default='enter live link')



    def __str__(self):
        return '{},{}'.format(self.author, self.project_name)

 
    def save_project(self):
        self.save()

    # @classmethod
    # def delete_project(cls, id):
    #     project = cls.objects.filter(id).all()
    #     project.delete()
    @classmethod
    def search_by_project_name(cls, search_term):
        projects = cls.objects.filter(project_name__icontains=search_term)
        return projects


    @classmethod
    def get_single_image_by_id(cls, id):
        project = cls.objects.filter(pk=id)
        return project

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return '{}'.format(self.user)


  
