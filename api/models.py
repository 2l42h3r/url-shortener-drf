from django.db import models

class UrlList(models.Model):
    fullurl = models.CharField(max_length=255)
    shortened = models.CharField(max_length=10)

    def __str__(self):
        return self.shortened
