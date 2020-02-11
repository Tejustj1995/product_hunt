from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=20)
    body = models.CharField(max_length=1000)
    url = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def bod(self):
        return self.body[:100]


