from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Coffee
from .serializers import CoffeeSerializer
from .permissions import IsOwnerOrReadOnly


class CoffeeList(ListCreateAPIView):
    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    queryset = Coffee.objects.all()

    #serializing
    serializer_class = CoffeeSerializer

# The ThingDetail needs the same things
class CoffeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
    permission_classes = (IsOwnerOrReadOnly,)