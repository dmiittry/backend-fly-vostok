from django.db import models

class CityLang(models.Model):
    rus = models.CharField('Rus', max_length=50, blank = True, null=True)
    eng = models.CharField('Eng', max_length=50, blank = True, null=True)
    uz = models.CharField('Uz', max_length=50, blank = True, null=True)
    tj = models.CharField('Tj', max_length=50, blank = True, null=True)
    cn = models.CharField('Cn', max_length=50, blank = True, null=True)
    
    def __str__(self):
        return ''
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Static(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT, null=True,verbose_name='Пользователь (Купивший билет)')
    firts_name = models.CharField('Фамилия, Имя пассажиров', max_length=200)
    data = models.DateTimeField('Дата покупки')

    vylet = models.CharField('Вылет (город)', max_length=50)
    data_vyleta = models.DateTimeField('Вылет (дата и время')
    port_vyleta = models.CharField('Вылет (аэропорт)', max_length=50)
    
    prilet = models.CharField('Прилёт (город)', max_length=50)
    data_prileta = models.DateTimeField('Прилёт (дата и время)')
    port_prileta = models.CharField('Прилёт (аэропорт)', max_length=50)

    avia_comp = models.CharField('Авиакомпания', max_length=50)

    col_pass = models.IntegerField('Количество пассажиров')

    price = models.CharField('Стоимость', max_length=50)


    def __str__(self):
        return ''
    
    
    class Meta:
        verbose_name = 'Статистику'
        verbose_name_plural = 'Статистика'

class Passajir(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT, null=True,verbose_name='Пользователь')
    firts_name = models.CharField('Фамилия', max_length=50)
    second_name = models.CharField('Имя', max_length=50)
    data = models.DateTimeField('Дата регистрации')
    phone = models.IntegerField('Номер телефона')
    passport = models.CharField('Серия и номер паспорта', max_length=50)
    srok = models.DateTimeField('Дата регистрации')
    grajdanstvo = models.CharField('Гражданство', max_length=50)
    email = models.CharField('Email', blank=True, null=True, max_length=50)
    category  = models.CharField('Возрастная категрия', blank=True, null=True, max_length=50)
    graj_id = models.CharField('Граж. id', blank=True, null=True, max_length=50)
    gender = models.CharField('Пол', blank=True, null=True, max_length=50)
    def __str__(self):
        return self.firts_name +' ' + self.second_name 

    class Meta:
        verbose_name = 'Пассажир'
        verbose_name_plural = 'Пассажиры'


class Users(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50,blank=True, null=True)
    phone = models.CharField('Номер телефона', max_length=20)
    data = models.DateTimeField('Дата регистрации', blank=True, null=True)
    uid = models.CharField('UID', max_length=100, blank=True, null=True)
    lang = models.CharField('Lang', max_length=20, blank=True, null=True)
    def phoneSet(phone):
        return phone
        
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Notificet(models.Model):
    text = models.TextField(verbose_name='Текст уведомления')
    data = models.DateTimeField('Дата отправки')
    user = models.ForeignKey('Users', on_delete=models.PROTECT,blank=True, null=True,verbose_name='Пользователи')
    see = models.CharField('see', max_length=20,blank=True, null=True, default='false')
    def __str__(self):
        return ''
        
    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

class Feedback(models.Model):
    text = models.TextField(verbose_name='Обратная связь')
    user = models.ForeignKey('Users', on_delete=models.PROTECT,blank=True, null=True,verbose_name='Пользователь')
    data_send = models.DateTimeField('Дата получение')
    otvet = models.TextField(verbose_name='Ответ', blank=True)

    def __str__(self):
        return ''
    
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class ErrorApp(models.Model):
    text = models.TextField(verbose_name='Ошибка')

    def __str__(self):
        return self.text


    class Meta:
        verbose_name = 'Ошибка'
        verbose_name_plural = 'Ошибки'


class Information(models.Model):
    text = models.TextField(verbose_name='Название')

    def __str__(self):
        return ''
    
    
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'


class Passport(models.Model):
    img = models.CharField(verbose_name='Паспорт', max_length=50)
    name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    dr = models.CharField(verbose_name='День рождение', max_length=50)
    nomer = models.CharField(verbose_name='Номер паспорта', max_length=50)
    srok = models.CharField(verbose_name='Срок паспорта', max_length=50)
    def __str__(self):
        return ''
    
    
    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорты'
