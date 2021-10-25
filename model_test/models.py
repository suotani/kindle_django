from django.db import models

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField(default=0)
  score = models.IntegerField(default=0)

  def __str__(self):
    return "id: %s name: %s" % (self.id, self.name)