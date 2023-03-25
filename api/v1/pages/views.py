from rest_framework.response import Response

from api.v1.pages.pages import page_index, page_teacher, page_vacancy
from base.error_messages import MESSAGE, error_params_unfilled
from base.helper import CustomGenericAPIView, custom_response
from corsheaders.conf import *


class PagesViews(CustomGenericAPIView):

    def post(self, requests, *args, **kwargs):
        data = requests.data
        params = data.get('params')
        method = data.get("method")

        if method is None:
            return Response(custom_response(status=False, message=MESSAGE['MethodMust']))

        if params is None:
            return Response(custom_response(status=False, message=MESSAGE['ParamsMust']))

        if "lang" not in params or not params["lang"]:
            return Response(custom_response(status=False, message=error_params_unfilled("lang")))
        langs = ['uz', "ru", "en"]
        if params['lang'] not in langs:
            message = {
                "uz": "Bunaqa til yo'q",
            }
            return Response(custom_response(status=False, message=message))

        if method == "index":
            return Response(custom_response(status=True, data=page_index(params['lang'])))
        elif method == "teacher":
            return Response(custom_response(status=True, data=page_teacher(params['lang'])))
        elif method == "vacancy":

            return Response(custom_response(status=True, data=page_vacancy(params['lang'])))
        else:
            return Response(custom_response(status=False, message=MESSAGE['MethodDoesNotExist']['default']))
