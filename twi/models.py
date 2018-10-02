from __future__ import unicode_literals

from datetime import datetime
from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    published_at = models.DateTimeField('date published', default=datetime.now, blank=True)
