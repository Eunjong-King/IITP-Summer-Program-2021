from .models import Data
from rest_framework.viewsets import ModelViewSet
from .serializers import DataSerializer
from .filter import DataFilter
from rest_framework.response import Response
from rest_framework import status

class DataViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    filterset_fields = ('device', )
    filter_class = DataFilter
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)