from django.urls import path

# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('profile/<str:pk>/', views.userProfile, name="profile"),
    path('updateprofile', views.updateprofile, name="updateprofile"),
    # path('delete_user/<str:pk>', views.deleteUser, name='delete_user'),
]