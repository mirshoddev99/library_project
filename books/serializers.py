from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author', 'isbn', 'price')

    def validate(self, data):
        # Validate - Method to validate of all fields of a serializer
        print('printing from serializers.py', data)
        title = data.get('title', None)
        if not title.isalpha():
            raise ValidationError(
                {'status': False, 'msg': 'you must enter string only'}
            )
        return data

    def validate_isbn(self, isbn):
        # Validate_field_name - Method to validate of one field of a serializer
        print('printing from serializers.py', isbn)
        if len(isbn) > 15:
            raise ValidationError({'status': False, 'error': 'the length of a isbn should be 15'})
        return isbn


# simple Serializer
class CashSerializer(serializers.Serializer):
    input = serializers.CharField(max_length=250)
    output = serializers.CharField(max_length=150)
