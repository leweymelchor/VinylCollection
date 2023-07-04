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
)


urlpatterns = [
    path("", RecordListView.as_view(), name="records_list"),
    path("add/record", RecordCreateView.as_view(), name="record_add"),
    path("add/artist/", ArtistCreateView.as_view(), name="artist_add"),
    path("record/<int:pk>/", RecordDetailView.as_view(), name="record_detail"),
    path("<int:pk>/", ArtistRecordsView.as_view(), name="artist_records"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("<int:pk>/edit/", RecordUpdateView.as_view(), name="record_edit"),
    path("<int:pk>/delete/", RecordDeleteView.as_view(), name="record_delete"),
]
