from django.urls import path

from api.v1.category.views import CtgView
from api.v1.pages.views import PagesViews
from api.v1.partner.views import PartnerView



urlpatterns = [
    path('ctg/', CtgView.as_view()),
    path('ctg/<int:pk>/', CtgView.as_view()),

    path('partner/', PartnerView.as_view()),
    path('partner/<int:pk>/', PartnerView.as_view()),



    path('pages/', PagesViews.as_view()),




]

