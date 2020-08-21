from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password=None, **extra_fields):
        try:
            user = self.model(
                username=username,
                nickname=nickname,
            )
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            user.set_password(password)
            user.is_active = True
            user.save()
            return user
        except Exception as e:
            print(e)

    def create_superuser(self, username, nickname, password=None, **extra_fields):
        try:
            superuser = self.create_user(
                username=username,
                nickname=nickname,
                password=password,
            )
            superuser.is_admin = True
            superuser.is_superuser = True
            superuser.is_active = True
            superuser.is_staff = True
            superuser.save()
            return superuser
        except Exception as e:
            print(e)


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, null=False, unique=True)
    nickname = models.CharField(max_length=20, null=False)
    email=models.EmailField(max_length=255, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    objects = UserManager()

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20)
    address=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=255)
    warning=models.PositiveIntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            user=instance
            Profile.objects.create(user=user)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()