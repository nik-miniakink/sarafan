import datetime

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Activity(models.Model):

    objects = None
    type_of_activity = [
        ('bike', 'bike'),
        ('walking', 'walking'),
        ('run', 'run')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.datetime.now())
    stop_time = models.DateTimeField(default=datetime.datetime.now())
    type = models.CharField(choices=type_of_activity, max_length=10)
    distance = models.IntegerField()
    calories = models.IntegerField()

    # def create_superuser(self, email, , password=None):
    #     user = self.create_user(
    #         email,
    #
    #         password=password,
    #         is_staff=True,
    #         is_admin=True,
    #     )
    #     return user
