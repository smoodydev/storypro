from django.conf.urls import url
from .views import remove_profile, register

urlpatterns = [
    url(r'^removeprofile/', remove_profile, name="remove_profile"),
    url(r'^register/', register, name="register"),
]