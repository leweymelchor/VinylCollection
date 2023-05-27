from django.urls import path

from records.views import (
    # create_record,
    ArtistCreateView,
    RecordListView,
    RecordCreateView,
    RecordDetailView,
)


urlpatterns = [
    path("", RecordListView.as_view(), name="records_list"),
    # path("add/record", create_record, name="record_add"),
    path("add/record", RecordCreateView.as_view(), name="record_add"),
    path("add/artist/", ArtistCreateView.as_view(), name="artist_add"),
    path("<int:pk>/", RecordDetailView.as_view(), name="record_detail"),
    # path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    # path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    # path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
]
