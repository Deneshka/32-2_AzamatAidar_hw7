from django.urls import path
from . import views

urlpatterns = [
    path('', views.WatchShopView.as_view(), name='watches'),
    path('watch_detail/<int:id>/', views.WatchShopDetailView.as_view(), name='watch_detail'),
    path('watch_detail/<int:id>/delete/', views.DeleteWatchShopView.as_view(), name='delete_watch'),
    path('watch_detail/<int:id>/update/', views.UpdateWatchShopView.as_view(), name='update_watch'),
    path('create_watch/', views.AddTvShowView.as_view(), name='create_watch'),
    path('search/', views.Search.as_view(), name='search'),


]