# changes by Muhammad Shoaib Sikander

from django.urls import path

from .views import home_page, page_1, page_2, page_3

urlpatterns = [
	path('', home_page, name='home_page'),
    path('Page_1/', page_1.as_view(), name='page_1'),
    path('Page_2/', page_2, name='page_2'),
    path('Page_3/', page_3, name='page_3'),
]