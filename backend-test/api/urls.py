from django.urls import path
from .views import UserLoginAPIView, UserRegisterAPIView, UserActionLogCreateAPIView,EventUserAPIView, CommentAPIView

urlpatterns = [
    path("login/", UserLoginAPIView.as_view(), name="user-login"),
    path("user-register/", UserRegisterAPIView.as_view(), name="user-register"),
    path("user-action-log/", UserActionLogCreateAPIView.as_view(), name='user-action-log-create'),
    path("register-event/", EventUserAPIView.as_view(), name='register-event'),
    path("register-comment/", CommentAPIView.as_view(), name='register-comment'),
]