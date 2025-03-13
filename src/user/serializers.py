from rest_framework import serializers

from user.models import User
from address.models import Address
from address.serializers import AddressSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UserSerializerWithAddress(serializers.ModelSerializer):
    address = AddressSerializer()

    def create(self, validated_data):
        if validated_data.get('address', None):
            validated_data['address'] = Address.objects.create(**validated_data['address'])

        return super().create(validated_data)

    class Meta:
        model = User
        fields = '__all__'
