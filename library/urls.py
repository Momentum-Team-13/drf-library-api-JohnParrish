"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views as books_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/books/', books_views.BookListView.as_view(), name='book_list'),
    path('api/books/<int:pk>/', books_views.BookDetailView.as_view()),
    path('api/tracked/books/', books_views.TrackedBookListView.as_view()),
    path('api/<int:pk>/delete/', books_views.DeleteBookView.as_view()),
    path('api/notes/', books_views.CreateNoteView.as_view()),
]
