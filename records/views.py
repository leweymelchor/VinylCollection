from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from records.models import Artist, Record

from django.db.models import Q


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
class SearchResultsView(PageTitleViewMixin, ListView):
    model = Record
    template_name = "records/search_results.html"

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        return Record.objects.filter(
        Q(album__icontains=query) | Q(artist__artist__icontains=query))

    def get_title(self):
        query = self.request.GET.get("q")
        return "Search results for " + str(query)


# ADD NEW ARTIST
class ArtistCreateView(PageTitleViewMixin, CreateView):
    model = Artist
    template_name = "records/addartist.html"
    fields = ["artist"]
    success_url = reverse_lazy("record_add")
    title = "New Artist"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# CREATES RECORDS
class RecordCreateView(PageTitleViewMixin, CreateView):
    model = Record
    template_name = "records/add.html"
    fields = ["artist", "album", "artwork", "date", "price"]
    success_url = reverse_lazy("records_list")
    title = "New Record"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# LISTS ALL RECORDS IN DB
class RecordListView(PageTitleViewMixin, ListView):
    paginate_by = 10
    model = Record
    template_name = "records/list.html"
    title = "Vinyl Catologue"


# LISTS ALL RECORDS BY SELECTED ARTIST
class ArtistRecordsView(PageTitleViewMixin, DetailView):
    model = Record
    template_name = "records/artist_records.html"

    def get_context_data(self, *args, **kwargs):
        records = Record.objects.filter(artist=self.object.artist)
        context = super(ArtistRecordsView, self).get_context_data(*args, **kwargs)
        context['records'] = records
        return context

    def get_title(self):
        return str(self.object.artist) + "'s Albums"


# SHOWS DETAILS OF SELECTED RECORD
class RecordDetailView(PageTitleViewMixin, DetailView):
    model = Record
    template_name = "records/recorddetail.html"

    def get_title(self):
        return str(self.object.album)


# EDITS SELECTED RECORD
class RecordUpdateView(PageTitleViewMixin, UpdateView):
    model = Record
    template_name = "records/edit.html"
    fields = ["artist", "album", "artwork", "date", "price"]

    def get_success_url(self):
        record_id = self.kwargs['pk']
        return reverse_lazy("record_detail", kwargs={"pk": record_id})

    def get_title(self):
        return "EDIT - " + str(self.object.album) + " BY - " + str(self.object.artist)


# DELETES SELECTED RECORD
class RecordDeleteView(PageTitleViewMixin, DeleteView):
    model = Record
    template_name = "records/delete.html"
    success_url = reverse_lazy("records_list")

    def get_title(self):
        return "DELETE - " + self.object.album
