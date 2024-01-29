"""
URL configuration for BonnyFlowers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("location.urls")),
    path("", include("orders.urls")),
    path("", include("feedback.urls")),
    path("", include("cart.urls")),
    path("", include("mainpage.urls")),
    path("catalogue/", include("catalogue.urls")),
    path("delivery_and_payment/", include("delivery_and_payment.urls")),
    path("reviews/", include("reviews.urls")),
    path("product/", include("products.urls")),
    path("zoho-token/", include("zoho_token.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)