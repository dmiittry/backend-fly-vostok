from django.contrib import admin
from main.models import Passajir, Feedback, Information, Notificet, Passport, Static, Users, ErrorApp, CityLang
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

# Register your models here.
class MyAdminSite(AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        #for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list
class CityLangAdmin(admin.ModelAdmin):
    list_display = ('id', 'rus', 'eng', 'uz', 'tj', 'cn')
    list_display_links = ('id', 'rus', 'eng', 'uz', 'tj', 'cn')

class StaticAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'firts_name', 'data', 'vylet', 'data_vyleta', 'port_vyleta', 'prilet','data_prileta','port_prileta','avia_comp','col_pass','price')
    list_display_links = ('id', 'user', 'firts_name', 'data', 'vylet', 'data_vyleta', 'port_vyleta', 'prilet','data_prileta','port_prileta','avia_comp','col_pass','price')

class PassajirAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'firts_name', 'second_name', 'data', 'phone', 'passport', 'srok', 'grajdanstvo', 'email')
    list_display_links = ('id', 'user', 'firts_name', 'second_name', 'data', 'phone', 'passport', 'srok', 'grajdanstvo', 'email')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','phone', 'data')
    list_display_links = ('id', 'name','phone', 'data')
    
class NotificetAdmin(admin.ModelAdmin):
    list_display = ('id', 'text','data', 'user')
    list_display_links = ('id', 'text','data', 'user')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'text','user', 'data_send', 'otvet')
    list_display_links = ('id', 'text','user', 'data_send', 'otvet')

class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')

class PassportAdmin(admin.ModelAdmin):
    list_display = ('id', 'img', 'name', 'surname', 'dr', 'nomer', 'srok')
    list_display_links = ('id', 'img', 'name', 'surname', 'dr', 'nomer', 'srok')

class ErrorAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id','text')


admin.site = MyAdminSite()

admin.site.register(Users, UsersAdmin)
admin.site.register(Passajir, PassajirAdmin)
admin.site.register(Static, StaticAdmin)
admin.site.register(Notificet, NotificetAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(ErrorApp, ErrorAppAdmin)
admin.site.register(CityLang, CityLangAdmin)

admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)

admin.site.site_title = 'Fly Vostok'
admin.site.site_header = 'Fly Vostok'
