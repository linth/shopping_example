from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, OrderStatus
from .forms import OrderForm, OrderStatusForm, OrderSecondCheckForm
import buying.models
# from django.shortcuts import render_to_response

# using Google e-mail
# ToDo: the funcitionality of sending e-mail.

@login_required(login_url='/')
def usa(request):
	query = request.GET.get("q", None) # search with orderID.
	# query_facebook = request.GET.get("q_facebook", None) # search with fb.

	order_object = Order.objects.all()
	orderstatus_object = OrderStatus.objects.all() #.order_by('submit_time').reverse()

	if query is not None:
		if Order.objects.filter(order_id_number=query):
			order_object = Order.objects.filter(order_id_number=query)
			orderstatus_object = OrderStatus.objects.filter(orderID=order_object)
		else:
			order_object = Order.objects.all()
			orderstatus_object = OrderStatus.objects.all()

	template = 'buying/usa.html'
	content = {
		"list_order": order_object,
		"list_orderStatus": orderstatus_object,
	}
	return render(request, template, content)

# def order_status_update_view(request, id=None):
# 	obj = get_object_or_404(OrderStatus, id=id)
# 	# form = PostModelForm(request.POST or None, instance=obj)
# 	template = ''
# 	content = {}
# 	return render(request, template, content)

def home(request):
	template = 'buying/home.html'
	return render(request, template)

def search(request):
	order = None
	order_check = None
	template = "buying/search.html"
	content = {"list": None, "error": None,}
    # get the data of order_id_number.
	query = request.GET.get("q", None)
    # get the data of phone number.
	query_2 = request.GET.get("q2", None)

	if query and query_2 is not None:
		if request.method == 'GET':
			if Order.objects.filter(order_id_number=query, phone=query_2):
				order_object = Order.objects.get(order_id_number=query, phone=query_2)

				if OrderStatus.objects.filter(orderID=order_object, phone=query_2):
					orderstatus_object = OrderStatus.objects.filter(orderID=order_object, phone=query_2)

					template = "buying/search.html"
					content = {"list": orderstatus_object, "list_order": order_object,}
			else:
				template = "buying/failure_search.html"
				content = {"error": "尚未填過單"}
	return render(request, template, content)

def order_form(request):
	
	content = {'form': OrderForm(),}
	template = "buying/shoppingform.html"

	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			# if not request.POST.get('product')
			form.save()
			# provide the account of Bank based on user's selection.
			if request.POST.get('bank') == '郵局':
				remittance_information = '郵局帳號 xxx: xxxxxxx xxxxxxx'
			elif request.POST.get('bank') == '台灣銀行':
				remittance_information = '台灣銀行帳號 xxx: xxxxxxx xxxxxxx'
			else: # request.POST.get('bank') == '彰化銀行':
				remittance_information = '彰化銀行帳號 xxx: xxxxxxx xxxxxxx'
			# else:
				# emittance_information = '兆豐商銀 xxx: xxxxxxx xxxxxxx' # 兆豐商銀

			# fill it in by users and list information of the form.
			content = {
				"product": request.POST.get('product'),
				"name": request.POST.get('name'),
				'phone': request.POST.get('phone'),
				"email": request.POST.get('email'),
				"post_method": request.POST.get('post_method'),
				"store_name": request.POST.get('store_name'),
				"store_id": request.POST.get('store_id'),
				"address": request.POST.get('address'),
				"facebook": request.POST.get('facebook'),
				"bank": request.POST.get('bank'),
				"last_5_digits": request.POST.get('last_5_digits'),
				"notes": request.POST.get('notes'),
				"is_agree": request.POST.get('is_agree'),
				"order_number": request.POST.get('order_id_number'),
				"remittance_information": remittance_information,
			}
			# add a new object to the table of OrderStatus
			order_object = Order.objects.get(order_id_number=request.POST.get('order_id_number'))
			OrderStatus.objects.create(orderID=order_object, 
				facebook=request.POST.get('facebook'), 
				product=request.POST.get('product'), 
				bank=request.POST.get('bank'), 
				last_5_digits=request.POST.get('last_5_digits'),
				phone=request.POST.get('phone'), )

			template = "buying/success_shoppingform.html"
		# else:
			# form = OrderForm()
	form = OrderForm()
	return render(request, template, content)

def order_check(request):
	form = OrderStatusForm(request.POST)
	content = {'form': OrderStatusForm(), }
	template = 'buying/order_check.html'

	if request.method == 'POST':
		if Order.objects.filter(order_id_number=request.POST.get('orderID'), phone=request.POST.get('phone')):
			order_object = Order.objects.get(order_id_number=request.POST.get('orderID'), phone=request.POST.get('phone'))
			orderstatus_object = OrderStatus.objects.filter(orderID=order_object, phone=request.POST.get('phone'))
			orderstatus_object.update(PaymentNotice=True)

			template = 'buying/success_order_check.html'
			content = {
				"orderID": request.POST.get('orderID'),
				"phone": request.POST.get('phone'),
				"PaymentNotice": request.POST.get('PaymentNotice'), }
		else:
			template = 'buying/failure_order_check.html'
			content = { "form": OrderStatusForm(), "error": "查無此資料"}
	return render(request, template, content)

def order_second_check(request):
	form = OrderSecondCheckForm(request.POST)
	content = {'form': OrderSecondCheckForm(), }
	template = 'buying/order_second_check.html'

	if request.method == 'POST':
		if Order.objects.filter(order_id_number=request.POST.get('orderID'), phone=request.POST.get('phone')):
			order_object = Order.objects.get(order_id_number=request.POST.get('orderID'), phone=request.POST.get('phone'))

			if OrderStatus.objects.filter(orderID=order_object, phone=request.POST.get('phone'), PaymentNotice=True):
				orderstatus_object = OrderStatus.objects.filter(orderID=order_object, phone=request.POST.get('phone'), PaymentNotice=True)
				orderstatus_object.update(ShippingFee=True)

				template = 'buying/success_order_second_check.html'
				content = {
					"orderID": request.POST.get('orderID'),
					"phone": request.POST.get('phone'),
					"ShippingFee": request.POST.get('ShippingFee'),}
			else:
				template = 'buying/failure_order_second_check.html'
				content = {
					"form": OrderSecondCheckForm(),
					"error": '訂單編號/手機號碼有誤或您未有填單紀錄/未有繳款紀錄!',}
		else:
			template = 'buying/failure_order_second_check.html'
			content = {
			"form": OrderSecondCheckForm(),
			"error": '訂單編號/手機號碼有誤或您未有填單紀錄/未有繳款紀錄!',}
	return render(request, template, content)
