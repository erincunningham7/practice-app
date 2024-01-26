from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class HelloKitty(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    cat_age = models.IntegerField()

    def __str__(self):
        return self.name
