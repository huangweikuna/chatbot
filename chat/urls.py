from django.urls import path

from chat.views.hello import HelloView

urlpatterns = [
    path('hello', HelloView.as_view()),
]
