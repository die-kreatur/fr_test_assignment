import uuid


class AnonIdSessionMiddlware:
    """Middleware для присвоения неавторизованным пользователям уникального id в рамках сессии"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and \
            'user_id' not in request.session:
            uid = str(uuid.uuid4().int)[:6]
            request.session['user_id'] = uid

        elif request.user.is_authenticated and \
            'user_id' not in request.session:
            uid = request.user.id
            request.session['user_id'] = uid

        response = self.get_response(request)

        return response
