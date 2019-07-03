from django.db import models

# Create your models here.
class exceptionlogs(models.Model):
    filename = models.CharField(max_length=100, null=True)
    lineno = models.CharField(max_length=10, null=True)
    code = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=200, null=True)
    time = models.DateTimeField(auto_now_add=True)
