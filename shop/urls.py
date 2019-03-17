"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.urls import path, re_path
from django.urls import include
from shop.settings import MEDIA_ROOT
from django.views.static import serve
from django.views.generic.base import TemplateView

from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryListViewSet, BannerViewset, IndexCategoryViewset, HotSearchsViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView

router = DefaultRouter()

router.register(r'goods', GoodsListViewSet, base_name="goods")
router.register(r'categorys', CategoryListViewSet, base_name="categorys")
router.register(r'codes', SmsCodeViewset, base_name="codes")
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")
router.register(r'users', UserViewset, base_name="users")
router.register(r'userfavs', UserFavViewset, base_name="userfavs")
router.register(r'messages', LeavingMessageViewset, base_name="messages")
router.register(r'address', AddressViewset, base_name="address")
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")
router.register(r'orders', OrderViewset, base_name="orders")
router.register(r'banners', BannerViewset, base_name="banners")
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('docs/', include_docs_urls(title="shop")),
    path('api-auth/', include('rest_framework.urls'), 'rest_framework'),
    path('api-token-auth/', views.obtain_auth_token),
    re_path('^login/$', obtain_jwt_token),
    path('', include(router.urls)),
    path('alipay/return/', AlipayView.as_view(), name="alipay"),
    path('index', TemplateView.as_view(template_name="index.html")),
    path('', include('social_django.urls', namespace='social')),
    re_path(r'^surprise/$', TemplateView.as_view(template_name="surprise.html"))
]