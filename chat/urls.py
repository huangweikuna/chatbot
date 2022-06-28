from django.urls import path

from chat.views.event_listener_view import EventListenerView
from chat.views.hello import HelloView

urlpatterns = [
    path('hello', HelloView.as_view()),
    path('evnet', EventListenerView.as_view()),
    # path('liveness', EventLivenessView.as_view()),
]
