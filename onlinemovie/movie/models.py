from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    year=models.IntegerField()
    language=models.CharField(max_length=30)
    pic=models.ImageField(upload_to='picture',null=True,blank=True)

    def __str__(self):
        return self.name
