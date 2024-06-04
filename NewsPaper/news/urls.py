from django.urls import path
from .views import PostList


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>/', PostList.as_view(), name='post')
]
