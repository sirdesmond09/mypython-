from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 150)
    content = models.TextField(max_length = 2500)

    def __str__(self):
        return self.title