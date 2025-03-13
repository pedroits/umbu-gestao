from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from address.serializers import AddressSerializer
from address.models import Address

class AddressList(ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class AddressView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

"""
L-List      /address/      - GET       - 200
C-reate     /address/      - POST      - 201
R-read      /address/1/    - GET       - 200
U-update    /address/1/    - PUT/PATCH - 200
D-delete    /address/1/    - DELETE    - 204
"""
