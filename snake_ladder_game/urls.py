"""
URL configuration for snake_ladder_game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('start/', views.start_game, name='start_game'),
    path('roll_dice/<int:game_id>/', views.roll_dice_view, name='roll_dice'),
    path('game_state/<int:game_id>/', views.get_game_state, name='get_game_state'),
]

