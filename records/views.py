from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

from records.forms import SignUpForm, ProfileForm, RecordForm #, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from records.models import Artist, Record

from django.db.models import Q

from django.shortcuts import get_object_or_404
from django.db.models import Sum



# CREATES TITLES FOR EACH TEMPLATE VIEW
class PageTitleViewMixin:
    title = ""

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


# SEARCH ARTIST / ALBUMS
class SearchResultsView(LoginRequiredMixin, PageTitleViewMixin, ListView):
    paginate_by = 25
    model = Record
    template_name = "records/search_results.html"

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        return Record.objects.filter(
        Q(album__icontains=query) | Q(artist__artist__icontains=query) | Q(date__icontains=query) | Q(price__icontains=query)).order_by('artist', 'date')

    def get_title(self):
        query = self.request.GET.get("q")
        return "Search results for " + str(query)


# ADD NEW ARTIST
class ArtistCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Artist
    template_name = "records/artist_add.html"
    fields = ["artist"]
    success_url = reverse_lazy("record_add")
    title = "New Artist"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# CREATES RECORDS
class RecordCreateView(LoginRequiredMixin, PageTitleViewMixin, CreateView):
    model = Record
    form_class = RecordForm
    template_name = "records/record_add.html"
    # fields = ["album", "artist", "artwork", "date", "price"]
    success_url = reverse_lazy("records_list")
    title = "New Record"

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display artist that belong to a given user"""

        kwargs = super(RecordCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form.instance.owner)


# LISTS ALL RECORDS IN USERS DB
class RecordListView(LoginRequiredMixin, PageTitleViewMixin, ListView):
    paginate_by = 10
    model = Record
    template_name = "records/record_list.html"
    title = "Vinyl Reserve"
    context_object_name = "records"

    def get_queryset(self):
        owner = self.request.user.id

        records = Record.objects.filter(owner=owner).order_by('artist', 'date')

        total = records.aggregate(total=Sum('price'))['total']

        if total is None:
            total = 0

        # Add the total_price to the view's context data
        self.total = total
        return records

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        def format_with_commas(number):
            parts = f"{number:,.2f}".split(".")
            return ".".join(parts)

        number = self.total
        formatted_number = format_with_commas(number)
        context['total'] = formatted_number
        return context


# LISTS ALL RECORDS IN USERS DB
class CreatedListView(LoginRequiredMixin, PageTitleViewMixin, ListView):
    paginate_by = 10
    model = Record
    template_name = "records/record_created_list.html"
    title = "Vinyl Reserve"
    context_object_name = "records"

    def get_queryset(self):
        owner = self.request.user.id

        records = Record.objects.filter(owner=owner).order_by('-created_at', 'artist')
        return records

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


# LISTS ALL RECORDS BY SELECTED ARTIST
class ArtistRecordsView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Record
    template_name = "records/artist_records.html"

    def get_context_data(self, *args, **kwargs):
        owner = self.request.user.id
        records = Record.objects.filter(owner=owner, artist=self.object.artist).order_by('date')
        context = super(ArtistRecordsView, self).get_context_data(*args, **kwargs)
        context['records'] = records
        return context

    def get_title(self):
        return str(self.object.artist) + "'s Albums"



# SHOWS DETAILS OF SELECTED RECORD
class RecordDetailView(LoginRequiredMixin, PageTitleViewMixin, DetailView):
    model = Record
    template_name = "records/record_detail.html"

    def get_title(self):
        return str(self.object.album)


# EDITS SELECTED RECORD
class RecordUpdateView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = Record
    form_class = RecordForm
    template_name = "records/record_edit.html"
    # fields = ["artist", "album", "artwork", "date", "price"]

    def get_success_url(self):
        record_id = self.kwargs['pk']
        return reverse_lazy("record_detail", kwargs={"pk": record_id})

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display artist that belong to a given user"""

        kwargs = super(RecordUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_title(self):
        return "EDIT - " + str(self.object.album) + " BY - " + str(self.object.artist)


# DELETES SELECTED RECORD
class RecordDeleteView(LoginRequiredMixin, PageTitleViewMixin, DeleteView):
    model = Record
    template_name = "records/record_delete.html"
    success_url = reverse_lazy("records_list")

    def get_title(self):
        return "DELETE - " + self.object.album


class SignUpView(PageTitleViewMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    title = "Sign-up"


class ProfileView(LoginRequiredMixin, PageTitleViewMixin, UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/profile.html'

    def get_title(self):
        return "Update " + self.object.username + "'s Profile"


# class LoginView(PageTitleViewMixin):
#     form_class = LoginForm
#     success_url = reverse_lazy('home')
#     template_name = 'registration/login.html'
#     title = "Vinyl Reserve Log-in"
