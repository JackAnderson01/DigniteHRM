from django.urls import path
from .views import HomeView, UserCreateView, VerifyOtpView, RegenerateOtpView, ForgotPasswordView, VerifyForgotOtpView,CompanyLoginView, LogoutView, ValidateTokenView, ChangePasswordView, EmployeeLoginView


urlpatterns = [
    path("signup", UserCreateView.as_view(), name="Signup"),
    path("verify-otp", VerifyOtpView.as_view(), name="VerifyOtp"),
    path("resend-otp", RegenerateOtpView.as_view(), name="RegenerateOtp"),
    path("forgot-password", ForgotPasswordView.as_view(), name="ForgotPassword"),
    path("verify-forgot-otp", VerifyForgotOtpView.as_view(), name="VerifyForgotOtp"),
    path("change-password", ChangePasswordView.as_view(), name="ChangePassword"),
    path("company-login", CompanyLoginView.as_view(), name="CompanyLogin"),
    path("employee-login", EmployeeLoginView.as_view(), name="EmployeeLogin"),
    path("logout", LogoutView.as_view(), name="Logout"),
    path("validate-token", ValidateTokenView.as_view(), name="ValidateToken"),


]