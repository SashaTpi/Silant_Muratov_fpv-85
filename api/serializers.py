from rest_framework import serializers
from backend.models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ServiceCompSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceComp
        fields = '__all__'


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'


class TOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TO
        fields = '__all__'


class FailureNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureNode
        fields = '__all__'


class MotorModSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorMod
        fields = '__all__'


class TransmModSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmMod
        fields = '__all__'


class MashinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mashins
        fields = '__all__'


class MashinsModSerializer(serializers.ModelSerializer):
    class Meta:
        model = MashinsMod
        fields = '__all__'


class MainBridgModSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBridgMod
        fields = '__all__'


class ControlBridgModSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlBridgMod
        fields = '__all__'


class RecoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recovery
        fields = '__all__'


class ReclamationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamation
        fields = '__all__'


class FailureCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureCharacter
        fields = '__all__'
