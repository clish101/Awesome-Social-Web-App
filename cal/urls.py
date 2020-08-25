
from django.urls import path
from . import views
from .views import CalendarView, eventDeleteView, alleventsListView


urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('new/event/', views.event, name='event_new'),
    path('all/events/', alleventsListView.as_view(), name='all_events'),
    path('edit/event/<int:event_id>/', views.event, name='event_edit'),
    path('delete/event/<int:pk>/',
         eventDeleteView.as_view(), name='event_delete'),
]
