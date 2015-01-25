from django.db import models


class Webservicedoc(models.Model):
    wadl_raw = models.TextField()
