from rest_framework import viewsets, permissions
from main.serializers import FeedbackSerializers, InformationSerializers, NotificetSerializers, PassajirSerializers, StaticSerializers, UsersSerializers, ErrorAppSerializers, CityLangSerializers
from .models import Static, Passajir, Notificet, Information, Users, Feedback, CityLang, ErrorApp

class CityLangViewSet(viewsets.ModelViewSet):
    queryset = CityLang.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CityLangSerializers

class ErrorAppViewSet(viewsets.ModelViewSet):
    queryset = ErrorApp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ErrorAppSerializers

class StaticViewSet(viewsets.ModelViewSet):
    queryset = Static.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StaticSerializers

class PassajirViewSet(viewsets.ModelViewSet):
    queryset = Passajir.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PassajirSerializers

class NotificetViewSet(viewsets.ModelViewSet):
    queryset = Notificet.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NotificetSerializers

class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InformationSerializers

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsersSerializers

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FeedbackSerializers
