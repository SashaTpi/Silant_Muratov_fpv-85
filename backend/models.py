from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Model(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'

class Client(Model):
    name = models.ForeignKey(CustomUser, verbose_name='Клиент', on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class ServiceComp(Model):
    name = models.ForeignKey(CustomUser, verbose_name='Сервисная компания', on_delete=models.CASCADE)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Список сервесных компаний'


class TransmMod(Model):
    name = models.CharField('Модель трансмиссии', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'


class MashinsMod(Model):
    name = models.CharField('Модель машины', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'


class MotorMod(Model):
    name = models.CharField('Модель мотора', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Модель мотора'
        verbose_name_plural = 'Модели моторов'


class MainBridgMod(Model): 
    name = models.CharField('Ведущий мост', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущего моста' 


class ControlBridgMod(Model):
    name = models.CharField('Управляемый мост', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемого моста'


class ServiceType(Model): 
    name = models.CharField('Вид ТО', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Вид технического обслуживания '
        verbose_name_plural = 'Виды технического обслуживания'


class FailureCharacter(Model):
    name = models.CharField('Характер отказа', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Описание отказа'
        verbose_name_plural = 'Виды отказа'


class FailureNode(Model): 
    name = models.CharField('Наименование узла', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узлы отказа'


class Recovery(Model): 
    name = models.CharField('Способ восстановления', max_length=64, unique=True)
    description = models.TextField('Описание', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы востановления'
    

class Mashins(models.Model):

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    zav_nom_mashins = models.CharField('Зав. № машины', primary_key=True, null=False, max_length=32, 
                                    unique=True)
    model_mashins = models.ForeignKey(MashinsMod, verbose_name='Модель техники', on_delete=models.CASCADE,
                                    related_name='model_mashins')

    model_motor = models.ForeignKey(MotorMod, verbose_name='Модель двигателя', on_delete=models.CASCADE,
                                    related_name='model_motor')
    zav_nom_motor = models.CharField('Зав. № двигателя', max_length=32, blank=True, null=True)
    
    model_transmission = models.ForeignKey(TransmMod, verbose_name='Модель трансмиссии',
                                    on_delete=models.CASCADE, related_name='model_transmission',
                                    blank=True, null=True)
    zav_nom_transmission = models.CharField('Зав. № трансмиссии', max_length=32, unique=True, blank=True, 
                                    null=True)

    model_main_bridge = models.ForeignKey(MainBridgMod, verbose_name='Модель ведущего моста',
                                    on_delete=models.CASCADE, related_name='model_main_bridge',
                                    blank=True, null=True)
    zav_nom_main_bridge = models.CharField('Зав. № ведущего моста', max_length=32, blank=True, null=True)

    model_controll_bridge = models.ForeignKey(ControlBridgMod, verbose_name='Модель управляемого моста',
                                              on_delete=models.CASCADE, related_name='model_controll_bridge',
                                              blank=True, null=True)
    zav_nom_controll_bridge = models.CharField('Зав. № управляемого моста', max_length=100, blank=True, null=True)

    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE,
                               related_name='client', blank=True, null=True)
    service_company = models.ForeignKey(ServiceComp, verbose_name='Сервисная компания', on_delete=models.CASCADE,
                                        related_name='service_company', blank=True, null=True)
    shipping_date = models.DateField('Дата отгрузки с завода', blank=True, null=True)  
    consignee = models.CharField('Грузополучатель (конечный потребитель)', max_length=250, blank=True, null=True)
    delivery_address = models.TextField('Адрес поставки (эксплуатации)', max_length=100, blank=True, null=True) 
    outfitting = models.TextField('Комплектация (доп. опции)', max_length=250, blank=True, null=True) 
      
    def __str__(self) -> str:
        return f'{self.zav_nom_mashins}'

    def get_absolute_url(self):
        return reverse('article-view', args=(str(self.pk),))


class TO(models.Model):

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'

    vid_TO = models.ForeignKey(ServiceType, verbose_name='Вид технического обслуживания', on_delete=models.CASCADE,
                               related_name='vid_TO') 
    date_TO = models.DateField('Дата проведения ТО')
    runtime = models.DecimalField('Наработка, м/час', max_digits=10, decimal_places=0)
    num_order = models.CharField('№ заказ-наряда', max_length=32, unique=True)
    date_order = models.DateField('Дата заказ-наряда')
    service_TO = models.ForeignKey(ServiceComp, verbose_name='Сервисная компания', on_delete=models.CASCADE)
    mashins_TO = models.ForeignKey(Mashins, verbose_name='Машина', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.mashins_TO}'

    def get_absolute_url(self):
        return reverse('article-view', args=(str(self.pk),))


class Reclamation(models.Model):
    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'

    mashins_c = models.ForeignKey(Mashins, verbose_name='Машина', on_delete=models.CASCADE)
    date_refusal = models.DateField('Дата отказа', null=True, blank=True)
    runtime_c = models.DecimalField('Наработка, м/час', max_digits=10, decimal_places=0)
    failure_node = models.ForeignKey(FailureNode, verbose_name='Узел отказа',
                                     on_delete=models.CASCADE, related_name='failure_node')
    reason_refusal = models.ForeignKey(FailureCharacter, verbose_name='Описание отказа',
                                       on_delete=models.CASCADE, related_name='reason_refusal')
    recovery_method = models.ForeignKey(Recovery, verbose_name='Способ восстановления',
                                        on_delete=models.CASCADE, related_name='recovery_method',)
    spare = models.TextField('Используемые запасные части', max_length=1000, blank=True, null=True) 
    date_recovery = models.DateField('Дата восстановления', blank=True, null=True)
    downtime = models.IntegerField('Время простоя техники (дней)', default=0, null=True)
    service = models.ForeignKey(ServiceComp, verbose_name='Сервисная компания', blank=True, null=True,
                                on_delete=models.CASCADE)

    def downtime(self):
        deltatime = self.date_recovery - self.date_refusal
        return deltatime.days

    def __str__(self):
        return f'{self.mashins_c} {self.reason_refusal}: {self.date_refusal}/{self.date_recovery}'



