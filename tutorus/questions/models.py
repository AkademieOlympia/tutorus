from django.db import models

ASKED = 'asked'
ANSWERED = 'answered'
DELETED = 'deleted'
QUESTION_CHOICES = (
    (ASKED, 'asked'),
    (ANSWERED, 'answered'),
    (DELETED, 'deleted'),
)

class Question(models.Model):
    """
    Start off with, following fields;

    - Subject (charfield)
    - Question Content (textfield)
    - Status (asked, answered, deleted, etc???)
    - Link to Class (foreignkey)

    But think of possible need to expand or handle # of upvotes on question or
    percentage of students in the class that have upvoted the particular
    question.
    """
    subject = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField(blank=True, null=True, default="")
    status = models.CharField(max_length=10,
                              choices=QUESTION_CHOICES,
                              default=ASKED)

    # class = models.ForeignKey(Class)