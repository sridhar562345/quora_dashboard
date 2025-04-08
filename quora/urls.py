from django.urls import path
from quora import views
from quora.views.ask_question import ask_question_view
from quora.views.like_view import like_answer_view
from quora.views.login_view import login_view, logout_view
from quora.views.question_detail import question_detail_view
from quora.views.question_list_view import question_list_view
from quora.views.register_view import register_view

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("", question_list_view, name="question_list"),
    path("ask/", ask_question_view, name="ask_question"),
    path("question/<int:pk>/", question_detail_view, name="question_detail"),
    path("like/<int:answer_id>/", like_answer_view, name="like_answer"),
]
