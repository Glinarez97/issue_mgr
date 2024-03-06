from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView
)

from django.urls import reverse_lazy
from .models import Issue, Status

class IssueCreateView(CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["summary", "description", "priority", "assignee"]

    def form_valid(self, form):
        to_do_status = Status.objects.get(name="to do")
        form.instance.reporter = self.request.user
        form.instance.status = to_do_status
        return super().form_valid(form)
    
class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue
    
class IssueUpdateView(UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["summary", "description", "priority", "status", "assignee"]
    
class IssueDeleteView(DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("list")
    
class IssueListView(ListView):
    template_name = "issues/list.html"  # Corrected template name
    model = Issue
