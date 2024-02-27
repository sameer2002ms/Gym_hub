from django.contrib import admin

# Register your models here.

from . import models

class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')
admin.site.register(models.Banner, BannerAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(models.Service, ServiceAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(models.Pages, PageAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('ques',)
admin.site.register(models.FAQ, FAQAdmin)


class ENQAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','details','send_time')
admin.site.register(models.Enquiry, ENQAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title','img')
admin.site.register(models.Gallery, GalleryAdmin)


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text','img')
admin.site.register(models.GalleryImages, GalleryImageAdmin)


class SubPlanAdmin(admin.ModelAdmin):
    list_editable = ('max_member',)
    list_display = ('title','price', 'max_member')
admin.site.register(models.SubPlan, SubPlanAdmin)


class SubPlanFeatureAdmin(admin.ModelAdmin):
    list_display = ('title','subplan')
admin.site.register(models.SubPlanFeature, SubPlanFeatureAdmin)


class planDiscountAdmin(admin.ModelAdmin):
    list_display = ('subplan', 'total_month','total_discount')
admin.site.register(models.PlanDiscount, planDiscountAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user','image_tag','mobile')
admin.site.register(models.Subscriber, SubscriberAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user','plan','price')
admin.site.register(models.Subscription, SubscriptionAdmin)
