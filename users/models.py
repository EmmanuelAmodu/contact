from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=200, unique=True, default="")
    email = models.EmailField()

    def __str__(self):
        return  self.name