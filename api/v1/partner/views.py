from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from api.v1.partner.serializer import PartnerSerializer
from base.formats import format_partner
from base.helper import CustomGenericAPIView, custom_response
from bmain.models import Partner


class PartnerView(CustomGenericAPIView):
    serializer_class = PartnerSerializer

    def get_object(self, pk):
        try:
            root = Partner.objects.get(pk=pk)
        except:
            raise NotFound("Partner Not Found")
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            try:
                response = format_partner(Partner.objects.get(pk=pk))
            except:
                response = {}
        else:
            response = [format_partner(x) for x in Partner.objects.all()]

        return Response(custom_response(status=True, data=response))

    def post(self, requests, *args, **kwargs):
        seriazlizer = self.get_serializer(data=requests.data)
        seriazlizer.is_valid(raise_exception=True)
        print(seriazlizer)
        data = seriazlizer.create(seriazlizer.data)

        return Response(custom_response(status=True, data=format_partner(data)))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)

        seriazlizer = self.get_serializer(data=requests.data, instance=root, partial=True)
        seriazlizer.is_valid(raise_exception=True)
        data = seriazlizer.save()
        return Response(custom_response(status=True, data=format_partner(data)))

    def delete(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        slug = root.company
        root.delete()

        return Response(custom_response(status=True, data={"success": f"{slug} partner o'chirib tashlandi"}))
