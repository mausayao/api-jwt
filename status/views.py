from rest_framework import request
from rest_framework import generics, mixins

from django.shortcuts import get_object_or_404

from .models import Status
from .serializers import StatusSerializer


class StatusAPIDetailView(
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.RetrieveAPIView):
                            
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class StatusAPIView(
                    mixins.CreateModelMixin,
                    generics.ListAPIView):

    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    


