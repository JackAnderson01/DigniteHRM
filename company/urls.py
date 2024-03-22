from django.urls import path
from .views import CompanyCreateView, CompanyVerifyAccessKeyView


urlpatterns = [
    path("register", CompanyCreateView.as_view(), name="CreateCompany"),
    path("verify-access-key", CompanyVerifyAccessKeyView.as_view(), name="VerifyAccessKey"),
  


]