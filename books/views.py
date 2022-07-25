# from django.shortcuts import render
from rest_framework import generics
from books.models import Book, Tracking
from .serializers import BookSerializer, TrackedSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TrackedBookListView(generics.ListAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackedSerializer
