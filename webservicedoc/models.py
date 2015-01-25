from django.db import models


class Webservicedoc(models.Model):
    dwml_raw = models.TextField()
