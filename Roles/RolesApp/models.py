from django.db import models


class Tasks(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    Task = models.CharField(max_length=100)
    Status = models.CharField(max_length=20)
    Employee = models.IntegerField

    def __str__(self):
        return self.Title


