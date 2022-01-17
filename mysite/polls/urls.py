from django.urls import path

from . import views

# By setting the app name, url references are not confused between apps with the same naming conventions
app_name = 'polls'

urlpatterns = [
    ###
#   Patterns for /polls/
    ###
    path('', views.index, name='index'),
    path('<int:render_method_num>/', views.index, name='index'),
    # EG /polls/5:
    path('question/<int:question_id>/', views.detail, name='detail'),
    # EG /polls/5/results/:
    path('question/<int:question_id>/results/', views.results, name='results'),
    # EG /polls/5/vote/:
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
]