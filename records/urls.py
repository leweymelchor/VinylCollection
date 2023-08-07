from django.urls import path

from records.views import (
    RecordListView,
    RecordCreateView,
    RecordDetailView,
    RecordUpdateView,
    RecordDeleteView,
    ArtistCreateView,
    ArtistRecordsView,
    SearchResultsView,
    CreatedListView,
)


urlpatterns = [
    path("", RecordListView.as_view(), name="records_list"),
    path("created", CreatedListView.as_view(), name="records_created_list"),
    path("add/record", RecordCreateView.as_view(), name="record_add"),
    path("add/artist/", ArtistCreateView.as_view(), name="artist_add"),
    path("record/<int:pk>/", RecordDetailView.as_view(), name="record_detail"),
    path("<int:pk>/", ArtistRecordsView.as_view(), name="artist_records"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("<int:pk>/edit/", RecordUpdateView.as_view(), name="record_edit"),
    path("<int:pk>/delete/", RecordDeleteView.as_view(), name="record_delete"),
]
