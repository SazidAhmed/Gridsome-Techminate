from django.urls import path, include
                  
from apis import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
]