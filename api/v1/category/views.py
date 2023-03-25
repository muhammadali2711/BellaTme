from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from api.v1.category.serializer import CtgSerializer
from base.formats import format_ctg
from base.helper import CustomGenericAPIView, custom_response
from bmain.models import Category


class CtgView(CustomGenericAPIView):
    serializer_class = CtgSerializer

    def get_object(self, pk):
        try:
            root = Category.objects.get(pk=pk)
        except:
            raise NotFound("Category Not Found")
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            try:
                response = format_ctg(Category.objects.get(pk=pk))
            except:
                response = {}
        else:
            response = [format_ctg(x) for x in Category.objects.all()]

        return Response(custom_response(status=True, data=response))

    def post(self, requests, *args, **kwargs):
        seriazlizer = self.get_serializer(data=requests.data)
        seriazlizer.is_valid(raise_exception=True)
        print(seriazlizer)
        data = seriazlizer.create(seriazlizer.data)

        return Response(custom_response(status=True, data=format_ctg(data)))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)

        seriazlizer = self.get_serializer(data=requests.data, instance=root, partial=True)
        seriazlizer.is_valid(raise_exception=True)
        data = seriazlizer.save()
        return Response(custom_response(status=True, data=format_ctg(data)))

    def delete(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        slug = root.slug
        root.delete()

        return Response(custom_response(status=True, data={"success": f"{slug} Categorysi o'chirib tashlandi"}))
