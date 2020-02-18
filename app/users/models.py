import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.template.loader import render_to_string
from core import managers as core_managers


class User(AbstractUser):
    """ Custom User model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    # 성별 선택
    GENDER_CHOICE = (
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    )

    # 언어 선택
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, _("Korean")),
        (LANGUAGE_ENGLISH, _("English")),
    )

    # 화폐 선택
    CURRENCY_USD = "usd"
    CURRENCY_WON = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_WON, "KRW"),
        (CURRENCY_USD, "USD"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    # 프로필 이미지
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        _("gender"), choices=GENDER_CHOICE, max_length=10, blank=True
    )
    bio = models.TextField(_("bio"), blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        _("language"),
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
        default=LANGUAGE_KOREAN,
    )
    currency = models.CharField(choices=LANGUAGE_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    objects = core_managers.CustomModelManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_messgae = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                subject=_("Verify Airbnb Account"),
                message=None,
                from_email=settings.EMAIL_FROM,
                recipient_list=[self.email],
                fail_silently=False,
                html_message=html_messgae,
            )
            self.save()
        return
