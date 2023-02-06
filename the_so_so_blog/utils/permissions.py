def is_own_user(request, obj):
    return request.user.id == obj.id
