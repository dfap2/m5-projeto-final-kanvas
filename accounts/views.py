from .models import Account
from .serializers import AccountSerializer
from rest_framework import generics


class UserView(generics.CreateAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
