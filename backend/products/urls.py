from django.urls import path
from . import views

urlpatterns = [
    # path('',views.ProductListCreateApiView.as_view()),
    # path('<int:pk>/',views.ProductDetailApiView.as_view()),
    path('',views.ProductMixinView.as_view()),
    path('<int:pk>/',views.ProductMixinView.as_view()),
    path('<int:pk>/update/',views.ProductUpdateApiView.as_view()),
    path('<int:pk>/delete/',views.ProductDeleteApiView.as_view())
]