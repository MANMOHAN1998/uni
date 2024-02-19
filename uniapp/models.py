from django.db import models

class ContactedUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class NewsLetterSubscribers(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name