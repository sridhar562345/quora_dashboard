from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from quora.forms.question_form import QuestionForm


@login_required
def ask_question_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.posted_by = request.user
            question.save()
            return redirect("question_list")
    else:
        form = QuestionForm()
    return render(request, "ask_question.html", {"form": form})
