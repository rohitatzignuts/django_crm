from django.urls import path, include
from website import views

urlpatterns = [
    path("", views.homeView, name="home"),
    path("logout/", views.userLogout, name="logout"),
    path("register/", views.userRegister, name="register"),
    path("records/<int:pk>/", views.indiRecord, name="indi-record"),
    path("records/add/", views.addRecord, name="add-record"),
    path("records/delete/<int:pk>/", views.deleteRecord, name="delete-record"),
    path("records/edit/<int:pk>/", views.updateRecord, name="edit-record"),
]
