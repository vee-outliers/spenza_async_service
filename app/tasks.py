import csv
import logging
import datetime
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from spenza_async_service.celery import app
from app.models import Stores, StoreProducts
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)

def mail_user(user_email, file_name, is_products_updated, failed_reason):
    subject = "Spenza Products Update Status"
    html_message = render_to_string(
        "products_update.html",
        {
            "file_name" : file_name,
            "is_products_updated": is_products_updated,
            "failed_reason": failed_reason
        },
    )
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    try:
        send_mail(subject, None, email_from, recipient_list, html_message=html_message)
        logger.info(f"Email sent successfully to : {user_email}.")
    except Exception as e:
        logger.info(f"Email failed to sent {user_email} : {e}")


@app.task
def update_products_async(file_id, store_id, user_email):
    logger.info("Started updating product prices.")

    file_name = "Loreto.csv"

    try:
        store_instance = Stores.objects.using("spenza").get(id=store_id, status=0)
        store_product_instances = StoreProducts.objects.using("spenza").select_related(
            "store", "product"
        ).filter(store_id=store_instance)

        store_product_dict = {sp.product.product_code: sp for sp in store_product_instances}

        products_to_update = []

        file_path = "/home/vee/Outliers/django_projects/spenza_async_service/Products_in_stock - Loreto 75 (1).csv"

        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                product_code = row["Product Code"]
                csv_store_id = row["Store ID"]
                price = row["Price"] if row["Price"] else None
                is_exist = True if row["Is Exist"] == 'TRUE' else False 

                if int(csv_store_id) == int(store_id):
                    store_product_instance = store_product_dict.get(product_code)

                    if store_product_instance:
                        store_product_instance.price = price
                        store_product_instance.is_exist = is_exist
                        store_product_instance.updated_at = datetime.datetime.now(
                            tz=timezone.utc
                        )
                        products_to_update.append(store_product_instance)
                    else:
                        logger.info(
                            f"product with product_code {product_code} not found in {store_instance.store_name}."
                        )
                else:
                    logger.info(
                        f"Error while updating price. Uploaded file store ID doesn't match with selected store ID."
                    )

            StoreProducts.objects.using("spenza").bulk_update(
                products_to_update, ["price", "is_exist", "updated_at"], batch_size=7500
            )
            logger.info("Updated product prices successfully.")

            logger.info(f"Produts update status emailing to : {user_email}.")
            mail_user(user_email, file_name, True, None)

    except Exception as e:
        logger.info(f"Some Error Occured : {e}")
        logger.info(f"Produts update failed status emailing to : {user_email}.")
        mail_user(user_email, file_name, True, e)
