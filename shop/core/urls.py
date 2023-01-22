from django.contrib import admin
from django.urls import path, include
# from shop.views import index, product, products, category, seller, callback, basket, order, addToBasket, removeItemFromBasket, categories
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api.views import  BasketViewSet, RatingViewSet, SellerViewSet, ProductViewSet, CallbackViewSet, CategoryViewSet, GetOrderView, GetProductView

router = DefaultRouter()

router.register('basket', BasketViewSet)
router.register('rating', RatingViewSet)
router.register('seller', SellerViewSet)
router.register('product', ProductViewSet)
router.register('callback', CallbackViewSet)
router.register('category', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/order-filter/', GetOrderView.as_view()),
    path('api/product-filter/', GetProductView.as_view()),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)