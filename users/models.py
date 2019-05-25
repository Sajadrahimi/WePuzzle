from django.db import models
from django.contrib.auth.models import User as djangoUser
from puzzle.models import puzzle


# Create your models here.
class User(djangoUser):
    last_solved_puzzle = models.ForeignKey('puzzle.puzzle', on_delete=models.CASCADE, unique=False,
                                           null=True, blank=True, related_name='puzzle_solved_by',
                                           default=puzzle.objects.order_by('pk')[0].id)
