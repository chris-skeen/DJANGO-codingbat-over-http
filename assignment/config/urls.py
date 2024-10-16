from django.contrib import admin
from django.urls import path
from app.views import near_hundred_view, string_splosion_view, cat_dog

urlpatterns = [
    path("near-hundred/<int:n>", near_hundred_view),
    path("string-splosion/<str:word>", string_splosion_view),
    path("cat-dog/",cat_dog),
    path("admin/", admin.site.urls),
]
