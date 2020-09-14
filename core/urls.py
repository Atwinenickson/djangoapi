from django.urls import path
from .views import article_list, article_detail, ClubAPIView, ClubDetails, GenericAPIView

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('club/', ClubAPIView.as_view(), name='club'),
    path('clubOne/', ClubDetails.as_view(), name='clubone'),
    path('generic/club/<int:id>/', GenericAPIView.as_view(), name='genericclub')
]
