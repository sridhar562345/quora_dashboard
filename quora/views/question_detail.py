from django.db.models import Count
from django.shortcuts import redirect, render

from quora.forms.answer_form import AnswerForm
from quora.models import Question, Answer


def question_detail_view(request, pk):
    question = Question.objects.get(pk=pk)
    answers = (
        Answer.objects.filter(question=question)
        .annotate(likes=Count("like"))
        .order_by("-likes")
    )

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.posted_by = request.user
            answer.save()
            return redirect("question_detail", pk=pk)
    else:
        form = AnswerForm()

    return render(
        request,
        "question_detail.html",
        {"question": question, "answers": answers, "form": form},
    )
