from django.http import HttpResponse


def view1(request):
    if not request.user.is_authenticated:
        return HttpResponse("You are not logged in\n please log in using username='user1' or 'user2' and password='testuser'")
    if not request.user.groups.filter(name='viewer1').exists():
        return HttpResponse("You are not authorized to view this page")
    return HttpResponse("This is View 1")
