from django.urls import path

from records.views import (
    RecordListView,
    RecordCreateView,
)


urlpatterns = [
    path("", RecordListView.as_view(), name="records_list"),
    # path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", RecordCreateView.as_view(), name="record_new"),
    # path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    # path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    # path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
]
