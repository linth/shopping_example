from django import forms
from .models import Order, OrderStatus

import buying.models

POST_METHOD = (
        ("7-11店到店", "7-11店到店"),
        ("郵局", "郵局"),)

BANK = (
        ("郵局", "郵局"),
        ("台灣銀行", "台灣銀行"),
        ("彰化銀行", "彰化銀行"),)
        # ("兆豐商銀", "兆豐商銀"),

class OrderForm(forms.ModelForm):
# class OrderForm(forms.Form):
    product = forms.CharField(label=u'購買商品*',
                            required=True,
                            help_text='<font size="2" color="blue">只要填上 品牌+商品+尺寸或顏色+件數 (例如: MK手機包深藍色1個)</font>',
                            error_messages={'required': u'此項目不能空白'},
                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'輸入商品，並盡可能讓我知道商品!',}))
    name = forms.CharField(label=u'收件人姓名*',
                            required=True,
                            help_text='',
                            error_messages={'required': u'此項目不能空白'},
                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'輸入購買人姓名!'}))
    phone = forms.CharField(label=u'手機號碼*',
                            required=True,
                            help_text='<font size="2" color="blue">格式按照09xxxxxxxx，不要加任何符號</font>',
                            # error_messages={"blank": "此項目不能空白",},
                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'輸入購買人姓名!',}))
    email = forms.CharField(label=u'Email*',
                            required=True,
                            help_text='<font size="2" color="blue">請使用常用的e-mail!</font>',
                            # error_messages={"blank": "此項目不能空白",},
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '輸入e-mail'}))
    post_method = forms.ChoiceField(label=u'選擇寄件方式',
                            choices=POST_METHOD,
                            required=True,
                            widget=forms.Select(attrs={'class': 'form-control', }))
    store_name = forms.CharField(label=u'7-11店到店 - 門市店名',
                            required=False,
                            help_text='<font size="2" color="blue">(選擇店到店才填) 選擇您最方便取件的分店, <a href="http://emap.pcsc.com.tw/emap.aspx" target="_blank">(7-11店名查詢)</font></a>',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '輸入7-11門市店名'}))
    store_id = forms.CharField(label=u'7-11店到店 - 門市店號',
                            required=False,
                            help_text='<font size="2" color="blue">(選擇店到店才填)</font>',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '輸入7-11店號'}))
    address = forms.CharField(label=u'郵局 - 郵遞區號 + 收件地址',
                            required=False,
                            help_text='<font size="2" color="blue">(選擇郵局才填), <a href="http://www.post.gov.tw/post/internet/SearchZone/index.jsp?ID=130107" target="_blank">(郵局: 3+2郵遞區號查詢)</a></font>',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '輸入寄件地址'}))
    facebook = forms.CharField(label=u'Facebook名稱/LINE*',
                            required=True,
                            help_text='<font size="2" color="blue">請填寫跟Erin聯絡方式的使用名稱</font>',
                            # error_messages={"blank": "此項目不能空白",},
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '輸入Facebook名稱'}))
    bank = forms.ChoiceField(label=u'匯款單位*',
                            required=True,
                            help_text='<font size="2" color="blue">選擇您要匯入的金融單位</font>',
                            choices=BANK,
                            # error_messages={"blank": "此項目不能空白",},
                            widget=forms.Select(attrs={'class': 'form-control', 'placeholder': '輸入匯款單位',}))
    last_5_digits = forms.CharField(label=u'匯款帳號後5碼*',
                            required=True,
                            help_text='<font size="2" color="blue">轉出帳號後5碼</font>',
                            # error_messages={"blank": "此項目不能空白",},
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '輸入匯款帳號後5碼'}))
    notes = forms.CharField(label=u'備註',
                            required=False,
                            help_text='<font size="2" color="blue">要跟Erin講的悄悄話，如果購買Coach商品需禮盒，請備註 (禮盒免費、禮袋則需酌收台幣50元)。</font>',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '輸入需要提醒的注意事項!!!'}))
    is_agree = forms.BooleanField(label=u'是*',
                            required=True,
                            help_text='<font size="2" color="blue">是否詳讀 <a href="http://shoppingbag2015.wixsite.com/masonry-layout-1/-----um3se" target="_blank">瞎拼包代購注意事項</a></font>',
                            # error_messages={"blank": "此項目不能空白",},
                            widget=forms.CheckboxInput(attrs={'class': 'big-checkbox',}))
    order_id_number = forms.CharField(label=u'訂單編號',
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly', 'value': buying.models.generate_order_id_number()}))
    class Meta:
        model = Order
        fields = (
			'id',
			'product',
			'name',
			'phone',
			'email',
			'post_method',
			'store_name',
			'store_id',
			'address',
			'facebook',
			'bank',
			'last_5_digits',
			'notes',
			'is_agree',
            'order_id_number',)

    # def clean(self):
    #     product = self.cleaned_data.get('product')
    #     name = self.cleaned_data.get('name')
    #     phone = self.cleaned_data.get('phone')
    #     email = self.cleaned_data.get('email')
    #     facebook = self.cleaned_data.get('facebook')
    #     bank = self.cleaned_data.get('bank')
    #     last_5_digits = self.cleaned_data.get('last_5_digits')
    #     is_agree = self.cleaned_data.get('is_agree')

    #     if product or name or phone or email or facebook or bank or last_5_digits or is_agree:



class OrderStatusForm(forms.ModelForm):
    orderID = forms.CharField(label=u'訂購號碼',
                                    required=True,
                                    help_text='<font size="2" color="blue">請輸入訂購號碼</font>',
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'輸入訂購編號!',}))
    phone = forms.CharField(label=u'手機號碼',
                                    required=True,
                                    help_text='<font size="2" color="blue">請填入填單時使用的手機號碼</font>',
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'輸入電話!',}))
    PaymentNotice = forms.BooleanField(label=u'',
                                    required=True,
                                    help_text='匯款後請勾選，Erin將幫您確認匯款',
                                    widget=forms.CheckboxInput(attrs={'class': ''}))

    class Meta:
        model = OrderStatus
        fields = (
			'orderID',
			'phone',
			'PaymentNotice',)

class OrderSecondCheckForm(forms.ModelForm):
	orderID = forms.CharField(label=u'訂購號碼',
                                    required=True,
                                    help_text='<font size="2" color="blue">請輸入訂購號碼</font>',
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'輸入訂購編號!',}))
	phone = forms.CharField(label=u'手機號碼',
                                    required=True,
                                    help_text='<font size="2" color="blue">請填入填單時使用的手機號碼</font>',
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'輸入電話!',}))
	ShippingFee = forms.BooleanField(label=u'',
                                    required=True,
                                    help_text='第二次匯款後請勾選，Erin將幫您確認匯款',
                                    widget=forms.CheckboxInput(attrs={'class': '',}))

	class Meta:
		model = OrderStatus
		fields = (
			'orderID',
			'phone',
			'ShippingFee',)

