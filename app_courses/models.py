from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Course(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"), blank=True)
    author = models.CharField(_("author"), max_length=50)
    thumbnail = models.ImageField(_("thumbnail"), upload_to="thumbnails/", blank=True)
    url = models.URLField(_("video or playlist link"), max_length=200, blank=True)
    added_by = models.ForeignKey(get_user_model(), verbose_name=_("added by"), on_delete=models.CASCADE)
    added_on = models.DateField(_("added on"), auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
