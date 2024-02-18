from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9]*$')


class Tovar(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', "DRAFT"
        PUBLISHED = 'PB', "PUBLISHED"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='babka_posts')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    cost = models.CharField(max_length=50, validators=[alphanumeric], null = True)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title
