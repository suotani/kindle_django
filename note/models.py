from django.db import models

class Note(models.Model):
  SCORE_CHOICE = ((1, "低"),(2, "普通"),(3,"重要"),(4,"最重要"),(5,"緊急"))
  title = models.CharField(max_length=100)
  score = models.IntegerField(choices=SCORE_CHOICE)
  text = models.TextField()

  def __str__(self):
    return "[%s]%s(%s)" % (self.id, self.title, self.score)