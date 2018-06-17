from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Order, OrderStatus

class OrderStatusInline(admin.TabularInline):
	model = OrderStatus
	extra = 0

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
	list_per_page = 40
	search_fields = ['order_id_number', 'facebook', 'phone']
	inlines = [OrderStatusInline]
	list_display = (
		# 'id',
		'order_id_number',
		'product',
		'name',
		'bank',
		'last_5_digits',
		'phone',
		'email',
		'post_method',
		'store_name',
		'store_No',
		'address',
		'facebook',
		'notes',
		'is_agree',
		'submit_time',)

@admin.register(OrderStatus)
class OrderStatusAdmin(ImportExportModelAdmin):
	list_per_page = 10
	search_fields = ['facebook']
	list_display = (
		# 'id',
		'orderID',
		'facebook',
		'product',
		'bank',
		'last_5_digits',
		'phone',
		'PaymentNotice',
		'PaymentReceived',
		'Ordered',
		'OrderReceivedUSA',
		'ShippingFee',
		'PackageDeliveredTW',
		'Sent',
		'TraceNo',)
	list_filter = (
		'PaymentNotice',
		'PaymentReceived',
		'Ordered',
		'OrderReceivedUSA',
		'ShippingFee',
		'PackageDeliveredTW',
		'Sent',)

