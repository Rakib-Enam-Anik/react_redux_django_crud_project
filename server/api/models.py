from django.db import models

# Create your models here.

class Project(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnail/images', null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=50)
    description = models.TextField()
    demo = models.CharField(max_length=200, null=True, blank=True)
   # price = models.DecimalField(max_places=2, decimal_places=5)
    
    def __str__(self):
        return self.title