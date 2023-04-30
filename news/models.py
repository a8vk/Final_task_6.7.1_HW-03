from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse


class New(models.Model):
    CATEGORIES_CHOICES = [('uncos', 'Новости'), ('articles', 'Статьи')]

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES, default='uncos')
    data_pub = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.title)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
