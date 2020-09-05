from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    writer = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote
