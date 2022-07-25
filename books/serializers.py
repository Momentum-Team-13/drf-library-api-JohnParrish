from rest_framework import serializers
from books.models import Note, Tracking, User, Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username')


class BookSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'user', 'author', 'title', 'date', 'genre', 'featured')


class TrackedSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    book = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Tracking
        fields = ('user', 'book', 'status')


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('__all__')
