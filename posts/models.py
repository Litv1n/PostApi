from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')

    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title
