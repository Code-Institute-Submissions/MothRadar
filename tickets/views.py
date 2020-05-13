from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from comments.forms import EditCommentForm
from upvotes.models import Upvote
from .models import Ticket


# Create your views here.
def home(request):
    return render(request, "tickets/home.html", {"title": "Homepage"})


class TicketCreateView(CreateView):
    model = Ticket
    fields = ["title", "description", "ticket_type"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketDetailView(DetailView):
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        voter = self.request.user
        upvoted = Upvote.objects.filter(ticket=self.object.id, upvoter=voter.id)

        context["comments"] = Comment.objects.filter(
            rel_ticket=self.object.id
        ).order_by("created")
        context["upvotes"] = Upvote.objects.filter(ticket=self.object.id).count()

        if upvoted:
            context["uv_status"] = False
        else:
            context["uv_status"] = True

        return context


class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ["title", "description", "ticket_type"]


class TicketDeleteView(DeleteView):
    model = Ticket
    success_url = reverse_lazy("ticket-list")


class TicketListView(ListView):
    paginate_by = 5
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["path"] = self.request.path
        return context

    # solution adapted from a post on Stack Overflow using Django documentation
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(description__icontains=search)
        return queryset


class BugListView(TicketListView):
    queryset = Ticket.objects.filter(ticket_type="BUG")


class FeatureListView(TicketListView):
    queryset = Ticket.objects.filter(ticket_type="FEATURE")


class UpvoteSortedListView(TicketListView):
    queryset = Ticket.objects.all().annotate(votes=Count("upvotes")).order_by("-votes")
