from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsAPIView.as_view(), name="api_News"),
    path('create/', NewsAPICreate.as_view(), name="api_News_create"),
    path('<int:pk>/', NewsAPIRetrieve.as_view(), name="api_News_detail"),
    path('update/<int:pk>/', NewsAPIUpdate.as_view(), name="api_News_update"),
    path('delate/<int:pk>/', NewsAPIDestroy.as_view(), name="api_News_destroy"),
]
