from .models import Order
from .serializers import OrderSerializer
from base.views import BaseViewSet

class OrderViewSet(BaseViewSet):
    """
       list:
       Return a list of all Orders.

       retrieve:
       Return the given Order.

       create:
       Create a new Order instance.

       update:
       Update the given Order instance.

       destroy:
       Set is_deleted=True & is_available=False and hide the given Order instance.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.filter(is_deleted=False)
