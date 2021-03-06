from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=3000)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
