from django.contrib.auth.models import User, Group
from store.models import Sell, Client, Seller, Product
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, SalesSerializer, ClientSerializer, SellerSerializer, SellSerializer, ProductSerializer
from .services import create_products_for_sell, group_by
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import datetime, timedelta


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']


class SellerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']


class SellViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        if 'product' not in request.data:
            return super().create(request, *args, **kwargs)
        result = create_products_for_sell(request.data)
        serializer = SellSerializer(result)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class SalesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sell.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']


class CommissionViewSet(viewsets.ViewSet):
    def list(self, request):
        start_date = request.query_params.get('start-date', '2022-01-01')
        end_date = request.query_params.get('end-date', datetime.today().strftime('%Y-%m-%d'))
        end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
        result, total = group_by(start_date, end_date)
        return JsonResponse({'data': result, "total": total}, safe=False, status=status.HTTP_200_OK)
