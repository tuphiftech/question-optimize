# Python imports
from decimal import Decimal

# Django imports
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class UnderstandState(models.TextChoices):
    EASY = "EASY", _("EASY")
    MEDIUM = "MEDIUM", _("MEDIUM")
    WELLKNOWN = "WELLKNOWN", _("WELLKNOWN")
    MASTERED = "MASTERED", _("MASTERED")


class QuestionType(models.TextChoices):
    SINGLE_CHOICE = "SINGLE_CHOICE", _("SINGLE_CHOICE")
    MULTI_CHOICES = "MULTI_CHOICES", _("MULTI_CHOICES")
    CONSTRUCTED_RESPONSES = "CONSTRUCTED_RESPONSES", _("CONSTRUCTED_RESPONSES")
    MULTI_QUESTIONS = "MULTI_QUESTIONS", _("MULTI_QUESTIONS")


# Create your models here.
class Question(models.Model):
    content = models.TextField(blank=True, null=True)
    question_type = models.CharField(
        max_length=30,
        choices=QuestionType.choices,
        default=QuestionType.SINGLE_CHOICE,
    )
    difficulty = models.CharField(
        max_length=30,
        choices=UnderstandState.choices,
        default=UnderstandState.EASY,
        blank=True,
        null=True,
    )
    parent_question = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="sub_questions",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    choices = models.JSONField(null=True, blank=True)
    true_choices = ArrayField(models.IntegerField())

    def get_true_choices(self):
        return [
            i
            for i, choice in enumerate(self.choices)
            if choice.get("is_right", False) is True
        ]
