from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from records.models import Artist, Record

# IMPORTS FOR FUNCTION VIEWS
# from records.forms import RecordForm


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


class RecordDetailView(PageTitleViewMixin, DetailView):
    model = Record
    template_name = "records/detail.html"

    def get_title(self):
        return str(self.object.artist) + " Vinyls"


# def create_record(request):
#     if request.method == "POST" and RecordForm:
#         form = RecordForm(request.POST)
#         if form.is_valid():
#             record = form.save()
#             return redirect("record_detail", pk=record.pk)
#     elif RecordForm:
#         form = RecordForm()
#     else:
#         form = None
#     context = {
#         "form": form,
#     }
#     return render(request, "records/add.html", context)
