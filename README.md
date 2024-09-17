# ApiRest Listar Tareas

Esta API REST permite crear, leer, actualizar y eliminar tareas. Cada tarea tiene un título y un campo booleano para indicar si es 
importante.


 ## Link de la API REST **https://web-production-1868.up.railway.app/api/task**

### Funcionalidades 

- Servir peticiones GET: Enviar solicitud GET a la api que devuelve un archivo en formato JSON con la información de las tareas creadas:
-   **https://web-production-1868.up.railway.app/api/task/**
-   resultado:
~~~
   {
    "id": 1, 
    "title": "Nombre de la tarea ",
    "completed": true 
  },
 {
    "id": 2, 
    "title": "Nombre de la tarea ",
    "completed": true  
  },
 {
    "id": 3, 
    "title": "Nombre de la tarea ",
    "completed": true 
  },
~~~

- Servir peticiones GET: Enviar solicitud GET a un elemento en especifico pasandole el id de lelemento:
-    **https://web-production-1868.up.railway.app/api/task/1**
-   resultado:
~~~
   {
    "id": 1, 
    "title": "Nombre de la tarea ",
    "completed": true 
  },
~~~

- Servir peticiones POST: Enviar solicitud POST a la api donde puedes utilizar un Server client como Postman para llenar
  los campos en formato JSON con la estructura:
  ~~~
  {
    "id": id_tarea, # lo llena la base de datos automaticamente 
    "title": "Nombre de la tarea ",
    "completed": true # campo booleano 
  },
  ~~~

- Servir peticiones PUT: Enviar solicitud PUT a la api para actualizar cualquier registro en la base de datos unicamnete envianndo como parametro el
  numero de id y el los campos a modificar como por ejemplo :

**https://web-production-1868.up.railway.app/api/task/3/**
  ~~~
   {
    "id": 3, 
    "title": "Nombre de la tarea ",
    "completed": true  
  },
  ~~~
  modificamos los campos deseados en est caso el campo completed la pasamos de true a false para verlo hacemos una solicitud GET
  https://web-production-1868.up.railway.app/api/task/3/ y la salida sería 
   ~~~
   {
    "id": 3, 
    "title": "Nombre de la tarea ",
    "completed": flase  
  },
   ~~~
- Servir peticiones DELETE: Envair solicitudes DELETE a la api para aeliminar un registro en la base dedatos pasandole unicamente el numpero de id:
  
  **https://web-production-1868.up.railway.app/api/task/3/** y esto devolverá todos los datos menos la tarea con el id 3:

  ~~~
   [
    {
      "id": 1,
      "title": "cuarta tarea",
      "completed": true
    },
    {
      "id": 2,
      "title": "cuarta tarea",
      "completed": true
    },
  
  ]
  ~~~

## Tecnologías 

**Backend:** 
  - Python version 3.11.0
  - Django version: 5.0.6
  - Django RestFramework: 3.15.2
  
**Base de datos:** 
- Postgresql
  
**Hosting:**
- Render 

## Requisitos previos para utilizarla en tu entorno local:
 * Python y pip instalados
 * Un entorno virtual configurado
Instalación:
 * Clonar el repositorio: git clone https://github.com/lesterdavid31/django-crud-auth-and-taskList.git
 * Crear y activar el entorno virtual:
   python -m venv venv
source venv/bin/activate

 * Instalar las dependencias: pip install
  ~~~
   -r requirements.txt
   ~~~
 * Migrar la base de datos:
 ~~~
   python manage.py migrate
 ~~~

- Con estas configuraciónes puedes probar el código en tu maquina local o puedes utilizar la API REST que tengo la tengo
  en deploy en Render

-**https://web-production-1868.up.railway.app/api/task**




