from django.urls import path
from . import views

app_name = 'chatbot_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_api, name='chat_api'),
    path('history/', views.conversation_history, name='history'),
]
