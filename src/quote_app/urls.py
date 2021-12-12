from django.urls import path

from quote_app import views

app_name = 'quote_app'

urlpatterns = [
    path('create-category', views.create_category, name='create_category'),
    path('get-categories', views.get_categories, name='get_categories'),
    path('get-category/<int:pk>', views.get_category, name='get_category'),
    path('update-category/<int:pk>', views.update_category, name='update_category'),
    path('delete-category/<int:pk>', views.delete_category, name='delete_category'),

    path('create-quote', views.create_quote, name='create_quote'),
    path('get-quotes', views.get_quotes, name='get_quotes'),
    path('get-quote/<int:pk>', views.get_quote, name='get_quote'),
    path('update-quote/<int:pk>', views.update_quote, name='update_quote'),
    path('delete-quote/<int:pk>', views.delete_quote, name='delete_quote'),
]