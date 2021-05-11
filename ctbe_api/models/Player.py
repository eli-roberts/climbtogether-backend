from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

class Player(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  league_id = models.CharField(max_length=16)
  verified = models.BooleanField(null=False, default=False)
  reputation = models.IntegerField(null=False, default=0)

  class Meta:
      verbose_name = ("artist")
      verbose_name_plural = ("artists")

  def __str__(self):
    return self.name