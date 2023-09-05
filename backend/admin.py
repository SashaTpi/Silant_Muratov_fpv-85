from import_export import resources
from import_export.admin import ImportExportMixin
from django.contrib import admin
from users.models import CustomUser
from .models import *


class BaseResource(resources.ModelResource):
    class Meta:
        report_skipped = True
        fields = ('id', 'name', 'description',)

class ServiceCompResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = ServiceComp


class ClientResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = Client


class MotorResource(resources.ModelResource):
    class Meta:
        model = MotorMod


class MainBridgModResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = MainBridgMod


class TransmModResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = TransmMod


class MashinsModResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = MashinsMod


class ControlBridgModResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = ControlBridgMod


class FailureNodeResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = FailureNode


class RecoveryResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = Recovery


class ServiceTypeResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = ServiceType


class FailureCharacterResource(BaseResource):
    class Meta(BaseResource.Meta):
        model = FailureCharacter


class MashinsResource(resources.ModelResource):
    class Meta(BaseResource.Meta):
        model = Mashins
        fields = ('zav_nom_mashins', 'model_mashins', 'model_motor', 'model_transmission', 
                  'model_main_bridge', 'model_controll_bridge', 'shipping_date', 'outfitting', 
                  'consignee', 'service_company',
        )

class TOResource(resources.ModelResource):
    class Meta:
        model = TO
        report_skipped = True
        fields = ('id', 'vid_TO', 'date_TO', 'num_order', 'date_order','runtime',
                  'service_TO', 'mashins_TO',
        )


class ReclamationResource(resources.ModelResource):
    class Meta:
        model = Reclamation
        report_skipped = True
        fields = ('id', 'mashins_c', 'date_refusal', 'runtime_c', 'failure_node', 
                  'reason_refusal', 'recovery_method', 'spare', 'date_recovery', 'downtime',
        )


@admin.register(Client)
class ClientAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ClientResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(ServiceComp)
class ServiceCompAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ServiceCompResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(MashinsMod)
class MashinsModAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MashinsModResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(MotorMod)
class MotorAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MotorResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(MainBridgMod)
class MainBridgModAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MainBridgModResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(TransmMod)
class TransmModAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TransmModResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(ControlBridgMod)
class ControlBridgModAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ControlBridgModResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(FailureNode)
class FailureNodeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FailureNodeResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(Recovery)
class RecoveryAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = RecoveryResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(ServiceType)
class ServiceTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ServiceTypeResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(FailureCharacter)
class FailureCharacterAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FailureCharacterResource
    list_display = ('id', 'name', 'description',)
    list_filter = ('name',)


@admin.register(Mashins)
class MashinsAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MashinsResource
    list_display = (
        'zav_nom_mashins', 'model_mashins', 'model_motor', 'model_transmission', 
        'model_main_bridge', 'model_controll_bridge', 'service_company',
    )

    list_filter = ('zav_nom_mashins',)


@admin.register(TO)
class TOAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TOResource
    list_display = (
        'mashins_TO', 'vid_TO', 'date_TO', 'num_order', 'date_order', 'runtime',
        'service_TO',
    )

    list_filter = ('mashins_TO',)


@admin.register(Reclamation)
class ReclamationAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ReclamationResource
    list_display = (
        'id', 'mashins_c', 'date_refusal', 'runtime_c', 'failure_node', 
        'reason_refusal', 'recovery_method', 'spare', 'date_recovery', 'downtime',
    )

    list_filter = ('mashins_c',)
