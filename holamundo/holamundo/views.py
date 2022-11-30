from django.http import HttpResponse

# Función que devuelve una respuesta http con el mensaje "Hola mundo"
def saludo(request):
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Hasta luego")

def post(request, id):
    return HttpResponse("Post id")