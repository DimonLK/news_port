from django.urls import path
from .views import *


urlpatterns = [
   path('', PostList.as_view(), name='post-list'),
   path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
   # path('<int:pk>/', PostForm.as_view(), name='post-form'),
   # path('<int:pk>/', PostCreate.as_view(), name='post-create'),
   # path('<int:pk>/', PostUpdate.as_view(), name='post-update')
]
