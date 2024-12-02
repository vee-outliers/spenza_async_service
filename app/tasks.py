import csv
import os
import logging
from django.conf import settings
from django.utils import timezone
from spenza_async_service.celery import app
from app.models import Stores, StoreProducts
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

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

def mail_user_with_attachment(user_email, file_name, is_products_updated, failed_reason, file):
    try:
        subject = "Spenza Products Update Status"
        html_message = render_to_string(
            "products_update.html",
            {
                "file_name" : file_name,
                "is_products_updated": is_products_updated,
                "failed_reason": failed_reason
            },
        )
        with open(file, "rb") as f:
            email = EmailMessage(
                subject=subject,
                body=html_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[user_email],
            )
            email.content_subtype = "html"
            email.attach(file, f.read(), "text/csv")
            email.send()
        logger.info(f"Email sent successfully to : {user_email}.")
        os.remove(file)
    except Exception as e:
        logger.info(f"Email failed to sent {user_email} : {e}")

def create_csv_file(products_not_in_store, store_id):
    products_not_in_store_filename = "products_not_updated.csv"
    with open(products_not_in_store_filename, "w") as csvfile:
        cr = csv.writer(csvfile, delimiter=",", lineterminator="\n")
        cr.writerow(["Product Code", "Store ID"])
        for instance in products_not_in_store:
            cr.writerow([instance, store_id])
    
    return products_not_in_store_filename

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
        products_not_in_store = []

        file_path = str(os.path.join(settings.BASE_DIR) + '/Products_in_stock - Loreto 75 (1).csv')

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
                        store_product_instance.updated_at = timezone.now()
                        products_to_update.append(store_product_instance)
                    else:
                        logger.info(
                            f"product with product_code {product_code} not found in {store_instance.store_name}."
                        )
                        products_not_in_store.append(product_code)
                else:
                    logger.info(
                        f"Error while updating price. Uploaded file store ID doesn't match with selected store ID."
                    )

            StoreProducts.objects.using("spenza").bulk_update(
                products_to_update, ["price", "is_exist", "updated_at"], batch_size=7500
            )
            logger.info("Updated product prices successfully.")

            logger.info(f"Preparing products not in store csv file.")
            products_not_in_store_filename = create_csv_file(products_not_in_store, store_id)
            logger.info(f"Prepared products not in store csv file.")

            logger.info(f"Produts update status emailing to : {user_email}.")
            mail_user_with_attachment(user_email, file_name, True, None, products_not_in_store_filename)

    except Exception as e:
        logger.info(f"Some Error Occured : {e}")
        logger.info(f"Produts update failed status emailing to : {user_email}.")
        mail_user(user_email, file_name, False, e)
