from django.urls import path

from main.gitsvn import views

app_name = "git"

urlpatterns = [
    path(
        route="",
        view=views.GitHomeView.as_view(),
        name="git_list_view",
    ),
    path(
        route="project/<pk>/",
        view=views.GitProjectDetail.as_view(),
        name="git_detail_view",
    ),

]
