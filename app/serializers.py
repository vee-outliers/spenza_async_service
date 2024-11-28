from rest_framework import serializers

class UpdateProductsSerializer(serializers.Serializer):
    file_id = serializers.IntegerField(required=True)
    store_id = serializers.IntegerField(required=True)
    user_email = serializers.CharField(required=True)