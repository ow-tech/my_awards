from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField

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
    # phone_number = models.TextField(default='0723475857842974')
    email = models.EmailField(default='Your email')

    def __str__(self):
        return '{}'.format(self.user)
class Review(models.Model):
    rates = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rates, default=0)
    usability = models.IntegerField(choices=rates, default=0)
    content = models.IntegerField(choices=rates, default=0)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    score = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)

    def __str__(self):
        return '{}{}'.format(self.user, self.project)

  
