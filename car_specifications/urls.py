from django.urls import path
from .views import car_views
from .views import brand_views

urlpatterns = [
    path('', view = car_views.index),
    path('create/', view=car_views.create),
    path('brand/', view = brand_views.index),
    path('<int:id>/', view = car_views.getById),
    path('<int:id>/delete/', view= car_views.delete),
    path('<int:id>/brand-delete/', view = brand_views.delete),
    path('<int:id>/update/', view= car_views.update)
]