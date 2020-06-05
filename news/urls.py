from django.urls import path
from . import views 
urlpatterns = [
    path('',views.Homeview.as_view(),name='home' ),
    path('<category>/',views.category_news,name='display-news' ), 
    path('export/news',views.export_news_csv,name='export-news' ), 

]