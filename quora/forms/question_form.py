from django import forms

from quora.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text"]
