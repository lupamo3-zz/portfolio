from django.db import models

# Create your models here.
class Portfolio(models.Model):
    viewmore=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    view=models.CharField(max_length=25)
    portfolio=models.ImageField(upload_to = 'image/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']