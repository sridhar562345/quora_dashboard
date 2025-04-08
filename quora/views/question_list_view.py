from django.shortcuts import render

from quora.models import Question


def question_list_view(request):
    questions = Question.objects.all().order_by("-created_at")
    return render(request, "question_list.html", {"questions": questions})
