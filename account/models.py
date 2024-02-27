# from django.db import models
# from django.contrib.auth.models import User
# from base.models import BaseModel
# # from django.db.models.signals import post_save
# # from django.dispatch import receiver
# # import uuid
# # from base.emails import send_account_activation_email
# # Create your models here.
# from products.models import Product, colorvariant,sizevariant

# class Profile(BaseModel):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name="profile")
#     is_email_verified = models.BooleanField(default=False)
#     email_token = models.CharField(max_length=100, null=True, blank=True)
#     profile_image = models.ImageField(upload_to='profile')

#     def get_Cart_count(self):
#         return CartItems.objects.filter(cart__is_paid = False, cart__user = self.user).count()

# # # Here we are addingg the signal to send email to verify the email id
# # @receiver(post_save, sender=User)
# # def send_email_token(sender, instance, created, **kwargs):
# #     try:
# #         if created:
# #             email_token = str(uuid.uuid4())
# #             email = instance.eamil
# #             send_account_activation_email(email, email_token)

# #     except Exception as e:
# #         print(e)


# class Cart(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
#     is_paid = models.BooleanField(default=False)



# class CartItems(BaseModel):
#     user = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
#     is_paid = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
#     sizevariant = models.ForeignKey(sizevariant, on_delete=models.SET_NULL, null=True, blank=True)
#     colorvariant =models.ForeignKey(colorvariant, on_delete=models.SET_NULL, null=True, blank=True)  