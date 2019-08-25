from django.http import HttpResponse


def view2(request):
    if not request.user.is_authenticated:
        return HttpResponse(
            "<h3>You are not logged in\n please log in using username='user1' or 'user2' and password='testuser'</h3>"
            "<a href='/admin'>login here</a>")
    if not request.user.groups.filter(name='viewer2').exists():
        return HttpResponse("You are not authorized to view this page")
    return HttpResponse("This is View 2")
