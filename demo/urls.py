"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from explorer import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.ExplorerView.as_view()),
    path('insurance/', views.InsuranceView.as_view()),
    path('hospital/', views.HospitalView.as_view()),
    path('medblock/', views.MedBlockListCreateView.as_view()),
    path('32HFdF1649Fd1DE5CfADb8Ca7II0bbcd2A3FfFf5f1D2af1bDc4dAfffd44d55Dr/', views.SupplyChainView.as_view()),
    path('medblock/<str:hash>/', views.MedBlockDetailView.as_view()),
    path('admin/', admin.site.urls),
    path('<str:hash>/', views.ExplorerDetailView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

