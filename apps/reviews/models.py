from django.db import models

from apps.users.models import UserProfile


class Review(models.Model):
    MAX_STARS = 5
    RATING_STARS = (
            (1, 'One star'),
            (2, 'Two stars'),
            (3, 'Three stars'),
            (4, 'Four stars'),
            (5, 'Five stars'),
    )
    user_profile = models.ForeignKey(UserProfile)
    book = models.ForeignKey('books.Book')
    content = models.TextField(blank=True, default='')
    updated_time = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=RATING_STARS, default=4)

    class Meta:
        db_table = 'review'
