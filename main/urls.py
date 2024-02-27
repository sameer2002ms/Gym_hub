from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('pagedetails/<int:id>', views.page_detail, name='pagedetails'),
    path('faqlist/', views.FAQ_List, name='faqlist'),
    path('enquiry/', views.Enquiry, name='enquiry'),
    path('gallery/', views.Gallery, name='gallery'),
    path('galleryimg/<int:id>', views.ImageGallery, name='galleryimg'),
    path('pricing/', views.Pricing, name='pricing'),
    path('checkout/<int:plan_id>', views.checkout, name='checkout'),
    path('checkoutsession/<int:plan_id>', views.checkout_session, name='checkoutsession'),
    path('pay_success', views.pay_success, name='pay_success'),
    path('pay_failure', views.pay_failure, name='pay_failure'),
    path("profile-detail/", views.profile_detail, name="profile-detail"),

]

