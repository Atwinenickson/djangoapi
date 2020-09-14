from django.urls import path
from .views import article_list, article_detail, ClubAPIView

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('club/', ClubAPIView.as_view(), name='club')
]
