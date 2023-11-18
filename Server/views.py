from django.shortcuts import redirect

#redirect function.
def redirect_(request):
    print(request.get_host(), request.META['SERVER_PORT'])
    print(f"http://{str(request.get_host())}/homepage")
    return redirect(f"http://{str(request.get_host())}/homepage")