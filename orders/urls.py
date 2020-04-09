from orders.views import OrderViewSet
from django.urls import path


orders = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create',
	'delete': 'bulk_delete'
})

order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path(r'<int:pk>/', order_detail),
    path(r'', orders),
]
