from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, EnterpriseDetailView, EnterpriseListView, success_request, store

app_name = 'landing'

urlpatterns = [
    path('', home, name='home'),
    path('store/', store, name='store'),
    path('enterprise/<str:slug>/', EnterpriseDetailView.as_view(), name='enterprise_detail'),
    path('enterprise_list/', EnterpriseListView.as_view(), name='enterprise_list'),
    path('success_request/', success_request, name='success_request'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
