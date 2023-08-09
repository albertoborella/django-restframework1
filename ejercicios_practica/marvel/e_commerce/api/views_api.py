from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
def primera_vista_api(request):
    template = '''<h1>Mi primera vista con api_view</h1>'''
    return HttpResponse(template)


@api_view(['GET','POST'])
@permission_classes([])
def segunda_vista_api(request):
    template = f'<h1>Mi nombre: {request.GET.get("mi_nombre")}</h1>'
    print(template)
    return HttpResponse(template)


@api_view(['GET','POST'])
@permission_classes([])
def tercera_vista_api(request):
    template = f'<h3>Bienvenido {request.GET.get("usuario")} al curso Django-RestFramework</h3>'
    print(template)
    return HttpResponse(template)
