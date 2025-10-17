# 🧪 Pruebas API Django REST Framework — Tareas

API base: `http://127.0.0.1:8000/api/v1/tareas/`

---

## 1️⃣ Listar todas las tareas (GET → 200 OK)

```bash
curl -X GET http://127.0.0.1:8000/api/v1/tareas/ \
     -H "Content-Type: application/json"
```

**Respuesta esperada:**

```json
[
  {
    "id": 1,
    "titulo": "Hacer Tarea 1",
    "hecho": false,
    "created_at": "2025-10-16 22:00:00"
  }
]
```

---

## 2️⃣ Crear una nueva tarea (POST → 201 Created)

```bash
curl -X POST http://127.0.0.1:8000/api/v1/tareas/ \
     -H "Content-Type: application/json" \
     -d '{"titulo": "Hacer Tarea 1", "hecho": false}'
```

**Respuesta esperada:**

```json
{
  "id": 2,
  "titulo": "Hacer Tarea 2",
  "hecho": false,
  "created_at": "2025-10-16 22:05:00"
}
```

---

## 3️⃣ Ver detalle de una tarea (GET → 200 OK)

```bash
curl -X GET http://127.0.0.1:8000/api/v1/tareas/1/ \
     -H "Content-Type: application/json"
```

**Respuesta esperada:**

```json
{
  "id": 1,
  "titulo": "Hacer Tarea 1",
  "hecho": false,
  "created_at": "2025-10-16 22:00:00"
}
```

---

## 4️⃣ Actualizar estado de la tarea (PATCH → 200 OK)

```bash
curl -X PATCH http://127.0.0.1:8000/api/v1/tareas/1/ \
     -H "Content-Type: application/json" \
     -d '{"hecho": true}'
```

**Respuesta esperada:**

```json
{
  "id": 1,
  "titulo": "Tarea 1 Actualizada",
  "hecho": true,
  "created_at": "2025-10-16 22:00:00"
}
```

---

## 5️⃣ Intentar acceder a un ID inexistente (GET → 404 Not Found)

```bash
curl -X GET http://127.0.0.1:8000/api/v1/tareas/999/ \
     -H "Content-Type: application/json"
```

**Respuesta esperada:**

```json
{
  "detail": "No encontrado."
}
```

---

✅ **Resultado:**
Estos 5 comandos prueban completamente el CRUD de tu API:

* `GET` → listar y detalle
* `POST` → crear
* `PATCH` → actualizar
* `404` → manejo de error al consultar un ID inexistente
