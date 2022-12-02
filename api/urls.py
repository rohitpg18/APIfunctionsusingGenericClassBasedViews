from django.urls import path
from api.views import *

urlpatterns = [
    path("", SnippetList.as_view()),
    path("<int:pk>/",SnippetDetail.as_view()),
    # path('', StudentView.as_view()),
    # path('api/<int:id>', StudentUd.as_view()),
    # path('update/<int:id>/',update_data),
    # path('delete/<int:id>/', delete),
]
