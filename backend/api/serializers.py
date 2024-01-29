from rest_framework import serializers

#use for bottom part serialize 
class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk',
        read_only = True
    )
    title = serializers.CharField(read_only = True)

# foreign key serializer, serializing user model as what we want to see
class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
    id = serializers.IntegerField(read_only = True)
    # other_products = serializers.SerializerMethodField(read_only = True)

    # def get_other_products(self, obj):
    #     print(obj)
    #     user = obj
    #     qs = user.product_set.all()[:5]
    #     print(qs)
    #     return UserProductInlineSerializer(qs, many = True,context = self.context).data
    
