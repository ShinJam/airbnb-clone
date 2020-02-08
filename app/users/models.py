from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom User model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    # 성별 선택
    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    # 언어 선택
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_ENGLISH, "English"),
    )

    # 화폐 선택
    CURRENCY_USD = "usd"
    CURRENCY_WON = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_WON, "KRW"),
        (CURRENCY_USD, "USD"),
    )

    # 프로필 이미지
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=CURRENCY_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    superhost = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        pass