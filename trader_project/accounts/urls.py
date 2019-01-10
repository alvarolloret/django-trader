from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

from django.urls import include, path

from .views import accounts, students


app_name = 'accounts'

urlpatterns = [
    path('', accounts.home, name='home'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        # path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        # path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        # path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'accounts'), namespace='students')),
]
