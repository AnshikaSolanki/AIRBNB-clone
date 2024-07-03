from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "eng"
    LANGUAGE_HINDI = "hin"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_HINDI, "Hindi")
    )

    CURRENCY_USD = "usd"
    CURRENCY_RUPPEE = "rs"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_RUPPEE, "RUPPEE")
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=3, default="English")
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, default="RUPEE")
    superhost = models.BooleanField(default=False)
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)
