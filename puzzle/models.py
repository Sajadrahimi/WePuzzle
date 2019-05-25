import time

from django.db import models


# Create your models here.



class puzzle(models.Model):
    puzzle_title = models.TextField()
    puzzle_image = models.ImageField(upload_to='puzzle_images', blank=True)
    puzzle_image_width_height = models.IntegerField(blank=False, default=100)
    puzzle_audio = models.FileField(upload_to='puzzle_audios', blank=True, null=True)
    puzzle_description = models.TextField(blank=True)
    puzzle_password = models.TextField()
    puzzle_url = models.CharField(max_length=50, blank=False, default="127.0.0.1")
    previous_puzzle = models.OneToOneField('puzzle.puzzle', null=True, blank=True,
                                           on_delete=models.SET_NULL, related_name='related_next_puzzle')
    next_puzzle = models.OneToOneField('puzzle.puzzle', null=True, blank=True,
                                       on_delete=models.SET_NULL, related_name='related_previous_puzzle')

    puzzle_hinted_password = models.ManyToManyField('hint_password', blank=True)

    def __str__(self):
        return self.puzzle_title


class hint_password(models.Model):
    hint_value = models.TextField(blank=True, null=True)
    hinted_page = models.ForeignKey('wrong_page', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.hint_value


class wrong_page(models.Model):
    wrong_page_title = models.CharField(max_length=30, blank=True, default="Wrong")
    wrong_page_description = models.TextField(blank=True)
    wrong_page_image = models.ImageField(upload_to='wrong_page_images')

    def __str__(self):
        return self.wrong_page_title


class Answer(models.Model):
    answer_content = models.TextField()
    answer_created_by = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    answer_created_time = models.DateTimeField()
    def __str__(self):
        return self.answer_content
