from rest_framework import viewsets
from backend.models import *
from .serializers import *


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ServiceCompViewSet(viewsets.ModelViewSet):
    queryset = ServiceComp.objects.all()
    serializer_class = ServiceCompSerializer
    permission_classes = []


class ReclamationViewSet(viewsets.ModelViewSet):
    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer


class MotorModViewSet(viewsets.ModelViewSet):
    queryset = MotorMod.objects.all()
    serializer_class = MotorModSerializer


class TransmModViewSet(viewsets.ModelViewSet):
    queryset = TransmMod.objects.all()
    serializer_class = TransmModSerializer


class MashinsViewSet(viewsets.ModelViewSet):
    queryset = Mashins.objects.all()
    serializer_class = MashinsSerializer


class MashinsModViewSet(viewsets.ModelViewSet):
    queryset = MashinsMod.objects.all()
    serializer_class = MashinsModSerializer


class MainBridgModViewSet(viewsets.ModelViewSet):
    queryset = MainBridgMod.objects.all()
    serializer_class = MainBridgModSerializer


class ControlBridgModViewSet(viewsets.ModelViewSet):
    queryset = ControlBridgMod.objects.all()
    serializer_class = ControlBridgModSerializer


class RecoveryViewSet(viewsets.ModelViewSet):
    queryset = Recovery.objects.all()
    serializer_class = RecoverySerializer


class FailureCharacterViewSet(viewsets.ModelViewSet):
    queryset = FailureCharacter.objects.all()
    serializer_class = FailureCharacterSerializer


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class TOViewSet(viewsets.ModelViewSet):
    queryset = TO.objects.all()
    serializer_class = TOSerializer


class FailureNodeViewSet(viewsets.ModelViewSet):
    queryset = FailureNode.objects.all()
    serializer_class = FailureNodeSerializer