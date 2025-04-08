from django import forms

from quora.models import Answer  # Assuming you have an Answer model


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text"]
