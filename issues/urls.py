from django.urls import path 
from issues import views 


urlpatterns = [
    path("new/", views.IssueCreateView.as_view(), name="new"),
    path("<int:pk>/", views.IssueDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.IssueUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.IssueDeleteView.as_view(), name="delete"),
    path("", views.IssueListView.as_view(), name="list"),
]