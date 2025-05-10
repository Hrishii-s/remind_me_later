
from . import views
from django.urls import path

urlpatterns = [
     path('create_reminder/',views.create_reminder,name='create_reminder_api')
]
