from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'injuries', views.InjuryViewSet)
router.register(r'symptoms', views.SymptomViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('injuries', views.injuries, name='injuries'),
]
