from django.http import HttpResponseForbidden

class AccessDeniedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Check if the user is trying to access a restricted view
        if response.status_code == 302 and response.url.startswith('/admin/') and not request.user.is_staff:
            return HttpResponseForbidden("Access Denied. You must be signed in as staff to access this page.")
        return response
