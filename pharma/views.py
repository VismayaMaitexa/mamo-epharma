from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from. import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    return render(request,'index.html')
def sample(request):
    return render(request,'sample.html')
def htmls(request):
    return HttpResponse('POOYI VAAA')
#login_page_admin
def abouts(request):
    return render(request,'about.html')
def admin(request):
    return render(request,'admin.html')
def buy(request):
    return render(request,'buy.html')
def user(request):
    return render(request,'user.html')
def contact(request):
    return render(request,'contanct.html')

#inside_admin_login_page
def product(request):
    return render(request,'product.html')
@login_required
def orders(request):
    orders =models.Address.objects.all()
    return render(request, 'order.html', {'orders': orders})
def users(request):
    return render(request,'in_user.html')
def feebback(request):
    feedbacks = models.Feedback.objects.all().order_by('-created_at') 
    return render(request,'feedbacks_admin.html', {'feedbacks': feedbacks})
def log_out(request):
    return render(request,'log.html')

#register and login of user
def register(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}

    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)

        if userForm.is_valid() and customerForm.is_valid():
           
            user = userForm.save(commit=False)
            user.set_password(user.password) 
            user.save()

          
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()

          
            my_customer_group, created = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group.user_set.add(user)
            messages.success(request, "Your account has been created successfully!")
            return HttpResponseRedirect('userlogin')

        else:
           
            messages.error(request, "Please correct the errors below.")

    return render(request, 'register.html', context=mydict)

def userlogin_view(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('user_dashh')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

#user_dashboard_register
@login_required 
def user_dashboard(request):
    try: 
        user_profile =models. UserProfile.objects.get(user=request.user) 
    except models.UserProfile.DoesNotExist: 
        user_profile = None 
        return render(request, 'user_dash.html', {'user_profile': user_profile})

#user_dashboard_purchase
def purchase_item(request):
   
    search_query = request.GET.get('search', '')  

   
    if search_query:
        products = models.Products.objects.filter(name__icontains=search_query)
    else:
       
        products = models.Products.objects.all()

  
    if not products:
      
        return render(request, 'purch_item.html', {
            'no_products_found': True,
            'search_query': search_query
        })

    return render(request, 'purch_item.html', {
        'products': products,
        'no_products_found': False,
        'search_query': search_query
    })
    
#user_dashboard order product
def order_user(request):
    if request.user.is_authenticated:
        orders = models.Address.objects.filter(user=request.user)
        
        context = {
            'orders': orders
        }
        return render(request, 'purch_order.html', context)
    else:
        return redirect('userlogin') 



#admin login 
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        if username == 'principal' and password == '12345':
            user = User.objects.filter(username=username).first()
            if not user:
                user = User.objects.create_user(username=username, password=password)

            login(request, user)
            return redirect('admin-home')
        else:
            print("Invalid username or password.")
            return render(request, 'admin.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'admin.html')

def adminhome_view(request):
    return render(request,'admindashboard.html')

#register and login of online delivery 
def online_register(request):
    userForm=forms.DeliveryUserForm()
    deliveryForm=forms.DeliveryForm()
    mydict={'userForm':userForm, 'deliveryForm':deliveryForm}
    if request.method=='POST':
        userForm=forms.DeliveryUserForm(request.POST)
        deliveryForm=forms.DeliveryForm(request.POST,request.FILES)
        if userForm.is_valid() and deliveryForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            delivery=deliveryForm.save(commit=False)
            delivery.user=user
            delivery.save()
            my_delivery_group=Group.objects.get_or_create(name='DELIVERY BOY')
            my_delivery_group[0].user_set.add(user)
        return HttpResponseRedirect('buys_logins')
    return render(request,'register_buys.html',context=mydict)

#login after the admin approval
def online_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            try:
              
                delivery_boy = models.Delivery_boy.objects.get(user=user)
                
                if delivery_boy.approved:
                   
                    return redirect('delivery boy dashboard')  
                else:
                    
                    return redirect('delivery_boy')  
            except models.Delivery_boy.DoesNotExist:
                
                messages.error(request, 'User not found as a delivery boy.')
                return redirect('online_registers')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login_buys.html') 

#login_of online delivery boy
def delivery_dash(request):
    return render(request,'dash_of_delivery.html')

#admin_user_container_box
def inuser_add(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            # Save the user details
            user = userForm.save(commit=False)
            user.set_password(user.password)  
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user 
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
            
            return redirect('view-customer') 
    return render(request,'add_inuser.html', {'userForm': userForm, 'customerForm': customerForm})
def user_in_views(request):
    return render(request,'dash_inviews.html')

#admin_user_ delete customer
def delete_customer_view(request,pk):
    customer=models.Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return redirect('view-customer')
#admin_user_ view customer
def view_customer_view(request):
    customers=models.Customer.objects.all()
    return render(request,'dash_inviews.html',{'customers':customers})
#admin_user update customer
def update_customer_view(request,pk):
    customer=models.Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
        return redirect('view-customer')
    return render(request,'admin_update_customer.html',context=mydict)   
 
#PRODUCTSSS
#admin_product_adding product
def product_adding(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()  
            return redirect('product-views')
    else:
        form =forms.ProductForm()
    return render(request,'product_add_admin.html', {'form': form})

#admin_product_viewing product
def product_viewing(request):
    products=models.Products.objects.all()
    return render(request,'product_view_admin.html', {'products': products})
#admin_product_viewing delete
def product_delete(request,pk):
    product=models.Products.objects.get(id=pk)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect('product-views')


#admin_product_viewing update
def product_update(request,pk):
    product = models.Products.objects.get(id=pk)
    productForm = forms.ProductForm(request.FILES, instance=product) 
    if request.method == 'POST':
        productForm = forms.ProductForm(request.POST, request.FILES, instance=product)
        if productForm.is_valid():  
            productForm.save()
            return redirect('product-views')
    return render(request, 'product_update_admin.html', {'productForm': productForm}) 

#add_to_cart_in user dash ADD TO CART FUNCTIONS
def add_to_cart(request,pk):
    products=models.Products.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids=request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=1    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('userlogin'))
    response=render(request,'purch_item.html',{'products':products,'product_count_in_cart':product_count_in_cart})
    if 'product_ids' in request.COOKIES:
        product_ids=request.COOKIES['product_ids']
        if product_ids == "":
            product_ids= str(pk)
        else:
           product_ids=product_ids + "|" + str(pk)
        response.set_cookie('product_ids',product_ids)
    else:
        response.set_cookie('product_ids',pk)
    product=models.Products.objects.get(id=pk)
    messages.info(request,product.name + 'Added to cart successfully..')
    return response  
#viewing the cart with storage  
def cart_view(request):
    products = None
    total = 0
    product_count_in_cart = 0


    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))  
        if product_ids != "":
            product_id_in_cart = product_ids.split('|')
            
            products = models.Products.objects.filter(id__in=product_id_in_cart)
            

            for p in products:
                
                quantity = request.COOKIES.get(f'quantity_{p.id}', 1)  
                total += p.price * int(quantity)

    # Return the response with the cart data (products, count, total)
    return render(request, 'addto_cart_user.html', {
        'products': products,
        'product_count_in_cart': product_count_in_cart,
        'total': total
    })
    
#proced_to chehckout user button
@login_required
def proced_user_checkout(request):
    if request.method == 'POST':
        form = forms.AddressForm(request.POST)
        product_ids_cookie = request.COOKIES.get('product_ids', '')
        if product_ids_cookie:
            product_ids_list = product_ids_cookie.split('|')
        else:
            product_ids_list = []
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            order_id=f'BM-x{address.id}'
            address.tracking_number=order_id
            address.save()
            products=models.Products.objects.filter(id__in=product_ids_list)
            for item in products:
                address.products.add(item)
            return redirect('payments')  
    else:
        form = forms.AddressForm()

    return render(request, 'proced_to_checkout.html', {'form': form})

#remove from add from cart
def cart_deletee(request,pk):
    if 'product_ids' in request.COOKIES:
        product_ids=request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0 
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids=request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=models.Products.objects.all().filter(id__in=product_id_in_cart)
        for p in products:
            total=total+p.price
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i] 
        response=render(request,'addto_cart_user.html',{'products': products,
        'product_count_in_cart': product_count_in_cart,
        'total': total})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        return response                   


