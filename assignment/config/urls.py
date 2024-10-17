from django.contrib import admin
from django.urls import path
from app.views import near_hundred_view, string_splosion_view, cat_dog_view, lone_sum_view

urlpatterns = [
    path("near-hundred/<int:n>", near_hundred_view),
    path("string-splosion/<str:word>", string_splosion_view),
    path("cat-dog/<str:string>",cat_dog_view),
    path("lone-sum/<int:a>/<int:b>/<int:c>", lone_sum_view),
    path("admin/", admin.site.urls),
]
