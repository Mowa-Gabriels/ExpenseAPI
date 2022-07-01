from urllib import response
from requests import Response
from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):

        response = ''
        if 'Error Detail' in str(data):
            response = json.dumps({'errors:data'})
        else:
            response = json.dumps({'data:data'})
        return super().render(data, accepted_media_type, renderer_context)

        return response