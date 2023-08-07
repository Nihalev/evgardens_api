from django.urls import path
from .views import PlantView

urlpatterns = [
    path('item/', PlantView.as_view()),
    path('item/<int:id>/', PlantView.as_view()),
]
