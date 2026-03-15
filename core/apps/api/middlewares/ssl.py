class ForceHttpsSchemeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.scheme = "https"  # doim HTTPS deb belgilash
        return self.get_response(request)
