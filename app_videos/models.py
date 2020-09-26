from django.db import models
from app_courses.models import Course
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Video(models.Model):
    title = models.CharField(_("title"), max_length=50)
    course = models.ForeignKey(Course, verbose_name=_("course"), related_name="videos", on_delete=models.CASCADE)
    url = models.URLField(_("video link"), max_length=200, blank=True)

    def __str__(self):
        return self.title
