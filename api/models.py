from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return self.title