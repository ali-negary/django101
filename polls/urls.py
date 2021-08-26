from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # for example: /polls/
    path('', views.index, name='index'),
    # for example: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # for example: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # for example: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
