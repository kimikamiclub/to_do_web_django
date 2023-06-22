import datetime

from django.db import models


class TaskItem(models.Model):
    DEFAULT = 'DEFAULT'
    PERSONAL = 'PERSONAL'
    SHOPPING = 'SHOPPING'
    WISHLIST = 'WISHLIST'
    WORK = 'WORK'
    SPORT = 'SPORT'
    CATEGORIES = (
        (DEFAULT, DEFAULT),
        (PERSONAL, PERSONAL),
        (SHOPPING, SHOPPING),
        (WISHLIST, WISHLIST),
        (WORK, WORK),
        (SPORT, SPORT)
    )

    TO_DO = 'TO_DO'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    BLOCK = 'BLOCK'
    STATUS = (
        (TO_DO, TO_DO),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
        (BLOCK, BLOCK)
    )

    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    due_date = models.DateField(default=datetime.datetime.now())
    status = models.CharField(max_length=20, choices=STATUS, default=TO_DO)
    category = models.CharField(max_length=20, choices=CATEGORIES, default=DEFAULT)

    def __str__(self):
        return f'{self.title}'
