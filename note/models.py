from django.db import models

# Create your models here.
class Note(models.Model):
  # judul = models.CharField(max_length=200)
  makul = models.CharField(max_length=50)
  deskripsi = models.CharField(max_length=250)
  tenggat = models.DateTimeField("Tenggat Waktu")  
 
  def __str__(self):
    return self.makul