from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='user_images')
    first_name = models.CharField(verbose_name='Имя', max_length=150, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150, null=True)
    father_name = models.CharField(verbose_name='Отчество', max_length=150, null=True)
    bio = models.TextField(verbose_name='О себе', max_length=4000, null=True)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def get_absolute_url(self):
        return reverse('list-detail', kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

class UsersList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwards):
    instance.profile.save()
