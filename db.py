# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppCachestoreproducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    cache_json = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    user = models.ForeignKey('AppUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_cachestoreproducts'


class AppCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    cart_id = models.UUIDField()
    products_json = models.JSONField()
    products_total_price = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    list = models.ForeignKey('AppMylist', models.DO_NOTHING, blank=True, null=True)
    store = models.ForeignKey('AppStores', models.DO_NOTHING)
    user = models.ForeignKey('AppUsers', models.DO_NOTHING)
    is_cart_outdated = models.BooleanField()
    preloaded = models.ForeignKey('AppPreloadedlist', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_cart'


class AppCountry(models.Model):
    name = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_country'


class AppDepartments(models.Model):
    name = models.CharField(max_length=256)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_departments'


class AppDistrict(models.Model):
    name = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    state = models.ForeignKey('AppState', models.DO_NOTHING)
    district_code = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'app_district'


class AppMylist(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    user = models.ForeignKey('AppUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_mylist'


class AppMylistproduct(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    my_list = models.ForeignKey(AppMylist, models.DO_NOTHING)
    product = models.ForeignKey('AppProducts', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_mylistproduct'


class AppNeighborhoodscolonias(models.Model):
    name = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    district = models.ForeignKey(AppDistrict, models.DO_NOTHING)
    state = models.ForeignKey('AppState', models.DO_NOTHING)
    neighborhood_code = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'app_neighborhoodscolonias'


class AppPreloadedlist(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_preloadedlist'


class AppPreloadedlistproduct(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    preloaded_list = models.ForeignKey(AppPreloadedlist, models.DO_NOTHING)
    product = models.ForeignKey('AppProducts', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_preloadedlistproduct'


class AppProducts(models.Model):
    brand = models.CharField(max_length=256)
    generic_names = models.JSONField()
    measure = models.CharField(max_length=256)
    multi_measure = models.BooleanField()
    product_name = models.CharField(max_length=256)
    product_image = models.TextField(blank=True, null=True)
    quantity = models.FloatField()
    site = models.CharField(max_length=256)
    sku = models.CharField(max_length=256)
    unit = models.CharField(max_length=50)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    department = models.ForeignKey(AppDepartments, models.DO_NOTHING)
    product_code = models.CharField(max_length=256)
    genericname_general = models.CharField(max_length=256)
    measure_per_piece = models.CharField(max_length=256)
    pieces_per_kg = models.IntegerField(blank=True, null=True)
    quantity_per_piece = models.IntegerField(blank=True, null=True)
    unit_per_piece = models.CharField(max_length=256)
    upload_image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_products'


class AppSocialuserprovider(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider_type = models.CharField(max_length=256, blank=True, null=True)
    provider_json = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    user = models.ForeignKey('AppUsers', models.DO_NOTHING)
    jwt_token = models.CharField(max_length=4096, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_socialuserprovider'


class AppState(models.Model):
    name = models.CharField(max_length=250)
    state_no = models.CharField(max_length=250)
    state_code = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country = models.ForeignKey(AppCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_state'


class AppStoregroups(models.Model):
    name = models.CharField(max_length=256)
    logo = models.CharField(max_length=256)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_storegroups'


class AppStoreproducts(models.Model):
    is_exist = models.BooleanField()
    new_measure_info = models.JSONField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    product = models.ForeignKey(AppProducts, models.DO_NOTHING)
    store = models.ForeignKey('AppStores', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_storeproducts'


class AppStores(models.Model):
    store_address = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=256)
    longitude = models.CharField(max_length=256)
    store_logo = models.CharField(max_length=256)
    store_name = models.CharField(max_length=256)
    store_zipcode = models.CharField(max_length=256)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    store_group = models.ForeignKey(AppStoregroups, models.DO_NOTHING)
    store_code = models.CharField(max_length=256)
    store_location = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_stores'


class AppUploadedfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.CharField(max_length=100, blank=True, null=True)
    is_uploaded = models.BooleanField()
    is_imported = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'app_uploadedfile'


class AppUploadreceiptaction(models.Model):
    image = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    amount_paid = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    my_list = models.ForeignKey(AppMylist, models.DO_NOTHING, blank=True, null=True)
    store = models.ForeignKey(AppStores, models.DO_NOTHING)
    preloaded_list = models.ForeignKey(AppPreloadedlist, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('AppUsers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_uploadreceiptaction'


class AppUserfavouritestore(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    store = models.ForeignKey(AppStores, models.DO_NOTHING)
    user = models.ForeignKey('AppUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_userfavouritestore'


class AppUsers(models.Model):
    user_email = models.CharField(max_length=256)
    user_password = models.CharField(max_length=250)
    user_phone = models.CharField(max_length=16)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    user_type = models.IntegerField()
    is_login = models.BooleanField()
    is_email_sent = models.BooleanField()
    is_email_verified = models.BooleanField()
    otp = models.CharField(max_length=6, blank=True, null=True)
    display_name = models.CharField(max_length=200, blank=True, null=True)
    last_signed_in_at = models.DateTimeField(blank=True, null=True)
    provider_info = models.JSONField(blank=True, null=True)
    is_phone_verified = models.BooleanField()
    is_fresh_login = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'app_users'


class AppUsersprofile(models.Model):
    user_birthdate = models.DateField(blank=True, null=True)
    user_gender = models.CharField(max_length=200, blank=True, null=True)
    user_address = models.CharField(max_length=300, blank=True, null=True)
    user_children = models.CharField(max_length=200, blank=True, null=True)
    user_marital_status = models.CharField(max_length=200, blank=True, null=True)
    user_family_members = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_first_name = models.CharField(max_length=200, blank=True, null=True)
    user_last_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField()
    user_street = models.CharField(max_length=200, blank=True, null=True)
    user_zipcode = models.CharField(max_length=200, blank=True, null=True)
    user_district = models.ForeignKey(AppDistrict, models.DO_NOTHING)
    user_state = models.ForeignKey(AppState, models.DO_NOTHING)
    user_neighborhood = models.ForeignKey(AppNeighborhoodscolonias, models.DO_NOTHING)
    user_image = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AppUsers, models.DO_NOTHING)
    user_country = models.ForeignKey(AppCountry, models.DO_NOTHING)
    latitude = models.CharField(max_length=256, blank=True, null=True)
    longitude = models.CharField(max_length=256, blank=True, null=True)
    interior = models.CharField(max_length=256, blank=True, null=True)
    user_street_no = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_usersprofile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
