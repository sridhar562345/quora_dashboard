from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from quora.models import Answer, Like


@login_required
def like_answer_view(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    Like.objects.create(answer=answer, user=request.user)
    return HttpResponseRedirect(
        reverse("question_detail", args=[answer.question.pk])
    )
