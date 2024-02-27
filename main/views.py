from django.shortcuts import render, redirect
from django.template import *
from . import models 
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import stripe


# Create your views here.

def home(request):
    banners = models.Banner.objects.all()
    services = models.Service.objects.all()
    gimg = models.GalleryImages.objects.all().order_by('-id')[:9]
    pages = models.Pages.objects.all()
    
    return render(request, 'home.html', {"banners": banners, "services" : services, 'gimg' : gimg, 'pagess' : pages, 'page_name' : 'Home Page'})

def page_detail(request, id):
    page = models.Pages.objects.get(id=id)

    return render(request, 'page.html', {"pages" : page,'page_name' : 'Page Details'})

def FAQ_List(request):
    questions = models.FAQ.objects.all()
    return render(request, 'faq.html', {"questions" : questions,'page_name' : 'FAQ List Page'})


def Enquiry(request):
    msg = ''
    if request.method=='POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
           form.save()
           msg = 'Congrats! Your Query has been sent' 
    form = forms.EnquiryForm
    enquiry = models.Enquiry.objects.all()
    return render(request, 'enquiry.html', {"form" : form, 'msg' : msg,'page_name' : 'Enquiry Page'})

def Gallery(request):
    gallerys = models.Gallery.objects.all().order_by('id')
    return render(request, 'Gallery.html', {"gallerys": gallerys, 'page_name' : 'Gallery Page'})


def ImageGallery(request,id):
    gallery = models.Gallery.objects.get(id=id)
    galleryimage = models.GalleryImages.objects.filter(gallery=gallery).order_by('-id')
    return render(request, 'galleryimg.html', {"galleryimage": galleryimage,'gallery' : gallery,'page_name' : 'Gallery Images Page'})


def Pricing(request):
    pricing = models.SubPlan.objects.all().order_by('price')
    dfeatures = models.SubPlanFeature.objects.distinct('title')
    return render(request, 'pricing.html', {"plans" : pricing, 'dfeatures' : dfeatures, 'page_name' : 'Pricing Page'})


def checkout(request,plan_id):
    plandetail = models.SubPlan.objects.get(id=plan_id)
    return render(request, 'checkout.html', {'plans' : plandetail, 'page_name' : 'Check Out Page'})




stripe.api_key = 'YOUR API KEY' 

def checkout_session(request,plan_id):
    plan = models.SubPlan.objects.get(pk = plan_id)
    try:
     session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
         line_items=[
             {
                    'price_data': {
                        'currency' : 'inr',
                            'product_data' : {
                                'name' : plan.title
                            },
                            'unit_amount' : plan.price*100,
                        },
                        'quantity': 1,
                    }
             ],
                mode='payment',
                success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url= 'http://127.0.0.1:8000//pay_failure', 
                client_reference_id=plan_id
                    )
    
    except Exception as e:
        return str(e)

    
    return redirect(session.url, code=303)

# success
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
def pay_success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id = session.client_reference_id
    plan = models.SubPlan.objects.get(pk=plan_id)
    user = request.user
    models.Subscription.objects.create(
        plan = plan,
        user = user,
        price =plan.price,
    )
    
    msg_plain = render_to_string('email.txt')
    msg_html = render_to_string('orderemail.html')
    
    send_mail("Your booking has been Successful", msg_plain, settings.EMAIL_HOST_USER,
                              ['sameer2002.ms@gmail.com'], html_message = msg_html)
    
    
    return render(request,'success.html', {'page_name' : 'Payment Success Page'})

def pay_failure(request):
    return render(request, 'failure.html', {'page_name' : 'Payment Failure Page'})


def profile_detail(request):
    user = request.user
    first_user = request.user.id
    plans = models.Subscription.objects.filter(id = first_user)
    
    
    return render(request, 'profile_detail.html', {'user':user, "plan" : plans,'page_name' : 'Profile Detail Page'})

       