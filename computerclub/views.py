from django.views.generic import TemplateView, ListView
from rest_framework.viewsets import ModelViewSet
from .models import Director, Administrator, User_test, Order
from .serializers import DirectorSerializer, AdministratorSerializer, UserSerializer, OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class AdministratorViewSet(ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


class UserViewSet(ModelViewSet):
    queryset = User_test.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('get', 'post', 'put', 'delete')


# Показывает частых гостей клуба
    @action(methods=['GET'], detail=False)
    def bestplayers(self, request):
        print(request.user)
        qs = self.get_queryset().filter(visitor__gte='Yes')
        serializer = self.get_serializer_class()(qs, many=True)
        return Response(data=serializer.data)
    
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ('get', 'post', 'put', 'delete')



# Открытые заказы
    @action(methods=['POST'], detail=True)
    def take(self, request, pk):
        return Response(data={'status': 'Open'})


class OrderList(ListView):
    template_name = 'computerclub/order.html'
    queryset = Order.objects.all()