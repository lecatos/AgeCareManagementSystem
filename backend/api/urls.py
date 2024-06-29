from django.urls import path, re_path
from django.conf import settings
from .views import index
from user.views import *
from client.views import *
from inventory.views import *
from service.views import *



urlpatterns = [
    path("user/list", list_user),
    path("user/logout", logout_view),
    path("user/register", register_user, name="register"),
    path("user/login", login_view),
    path("user/whoami", whoami),
    path("user/<int:id>/update", update_user),
    path("client/list", list_client),
    path("client/add", create_client),
    path("client/<int:id>/", get_client),
    path("client/<int:id>/update", update_client),
    path("client/<int:id>/allergy/list", get_allergy),
    path("client/<int:id>/allergy/add", add_allergy),
    path("client/<int:id>/allergy/remove", remove_allergy),
    path("client/<int:id>/medhist/list", get_medhist),
    path("client/<int:id>/medhist/add", add_medhist),
    path("inventory/add", add_inv),
    path("inventory/<str:item_name>/remove", remove_inv),
    path("inventory/<str:item_name>/update", update_inv),
    path("inventory/list", list_inv),
    path("service/list", list_service),
    path("service/add", add_service),
    path("service/remove", remove_service),
    path("service/update", update_service),
    re_path("^.*$", index),
]