#confirm and payments
def confirm_payment(request):
    if request.method == 'POST':
        form =forms.PaymentForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('credits payment done ') 
    else:
        form =forms.PaymentForm()
    return render(request,'confirm_pay.html', {'form': form})  

#credit card page with card number/cv code
def credit_payment(request):
    return render(request,'payment_credit.html') 

#feedback in user side
def user_feedback(request):
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('thank you')  
    else:
        form =forms.FeedbackForm()
    return render(request,'feedback_user.html', {'form': form})

#thank u page after submit in user
def thanks(request):
    return render(request,'thanks_page.html')

#online boy at admin side 
def online_boy_admine(request):
    delivery_boys = models.Delivery_boy.objects.all
    return render(request, 'delivery_boys.html', {'delivery_boys': delivery_boys})

#delivery approval by admin
def approve_delivery_boy(request, id):
    boy = models.Delivery_boy.objects.get(id=id)
    boy.approved = True
    boy.save()
    return redirect('admin_online')

#delivery boy reject by admiin
def reject_delivery_boy(request, id):
    boy = models.Delivery_boy.objects.get(id=id)
    boy.delete()
    return redirect('admin_online')

#online dashboard for delivery boys
def delivery_dashboard(request):
    orders = models.Address.objects.filter(status__in=['PENDING', 'SHIPPED']).order_by('date')
    return render(request, 'delivery2_dashboard.html', {'orders': orders})


#online delivery boy dashboard_update the status 
def update_order_status(request, order_id):
    order = get_object_or_404(models.Address, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('delivery boy dashboard') 
    

#prescription adding in the purch item
from pharma.forms import PrescriptionForm
import easyocr
reader=easyocr.Reader(['en'])
def image(request):
    products = models.Products.objects.all()
    
    if request.method == 'POST':
        form = forms.PrescriptionForm(request.POST, request.FILES)
        
        if form.is_valid():
            file = request.FILES['file']
            image = file.read()
            result = reader.readtext(image)
            extracted_text = ' '.join([res[1] for res in result])
            extracted_text_words = extracted_text.split()
            
            data = [word for word in extracted_text_words if word.isupper() and len(word) >= 4]
            
            return render(request, 'prescription.html', {
                'extracted_text': data,
                'products': products
            })
    else:
        form = forms.PrescriptionForm()

    return render(request, 'prescription.html', {
        'form': form,
        'products': products
    })

#forgot password in user
def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('forgot_password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username not found!')
            return redirect('forgot_password')

        user.password = make_password(new_password)
        user.save()

        messages.success(request, 'Your password has been updated successfully!')
        return redirect('login')
    return render(request, 'forgot_password.html')


def chatbhot(request):
    return render(request,'chatbots.html')