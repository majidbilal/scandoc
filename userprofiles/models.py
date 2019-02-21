from PIL import Image

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics')
    bio = models.TextField(blank=True, verbose_name='Biography')

    def __str__(self):
        print(self.user)
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)


