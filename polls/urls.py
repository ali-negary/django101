from django.urls import path
from . import views


app_name = 'polls'

# for generic views we should use keys in the format: <int:pk>
urlpatterns = [
    # for example: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # for example: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # for example: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # for example: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
