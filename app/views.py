from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import app.serializers as app_serializers
import app.tasks as app_tasks
import logging
from app.models import StoreProducts
import datetime

# Create your views here.

logger = logging.getLogger(__name__)


class ProductsUpdateAPIView(APIView):

    def post(self, request):
        serializer_instance = app_serializers.UpdateProductsSerializer(
            data=request.data
        )

        if not serializer_instance.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=serializer_instance.errors
            )

        serialized_data = serializer_instance.validated_data

        store_products = StoreProducts.objects.using('spenza').filter(store_id=75)
        print("Length", len(store_products))
        updated_at = datetime.datetime(2024, 11, 26)
        store_products.update(updated_at=updated_at, price=None, is_exist=False)

        # app_tasks.update_products_async.delay(
        #     serialized_data.get("file_id"),
        #     serialized_data.get("store_id"),
        #     serialized_data.get("user_email"),
        # )

        return Response(
            status=status.HTTP_200_OK, data={"message": "Products Update Accepted."}
        )
