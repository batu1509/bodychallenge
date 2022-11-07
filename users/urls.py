from django.urls import path

# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('profile/<str:pk>/', views.userProfile, name="profile"),
    # path('delete_user/<str:pk>', views.deleteUser, name='delete_user'),
]