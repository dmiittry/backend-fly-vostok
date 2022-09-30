from rest_framework import serializers
from .models import Static, Passajir, Notificet, Information, Users, Feedback, CityLang, ErrorApp

class CityLangSerializers(serializers.ModelSerializer):
    class Meta:
        model = CityLang
        fields = '__all__'

class ErrorAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = ErrorApp
        fields = '__all__'
 
class StaticSerializers(serializers.ModelSerializer):
    class Meta:
        model = Static
        fields = '__all__'

class PassajirSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passajir
        fields = '__all__'

class NotificetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notificet
        fields = '__all__'

class InformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
