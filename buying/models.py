from django.db import models
import django.utils.timezone as timezone
import uuid
import datetime

global Order_number

def generate_order_id_number():
	global Order_number
    # generate first random varible.
	first_random_number = uuid.uuid4().hex[:6].upper()
    # generate second random varibale.
	y = int(datetime.datetime.now().strftime("%Y"))
	md = int(datetime.datetime.now().strftime("%m%d"))
	hm = int(datetime.datetime.now().strftime("%H%M"))
	second_random_number = str(y - md + hm)

    # you can create a new one whatever you want.
	Order_number = second_random_number + first_random_number
	return Order_number

class Order(models.Model):
    POST_METHOD = (("7-11店到店", "7-11店到店"), ("郵局", "郵局"),)
    BANK = (("郵局", "郵局"), ("台灣銀行", "台灣銀行"),  ("彰化銀行", "彰化銀行")) # ("兆豐商銀", "兆豐商銀"),

    product = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    submit_time = models.DateTimeField(default=timezone.now, null=True)
    email = models.CharField(max_length=50)
    post_method = models.CharField(choices=POST_METHOD, max_length=20) # default='7-11店到店',
    store_name = models.CharField(max_length=50, blank=True)
    store_No = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50)
    bank = models.CharField(choices=BANK, max_length=20) # default='郵局',
    last_5_digits = models.CharField(max_length=20)
    notes = models.CharField(max_length=100, blank=True)
    is_agree = models.BooleanField(max_length=2)
    # the number of order
    order_id_number = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return str(self.order_id_number)

class OrderStatus(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=50, blank=True)
    product = models.CharField(max_length=50, blank=True)
    bank = models.CharField(max_length=50, blank=True)
    last_5_digits = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    PaymentNotice = models.BooleanField(max_length=2, default='False', blank=True)
    PaymentReceived = models.BooleanField(max_length=2, default='False', blank=True)
    Ordered = models.BooleanField(max_length=2, default='False', blank=True)
    OrderReceivedUSA = models.BooleanField(max_length=2, default='False', blank=True)
    ShippingFee = models.BooleanField(max_length=2, default='False', blank=True)
    PackageDeliveredTW = models.BooleanField(max_length=2, default='False', blank=True)
    Sent = models.BooleanField(max_length=2, default='False', blank=True)
    TraceNo = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
    	return str(self.orderID.order_id_number)
