from django.db import models
from django.utils.translation import ugettext_lazy as _

from classroom.models import ClassRoom
from questions import constants


class Question(models.Model):

    subject = models.CharField(_('Subject'), max_length=50, blank=False,
                               null=False)
    content = models.TextField(_('Content'), blank=True, null=True, default="")
    status = models.CharField(max_length=10,
                              choices=constants.QUESTION_CHOICES,
                              default=constants.ASKED)
    classroom = models.ForeignKey(ClassRoom, blank=None, null=True)
