

from django.db import models

class Posts(models.Model):
  title = models.CharField(max_length=100)
  post = models.TextField()
  date = models.DateTimeField()

  def __str__(self):
    return  self.title


