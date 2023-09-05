from rest_framework import routers
from api.views import *


router = routers.DefaultRouter()

viewsets = [
    (MashinsModViewSet, 'model_mashins'),
    (MotorModViewSet, 'motors'),
    (TransmModViewSet, 'transmissions'),
    (MainBridgModViewSet, 'mainbridge'),
    (ControlBridgModViewSet, 'controllbridge'),
    (RecoveryViewSet, 'recovery'),
    (FailureCharacterViewSet, 'failurecharacter'),
    (FailureNodeViewSet, 'failurenode'),
    (ServiceTypeViewSet, 'servicetype'),
    (MashinsViewSet, 'mashins'),
    (TOViewSet, 'TO'),
    (ReclamationViewSet, 'reclamation'),
    (ClientViewSet, 'client'),
    (ServiceCompViewSet, 'service'),
]

for viewset, basename in viewsets:
    router.register(basename, viewset)



