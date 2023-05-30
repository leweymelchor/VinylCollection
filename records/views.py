from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from records.models import Artist, Record

from django.db.models import Q


# CLASS BASED VIEWS
class PageTitleViewMixin:
    title = ""

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class ArtistCreateView(PageTitleViewMixin, CreateView):
    model = Artist
    template_name = "records/addartist.html"
    fields = ["artist"]
    success_url = reverse_lazy("record_add")
    title = "New Artist"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecordListView(PageTitleViewMixin, ListView):
    paginate_by = 10
    model = Record
    template_name = "records/list.html"
    title = "Vinyl Catologue"


class RecordCreateView(PageTitleViewMixin, CreateView):
    model = Record
    template_name = "records/add.html"
    fields = ["artist", "album", "artwork", "date", "price"]
    success_url = reverse_lazy("records_list")
    title = "New Record"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArtistRecordsDetailView(PageTitleViewMixin, DetailView):
    model = Record
    template_name = "records/artistrecordsdetail.html"

    def get_title(self):
        return str(self.object.artist) + " Vinyls"

    def get_context_data(self, *args, **kwargs):
        records = Record.objects.filter(artist=self.object.artist)
        context = super(ArtistRecordsDetailView, self).get_context_data(*args, **kwargs)

        context['records'] = records
        return context


class SearchResultsView(ListView):
    model = Record
    template_name = "records/search_results.html"

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        # artist_name = Record.objects.filter(artist=self.object.artist)
        # context = super(ArtistRecordsDetailView, self).get_context_data(*args, **kwargs)
        # context['artists'] = artist_name
        return Record.objects.filter(
        Q(album__icontains=query)
        )

#       | Q(artist__icontains=artist_name
