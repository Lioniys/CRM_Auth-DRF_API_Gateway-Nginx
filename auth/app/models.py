from django.conf import settings
from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="info")
    in_owner = models.BooleanField(default=False)
    company = models.ForeignKey("Company", on_delete=models.PROTECT, blank=True, null=True, related_name="staff")

    class Meta:
        ordering = ['id']


class Company(models.Model):
    title = models.CharField(max_length=50)
    is_paid_for = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
