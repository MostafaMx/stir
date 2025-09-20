from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
# Create your models here.

class Person(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username
class Meetingtime(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='meetingtimes',null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    favouraite = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    message = models.TextField(max_length=10000)
    def __str__(self):
        return f'Meetingtime by {self.name}'

class Service(models.Model):
    title = models.CharField(max_length=200)
    bio = models.CharField(max_length=400)
    description = models.TextField()
    imageicon = models.FileField(upload_to='pics/',
    validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg','svg'])], null=True, blank=True)
    info = models.CharField(max_length=800)
    examples = models.JSONField(default=list)
    mainpicture = models.ImageField(upload_to='uploaded_images/',null=True, blank=True)



    def __str__(self):
        return self.title

class Question(models.Model):
    name = models.CharField(max_length=100)
    thequestion = models.TextField(max_length=10000)
    theanswer = models.TextField(max_length=10000)
    def __str__(self):
        return f'Question by {self.name}'