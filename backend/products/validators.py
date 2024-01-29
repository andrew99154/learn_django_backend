from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

def validate_title(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("'hello' is not allowed.")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')