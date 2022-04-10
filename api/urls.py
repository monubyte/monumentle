from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', AllImageAPIView.as_view(), name='list'),
    path('random/', RandomImageAPIView.as_view(), name='random'),
    re_path('random/(?P<params>([0-9]+\+)*[0-9])', RandomExcludeAPIView().as_view(), name='exclude'),
    path('<int:pk>/', ImageAPIView.as_view(), name='id'),
]