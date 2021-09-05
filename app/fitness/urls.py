from django.urls import path

from app.fitness.views import ActivityCreate, agregate_statictic

urlpatterns = [
    path('', ActivityCreate.as_view()),
    path('<int:gap>/', agregate_statictic),
]
