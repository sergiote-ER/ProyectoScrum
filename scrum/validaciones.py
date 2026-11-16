from .models import *

def validar_tarea(tarea_json):
    errores = []
    if not tarea_json.get("sprint_id"):
        errores.append("El campo 'sprint_id' es obligatorio.")
    elif not Sprint.objects.filter(id=tarea_json.get("sprint_id")).exists():
        errores.append(f"El sprint con ID {tarea_json.get("sprint_id")} no existe.")

    if not tarea_json.get("programador_id"):
        errores.append("El campo 'programador_id' es obligatorio.")
    elif not Programador.objects.filter(id=tarea_json.get("programador_id")).exists():
        errores.append(f"El programador con ID {tarea_json.get("programador_id")} no existe.")

    return errores