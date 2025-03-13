from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from user.serializers import UserSerializer, UserSerializerWithAddress
from user.models import User

class UserList(ListCreateAPIView):
    serializer_class = UserSerializerWithAddress
    queryset = User.objects.all()

class UserView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

"""
L-List     /user/      - GET       - 200
C-reate     /user/      - POST      - 201
R-read      /user/1/    - GET       - 200
U-update    /user/1/    - PUT/PATCH - 200
D-delete    /user/1/    - DELETE    - 204
"""
