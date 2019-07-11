from .models import User


def get_user(request):
    u_id = request.session.get("u_id")
    if u_id:
        u = User.objects.get(id=u_id)
        return {"u": u}
    else:
        return {}



