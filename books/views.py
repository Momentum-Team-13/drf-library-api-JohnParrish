# from django.shortcuts import render
from rest_framework import generics, permissions
from books.models import Book, Note, Tracking
from .serializers import BookSerializer, TrackedSerializer, NoteSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TrackedBookListView(generics.ListCreateAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackedSerializer


class DeleteBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateNoteView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
