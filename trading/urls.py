from django.urls import path

from trading.apps import TradingConfig
# from habit.views import (
#     HabitListAPIView,
#     PublicHabitListAPIView,
#     HabitCreateAPIView,
#     HabitRetrieveAPIView,
#     HabitUpdateAPIView,
#     HabitDestroyAPIView
# )

app_name = TradingConfig.name

urlpatterns = [
    path('',
         HabitListAPIView.as_view(),
         name='habit_list'),
    path('public/',
         PublicHabitListAPIView.as_view(),
         name='public_habit_list'),
    path('create/',
         HabitCreateAPIView.as_view(),
         name='habit_create'),
    path('<int:pk>/',
         HabitRetrieveAPIView.as_view(),
         name='habit_detail'),
    path('<int:pk>/update/',
         HabitUpdateAPIView.as_view(),
         name='habit_update'),
    path('<int:pk>/delete/',
         HabitDestroyAPIView.as_view(),
         name='habit_delete'),
]
