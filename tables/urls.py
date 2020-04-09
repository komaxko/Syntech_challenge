from tables.views import TableViewSet
from django.urls import path


tables = TableViewSet.as_view({
    'get': 'list',
    'post': 'create',
	'delete': 'bulk_delete'
})

table_detail = TableViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path(r'<int:pk>/', table_detail),
    path(r'', tables),
]
