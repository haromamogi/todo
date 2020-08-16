from django.db import models


class Todo(models.Model):

    duty = models.CharField('やること', max_length=140)
    limit = models.IntegerField('期限n（例、3以内）', blank=True, default=0)

    def __str__(self):
        return self.duty
