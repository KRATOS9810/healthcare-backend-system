from django.urls import path

from .views import (
    MappingListCreateView,
    MappingPatientDeleteView
)


urlpatterns = [
    path(
        '',
        MappingListCreateView.as_view(),
        name='mapping-list-create'
    ),

    path(
        '<int:pk>/',
        MappingPatientDeleteView.as_view(),
        name='mapping-detail'
    ),
]