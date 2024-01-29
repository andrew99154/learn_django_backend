from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, unique_product_title
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source = 'user', read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    my_discount = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk'
    )
    title = serializers.CharField(validators = [validate_title, unique_product_title])
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError("This title has already exists.")
    #     return value

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs = {'pk': obj.pk}, request = request)
    
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
    

