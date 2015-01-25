from django.db import models


class Webservicedoc(models.Model):
    dwml_raw = models.TextField()

    def __str__(self):              
        return self.dwml_raw
