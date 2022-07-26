from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.constraints import UniqueConstraint


class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField()
    genre = models.CharField(max_length=255)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'author'], name='unique_book')
        ]


class Tracking(models.Model):
    WANT_TO_READ = 'WTR'
    READING = 'R'
    FINISHED = 'F'
    STATUS_CHOICES = [
        (WANT_TO_READ, 'Want to read'), (READING, 'Reading'), (FINISHED, 'Finished'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracker')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=WANT_TO_READ)

    def __str__(self):
        return self.status


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes', null=True)
    note = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()

    def __str__(self):
        return self.note
