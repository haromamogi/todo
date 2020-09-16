from django.db import models


class Todo(models.Model):

    duty = models.CharField('やること', max_length=140)
    limit = models.IntegerField('期限n（例、3以内）', blank=True, default=0)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    existence = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.duty
