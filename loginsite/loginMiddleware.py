import re
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
EXCLUDE_URL = (
     '/loginsite/login/',
     '/loginsite/logout/',
     '/captchaimage/',
     '/loginsite/refresh',
)
exclued_path = [re.compile(item) for item in EXCLUDE_URL]
class PubAuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        url_path = request.path
        for each in exclued_path:
            if re.match(each, url_path):
                return None
        if not request.session.get('is_login', None):
            return HttpResponseRedirect('/loginsite/login/')
        else:
            return None
