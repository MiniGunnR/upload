from __future__ import unicode_literals

from django.db import models

class Image(models.Model):
    file = models.ImageField(upload_to='alpha/uploads/')
