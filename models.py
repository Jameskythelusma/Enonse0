from django.db import models

# Create your models here.

class kontinan(models.Model):
    non = models.CharField(max_length=255)

    def __str__(self):
        return self.non

class peyi(models.Model):
    non = models.CharField(max_length=255)
    popilasyon = models.PositiveIntegerField()
    sipefisi = models.PositiveIntegerField()
    kontinan = models.ForeignKey(kontinan, on_delete=models.CASCADE)
    langaj = models.ManyToManyField('langaj', related_name='peyi')

    def __str__(self):
        return self.non
    
class langaj(models.Model):
    non = models.CharField(max_length=255)

    def __str__(self):
        return self.non

