Respuestas Eva3:
Recursos y URIs

Recurso: /api/v1/tareas/
Descripción: Listar todas las tareas y crear nuevas.

Recurso: /api/v1/tareas/{id}/
Descripción: Obtener detalle, actualizar parcialmente o eliminar una tarea específica.

---------------------------
Verbos HTTP y códigos esperados

GET /api/v1/tareas/ → Listar todas las tareas → 200 OK
POST /api/v1/tareas/ → Crear nueva tarea → 201 Created
GET /api/v1/tareas/{id}/ → Obtener detalle de una tarea → 200 OK / 404 Not Found
PATCH /api/v1/tareas/{id}/ → Actualizar parcialmente una tarea → 200 OK / 404 Not Found
DELETE /api/v1/tareas/{id}/ → Eliminar una tarea → 204 No Content / 404 Not Found
POST / PATCH con datos inválidos → Validación de campos → 400 Bad Request

---------------------------
Reglas REST aplicadas

1. Stateless
Cada petición HTTP contiene toda la información necesaria; no se mantiene sesión en el servidor.

2. JSON
"El lenguaje universal para intercambiar datos", es como enviar información en formato de texto organizado
Todas las solicitudes y respuestas usan formato JSON (Content-Type: application/json).

3. Versionado en la ruta
La API usa /api/v1/ para permitir futuros cambios sin romper clientes.

4. Idempotencia
- GET no cambia el estado del servidor, se puede repetir sin efectos.
- PATCH repetido con los mismos datos deja el recurso en el mismo estado.

---------------------------
Diagrama de arquitectura

[ Cliente (curl / SPA) ]
        |
HTTP/JSON
        |
[ API /api/v1 (DRF ViewSets / URLs) ]
        |
[ Lógica / Serializers (validación de datos) ]
        |
[ Modelo Django (ORM) ]
        |
[ Base de datos SQLite (local) ]

---------------------------
Función de cada capa

- Cliente: Envía solicitudes HTTP con JSON y recibe respuestas.
- API /api/v1: Recibe peticiones y las dirige a los ViewSets según URL y método.
- Lógica / Serializers: Valida datos y convierte JSON ↔ objetos de Django.
- Modelo Django / ORM: Representa datos en Python y traduce operaciones a la base de datos.
- Base de datos SQLite: Almacena persistentemente la información de las tareas.
