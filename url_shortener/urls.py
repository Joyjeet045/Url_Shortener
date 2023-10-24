from django.urls import path
from . import views

urlpatterns = [
  path('shorten/', views.shorten_url, name='shorten_url'),
  path('',views.test_view,name="home-page"),
  path('shortened_urls/', views.display_shortened_urls, name='display_shortened_urls'),
  path('my_shorturl/<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
  path('update_click_count/<str:short_code>/', views.update_click_count, name='update_click_count'),
]