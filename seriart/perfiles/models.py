from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    clave = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.id} : {self.user.username}'

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        perfil = Perfil.objects.create(user=instance)
        perfil.save()