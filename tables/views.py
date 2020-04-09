from .models import Table
from .serializers import TableSerializer
from base.views import BaseViewSet

class TableViewSet(BaseViewSet):
    """
       list:
       Return a list of all Tables which satisfying is_deleted=False and is_available=True statements.

       retrieve:
       Return the given Table.

       create:
       Create a new Table instance.

       update:
       Update the given Table instance.

       destroy:
       Set is_deleted=True & is_available=False and hide the given Table instance.
    """
    serializer_class = TableSerializer
    queryset = Table.objects.filter(is_deleted=False)
