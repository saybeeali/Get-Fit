from django.urls import path
from . import views



urlpatterns = [
    path('',views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name="about"),
    path('workouts/', views.BodypartList.as_view(), name="workout_list"),
    path('workout/new/', views.BodypartCreate.as_view(), name='workout_create'),
    path('workouts/<int:pk>/',views.BodypartDetail.as_view(), name='workout_detail'),
    path('workout/<int:pk>/update', views.BodypartUpdate.as_view(), name='workout_update'),
    path('workout/<int:pk>/delete', views.BodypartDelete.as_view(), name='workout_delete'),
    path('routines/<int:pk>/exercise/<int:exercise_pk>/', views.RoutineExerciseAssoc.as_view(), name='routine_exercise_assoc'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),



]