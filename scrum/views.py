import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import *
from .validaciones import validar_tarea


# Create your views here.
def bienvenida(request):
    return HttpResponse("Hola chicos estamos en nuestro primer controlador")


def listar_tareas(request):
    if request.method != "GET":
        return JsonResponse("Error esta petición solo funciona con get")

    tareas = Tareas.objects.all().values()
    return JsonResponse(list(tareas), safe=False)

    # def listar_tarea(request):
    #     if request.method != "GET":
    #         return JsonResponse("Error esta petición solo funciona con get")
    #
    #     try:
    #         tarea = Tareas.objects.get(id=id)
    #     except Tareas.DoesNotExist:
    #         return JsonResponse({"error": "La tarea no existe"}, status=404, safe=False)
    #
    #     datos = {
    #         "id": tarea.id,
    #         "nombre": tarea.nombre,
    #         "fecha_inicio": tarea.fecha_inicio,
    #         "fecha_fin": tarea.fecha_fin,
    #         "completada": tarea.completada,
    #         "sprint_id": tarea.sprint.id,
    #         "programador_id": tarea.programador.id},
    #     }

    return JsonResponse(datos, safe=False)


def listar_tareas_mejorado(request):
    if request.method != "GET":
        return JsonResponse("Error esta petición solo funciona con get")

    tarea = Tareas.objects.filter(id=id).values().first()
    return JsonResponse(tarea, safe=False)


def listar_tareas_completadas(request):
    if request.method != "GET":
        return JsonResponse("Error esta petición solo funciona con get")

    tareas = Tareas.objects.filter(completada=True).values()
    return JsonResponse(list(tareas), safe=False)


@csrf_exempt
def crear_tareas(request):
    if request.method != "POST":
        return JsonResponse({"error": "Error esta petición solo funciona con post"}, status=405)

    try:
        tarea_json = json.loads(request.body)
    except:
        return JsonResponse({"error": "Json no está bien formado"}, status=400)

    # tarea_validada= validar_tareas(tarea_json)

    errores = validar_tarea(tarea_json)

    if errores:
        return JsonResponse({"errores": errores}, status=400)

    # Aquí hago el post
    tarea = Tareas.objects.create(
        nombre=tarea_json.get("nombre"),
        fecha_inicio=tarea_json.get("fecha_inicio"),
        fecha_fin=tarea_json.get("fecha_fin"),
        completada=tarea_json.get("completada", False),
        sprint_id=tarea_json.get("sprint_id"),
        programador_id=tarea_json.get("programador_id"),
    )
    ## si la tarea vienen etiquetas y esas etiquetas no existen, que cree las etiquetas

    etiquetas = tarea_json.get("etiquetas", [])
    crear_etiquetas(etiquetas, objeto)

    return JsonResponse({'exito': 'Se ha creado correctamente', 'tarea': tarea.id}, status=201)


@csrf_exempt
def crear_programador(request):
    if request.method != "POST":
        return JsonResponse({"error": "Error esta petición solo funciona con post"}, status=405)

    try:
        programador_json = json.loads(request.body)
    except:
        return JsonResponse({"error": "Json no está bien formado"}, status=400)
    programador_json = Tareas.objects.create(
        nombre=programador_json.get("nombre"),
        apellido1=programador_json.get("apellido1"),
        apellido2=programador_json.get("apellido2"),
    )


def crear_etiquetas(etiquetas, objeto):
    for etiqueta in etiquetas:
        etiqueta_model, creada = Etiqueta.objects.get_or_create(nombre=etiqueta)
        objeto.etiquetas.add(etiqueta_model)
        if not creada:
            print("Se ha creado correctamente")
        else:
            print("Etiqueta no creada")
